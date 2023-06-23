# -*- coding: utf-8 -*-
# Copyright (c) 2013-2023 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Collection of serial interfaces to LCD devices.
"""

# Example usage:
#
#   from luma.core.interface.serial import spi
#   from luma.core.render import canvas
#   from luma.lcd.device import pcd8544
#   from PIL import ImageDraw
#
#   serial = spi(port=0, device=0)
#   device = pcd8544(serial)
#
#   with canvas(device) as draw:
#      draw.rectangle(device.bounding_box, outline="white", fill="black")
#      draw.text(30, 40, "Hello World", fill="white")
#
# As soon as the with-block scope level is complete, the graphics primitives
# will be flushed to the device.
#
# Creating a new canvas is effectively 'carte blanche': If you want to retain
# an existing canvas, then make a reference like:
#
#    c = canvas(device)
#    for X in ...:
#        with c as draw:
#            draw.rectangle(...)
#
# As before, as soon as the with block completes, the canvas buffer is flushed
# to the device

from time import sleep

from luma.core.lib import rpi_gpio
from luma.core.device import device, parallel_device
from luma.core.interface.serial import noop, pcf8574
from luma.core.framebuffer import diff_to_previous
import luma.core.error
import luma.core.framebuffer
import luma.lcd.const
from luma.lcd.segment_mapper import dot_muncher
from luma.core.virtual import character
from luma.core.bitmap_font import embedded_fonts

__all__ = ["pcd8544", "st7735", "st7789", "ht1621", "uc1701x", "st7567", "ili9341", "ili9486", "ili9488", "hd44780"]


class GPIOBacklight:
    """
    Helper class for controlling the LCD backlight using a digital GPIO output pin.

    :param gpio: GPIO interface (must be compatible with `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_).
    :param pin: the GPIO pin to use for the backlight.
    :type pin: int
    :param active_low: Set to True if active low (default), False otherwise.
    :type active_low: bool
    :raises luma.core.error.UnsupportedPlatform: GPIO access not available.

    .. versionadded:: 2.3.0
    """

    def __init__(self, gpio, pin=18, active_low=True):
        self._gpio = gpio
        self._pin = pin
        if active_low:
            self._enabled = self._gpio.LOW
            self._disabled = self._gpio.HIGH
        else:
            self._enabled = self._gpio.HIGH
            self._disabled = self._gpio.LOW

        try:
            self._gpio.setup(self._pin, self._gpio.OUT)
        except RuntimeError as e:
            if str(e) == 'Module not imported correctly!':
                raise luma.core.error.UnsupportedPlatform('GPIO access not available')

    def __call__(self, is_enabled):
        """
        Toggle the LCD Backlight

        :param is_enabled: Turn backlight on or off.
        :type is_enabled: bool
        """
        assert is_enabled in (True, False)
        self._gpio.output(self._pin, self._enabled if is_enabled else self._disabled)

    def cleanup(self):
        if self._gpio:
            self._gpio.cleanup(self._pin)


class I2CBackpackBacklight:
    """
    Helper class for controlling the LCD backlight when the device is using
    an I2C backpack such as the PCF8574

    :param serial_interface: The serial interface (usually a
        :py:class:`luma.core.interface.serial.pcf8574` instance) that the device
        uses to communicate.
    :param pin: the backpack pin number used to control the backlight on the
        device.
    :type pin: int
    :raises luma.core.error.UnsupportedPlatform: This I2C interfaces does not
        support a backlight.

    .. note: If the I2C interface is already configured to use a backlight, the
        pin setting here will be ignored.

    .. versionadded:: 2.5.0
    """

    def __init__(self, serial_interface, pin=None):
        self._serial_interface = serial_interface

        if not hasattr(serial_interface, "_backlight_enabled"):
            raise luma.core.error.UnsupportedPlatform('This I2C interface does not support a backlight')

        # If the serial_interface has already been set up to use a backlight
        # use its setting, otherwise initialize the backlight from the pin arg
        _be = serial_interface._backlight_enabled
        self._pin = _be if _be else serial_interface._mask(pin) if pin else 0

        serial_interface._backlight_enabled = self._pin

    def __call__(self, is_enabled):
        """
        Toggle the LCD Backlight

        :param is_enabled: Turn on or off the backlight.
        :type is_enabled: bool
        """
        assert is_enabled in (True, False)
        self._serial_interface._backlight_enabled = self._pin if is_enabled else 0


class PWMBacklight:
    """
    Helper class for controlling the LCD backlight using a PWM channel pin.

    :param gpio: GPIO interface (must be compatible with `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_).
    :param pin: the GPIO pin to use for the backlight.
    :type pin: int
    :param frequency: The frequency to use for the PWM channel.
    :type frequency: float
    :raises luma.core.error.UnsupportedPlatform: GPIO access not available.

    .. versionadded:: 2.3.0
    """

    def __init__(self, gpio, pin=18, frequency=362):
        self._gpio = gpio

        try:
            self._pwm = self._gpio.PWM(pin, frequency)
            self._pwm.start(0.0)
            self._pin = pin
        except RuntimeError as e:
            if str(e) == 'Module not imported correctly!':
                raise luma.core.error.UnsupportedPlatform('GPIO access not available')

    def __call__(self, value):
        """
        Set the LCD Backlight

        :param value: Sets the value of the backlight.  Can provide a bool
        (True/False) to turn on/off or a float to set the backlight intensity in
        percentage (0 <= value <= 100.0).
        :type value: bool or float
        """
        if value in (True, False):
            value = 100.0 if value else 0.0
        assert 0.0 <= value <= 100.0
        self._pwm.ChangeDutyCycle(value)

    def cleanup(self):
        if self._gpio:
            self._pwm.stop()
            self._gpio.cleanup(self._pin)


@rpi_gpio
class backlit_device(device):
    """
    Controls a backlight (active low), assumed to be on GPIO 18 (``PWM_CLK0``) by default.

    :param gpio: GPIO interface (must be compatible with `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_).
    :param gpio_LIGHT: The GPIO pin to use for the backlight.
    :type gpio_LIGHT: int
    :param active_low: Set to true if active low (default), false otherwise.
    :type active_low: bool
    :param pwm_frequency: Use PWM for backlight brightness control with the specified frequency when provided.
    :type pwm_frequency: float
    :type backpack_pin: If using an I2C backpack, sets the pin on the backpack that
        is connected to the backlight.
    :type backpack_pin: int
    :raises luma.core.error.UnsupportedPlatform: GPIO access not available.

    .. versionadded:: 2.0.0
    """

    def __init__(self, const=None, serial_interface=None, gpio=None, gpio_LIGHT=18, active_low=True, pwm_frequency=None, backpack_pin=None, **kwargs):
        super(backlit_device, self).__init__(const, serial_interface)

        if backpack_pin or (isinstance(serial_interface, pcf8574) and hasattr(serial_interface, "_backlight_enabled")):
            self.backlight = I2CBackpackBacklight(serial_interface, pin=backpack_pin)
        elif pwm_frequency:
            self._gpio = gpio or self.__rpi_gpio__()
            self.backlight = PWMBacklight(self._gpio, pin=gpio_LIGHT, frequency=pwm_frequency)
        else:
            self._gpio = gpio or self.__rpi_gpio__()
            self.backlight = GPIOBacklight(self._gpio, pin=gpio_LIGHT, active_low=active_low)

        self.persist = True
        self.backlight(True)

    def cleanup(self):
        """
        Attempt to reset the device & switching it off prior to exiting the
        python process.
        """
        if self.persist:
            self.backlight(False)
        try:
            self.backlight.cleanup()
        except AttributeError:
            # Not all backlights require cleanup
            pass
        super(backlit_device, self).cleanup()


class pcd8544(backlit_device):
    """
    Serial interface to a monochrome PCD8544 LCD display.

    On creation, an initialization sequence is pumped to the display
    to properly configure it. Further control commands can then be called to
    affect the brightness and other settings.

    :param serial_interface: The serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    """

    def __init__(self, serial_interface=None, rotate=0, **kwargs):
        super(pcd8544, self).__init__(luma.lcd.const.pcd8544, serial_interface, **kwargs)
        self.capabilities(84, 48, rotate)

        self._mask = [1 << (i // self._w) % 8 for i in range(self._w * self._h)]
        self._offsets = [(self._w * (i // (self._w * 8))) + (i % self._w) for i in range(self._w * self._h)]

        self.contrast(0xB0)
        self.clear()
        self.show()

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and dumps it to the PCD8544
        LCD display.
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        self.command(0x20, 0x80, 0x40)

        buf = bytearray(self._w * self._h // 8)
        off = self._offsets
        mask = self._mask

        for idx, pix in enumerate(image.getdata()):
            if pix > 0:
                buf[off[idx]] |= mask[idx]

        self.data(list(buf))

    def contrast(self, value):
        """
        Sets the LCD contrast
        """
        assert 0 <= value <= 255
        self.command(0x21, 0x14, value | 0x80, 0x20)


class st7789(backlit_device):
    """
    Serial interface to a colour ST7789 240x240 pixel LCD display.

    .. versionadded:: 2.9.0
    """
    def __init__(self, serial_interface=None, width=240, height=240, rotate=0, **kwargs):
        super(st7789, self).__init__(luma.lcd.const.st7789, serial_interface, **kwargs)
        self.capabilities(width, height, rotate, mode="RGB")

        self.command(0x36, 0x70)     # MADCTL (36h): Memory Data Access Control: Bottom to Top, Right to Left, Reverse Mode
        self.command(0x3A, 0x06)     # COLMOD (3Ah): Interface Pixel Format: 18bit/pixel
        self.command(0xB2,          # PORCTRL (B2h): Porch Setting: Disable separate porch control, 0xC in normal mode, 0x3 in idle and partial modes
                     0x0C, 0x0C, 0x00, 0x33, 0x33)
        self.command(0xB7, 0x35)      # GCTRL (B7h): Gate Control: VGH = 13.26V, VGL = -10.43V
        self.command(0xBB, 0x19)      # VCOMS (BBh): VCOM Setting: 0.725V
        self.command(0xC0, 0x2C)    # LCMCTRL (C0h): LCM Control: XBGR, XMX, XMH
        self.command(0xC2, 0x01)   # VDVVRHEN (C2h): VDV and VRH Command Enable: VDV and VRH register value comes from command write
        self.command(0xC3, 0x12)       # VRHS (C3h): VRH Set: 4.45V + (vcom + vcom offset + vdv)
        self.command(0xC4, 0x20)       # VDVS (C4h): VDV Set: 0V
        self.command(0xC6, 0x0F)    # FRCTRL2 (C6h): Frame Rate Control in Normal Mode: 60Hz
        self.command(0xD0,          # PWCTRL1 (D0h): Power Control 1: AVDD = 6.8V, AVCL = -4.8V, VDDS = 2.3V
                     0xA4, 0xA1)
        self.command(0xE0,        # PVGAMCTRL (E0h): Positive Voltage Gamma Control
                     0xD0, 0x04, 0x0D, 0x11, 0x13, 0x2B, 0x3F, 0x54, 0x4C, 0x18, 0x0D, 0x0B, 0x1F, 0x23)
        self.command(0xE1,        # NVGAMCTRL (E1h): Negative Voltage Gamma Control
                     0xD0, 0x04, 0x0C, 0x11, 0x13, 0x2C, 0x3F, 0x44, 0x51, 0x2F, 0x1F, 0x1F, 0x20, 0x23)
        self.command(0x21)            # INVON (21h): Display Inversion On
        self.command(0x11)           # SLPOUT (11h): Sleep Out
        self.command(0x29)           # DISPON (29h): Display On

        self.clear()
        self.show()

    def command(self, cmd, *args):
        """Send a command to the display, with optional arguments.
           The arguments are sent as data bytes, in accordance with the ST7789 datasheet."""
        super(st7789, self).command(cmd)
        if args:
            self.data(args)

    def set_window(self, x1, y1, x2, y2):
        self.command(0x2A,            # CASET (2Ah): Column Address Set
                     x1 >> 8, x1 & 0xFF, (x2 - 1) >> 8, (x2 - 1) & 0xFF)
        self.command(0x2B,            # RASET (2Bh): Row Address Set
                     y1 >> 8, y1 & 0xFF, (y2 - 1) >> 8, (y2 - 1) & 0xFF)
        self.command(0x2C)            # RAMWR (2Ch): Memory Write

    def display(self, image):
        self.set_window(0, 0, self._w, self._h)

        image = self.preprocess(image)
        self.data(list(image.convert("RGB").tobytes()))

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert 0 <= level <= 255


class st7567(backlit_device):
    """
    Serial interface to a monochrome ST7567 128x64 pixel LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param serial_interface: The serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int

    .. versionadded:: 1.1.0
    """

    def __init__(self, serial_interface=None, rotate=0, **kwargs):
        super(st7567, self).__init__(luma.lcd.const.st7567, serial_interface, **kwargs)
        self.capabilities(128, 64, rotate)

        self._pages = self._h // 8

        self.command(0xA3)  # Bias 1/7
        self.command(0xA1)
        self.command(0xC0)  # Normal Orientation
        self.command(0xA6)  # Normal Display (0xA7 = inverse)
        self.command(0x40)
        self.command(0x2F)
        self.command(0x22)
        self.command(0xAF)

        self.contrast(57)

        self.clear()
        self.show()

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and dumps it to the ST7567
        LCD display
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        set_page_address = 0xB0

        image_data = image.getdata()
        pixels_per_page = self.width * 8
        buf = bytearray(self.width)

        for y in range(0, int(self._pages * pixels_per_page), pixels_per_page):
            self.command(set_page_address, 0x04, 0x10)
            set_page_address += 1
            offsets = [y + self.width * i for i in range(8)]

            for x in range(self.width):
                buf[x] = \
                    (image_data[x + offsets[0]] and 0x01) | \
                    (image_data[x + offsets[1]] and 0x02) | \
                    (image_data[x + offsets[2]] and 0x04) | \
                    (image_data[x + offsets[3]] and 0x08) | \
                    (image_data[x + offsets[4]] and 0x10) | \
                    (image_data[x + offsets[5]] and 0x20) | \
                    (image_data[x + offsets[6]] and 0x40) | \
                    (image_data[x + offsets[7]] and 0x80)

            self.data(list(buf))

    def contrast(self, value):
        """
        Sets the LCD contrast
        """
        assert 0 <= value <= 255
        self.command(0x81, value)


class __framebuffer_mixin(object):
    """
    Helper class for initializing the framebuffer. Its only purpose is to
    log a deprecation warning if a string framebuffer is specified.

    .. note::
        Specifying the framebuffer as a string will be removed at the next
        major release, and hence this mixin will become redundant and will
        also be removed at that point.
    """

    def init_framebuffer(self, framebuffer, default_num_segments):
        if framebuffer is None:
            self.framebuffer = diff_to_previous(num_segments=default_num_segments)
        elif isinstance(framebuffer, str):
            import warnings
            warnings.warn(
                "Specifying framebuffer as a string is now deprecated; Supply an instance of class full_frame() or diff_to_previous() instead",
                DeprecationWarning
            )
            self.framebuffer = getattr(luma.core.framebuffer, framebuffer)()
        else:
            self.framebuffer = framebuffer


class st7735(backlit_device, __framebuffer_mixin):
    """
    Serial interface to a 262K color (6-6-6 RGB) ST7735 LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param serial_interface: the serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param width: The number of pixels laid out horizontally.
    :type width: int
    :param height: The number of pixels laid out vertically.
    :type height: int
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param framebuffer: Framebuffering strategy, currently instances of
        ``diff_to_previous()`` or ``full_frame()`` are only supported.
    :type framebuffer: luma.core.framebuffer.framebuffer
    :param bgr: Set to ``True`` if device pixels are BGR order (rather than RGB).
    :type bgr: bool
    :param inverse: Set to ``True`` if device pixels are inversed.
    :type inverse: bool
    :param h_offset: Horizontal offset (in pixels) of screen to device memory
        (default: 0).
    :type h_offset: int
    :param v_offset: Vertical offset (in pixels) of screen to device memory
        (default: 0).
    :type v_offset: int

    .. versionadded:: 0.3.0
    """

    def __init__(self, serial_interface=None, width=160, height=128, rotate=0,
                 framebuffer=None, h_offset=0, v_offset=0, bgr=False, inverse=False, **kwargs):
        super(st7735, self).__init__(luma.lcd.const.st7735, serial_interface, **kwargs)
        self.capabilities(width, height, rotate, mode="RGB")
        self.init_framebuffer(framebuffer, 16)

        if h_offset != 0 or v_offset != 0:
            def offset(bbox):
                left, top, right, bottom = bbox
                return (left + h_offset, top + v_offset, right + h_offset, bottom + v_offset)
            self.apply_offsets = offset
        else:
            self.apply_offsets = lambda bbox: bbox

        # Supported modes
        supported = (width, height) in [(160, 80), (160, 128), (128, 128)]
        if not supported:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        # RGB or BGR order
        order = 0x08 if bgr else 0x00

        self.command(0x01)                       # reset
        self.command(0x11)                       # sleep out & booster on
        self.command(0xB1, 0x01, 0x2C, 0x2D)     # frame rate control: normal mode
        self.command(0xB2, 0x01, 0x2C, 0x2D)     # frame rate control: idle mode
        self.command(0xB3, 0x01, 0x2C, 0x2D,     # frame rate control: partial mode dot inversion mode
                     0x01, 0x2C, 0x2D)           # frame rate control: line inversion mode
        self.command(0xB4, 0x07)                 # display inversion: none
        self.command(0xC0, 0xA2, 0x02, 0x84)     # power control 1: -4.6V auto mode
        self.command(0xC1, 0xC5)                 # power control 2: VGH
        self.command(0xC2, 0x0A, 0x00)           # power control 3: OpAmp current small, boost freq
        self.command(0xC3, 0x8A, 0x2A)           # power control 4: BCLK/2, Opamp current small & Medium low
        self.command(0xC4, 0x8A, 0xEE)           # power control 5: partial mode/full-color
        self.command(0xC5, 0x0E)                 # VCOM Control 1
        self.command(0x36, 0x60 | order)         # memory data access control
        self.command(0x21 if inverse else 0x20)  # display inversion on(0x21)/off(0x20)
        self.command(0x3A, 0x06)                 # interface pixel format
        self.command(0x13)                       # partial off (normal)
        self.command(0xE0,                       # gamma adjustment (+ polarity)
                     0x0F, 0x1A, 0x0F, 0x18, 0x2F, 0x28, 0x20, 0x22,
                     0x1F, 0x1B, 0x23, 0x37, 0x00, 0x07, 0x02, 0x10)
        self.command(0xE1,                       # gamma adjustment (- polarity)
                     0x0F, 0x1B, 0x0F, 0x17, 0x33, 0x2C, 0x29, 0x2E,
                     0x30, 0x30, 0x39, 0x3F, 0x00, 0x07, 0x03, 0x10)

        self.clear()
        self.show()

    def display(self, image):
        """
        Renders a 24-bit RGB image to the ST7735 LCD display. The 8-bit RGB
        values are passed directly to the devices internal storage, but only
        the 6 most-significant bits are used by the display.

        :param image: The image to render.
        :type image: PIL.Image.Image
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        for image, bounding_box in self.framebuffer.redraw(image):
            left, top, right, bottom = self.apply_offsets(bounding_box)

            self.command(0x2A, left >> 8, left & 0xFF, (right - 1) >> 8, (right - 1) & 0xFF)     # Set column addr
            self.command(0x2B, top >> 8, top & 0xFF, (bottom - 1) >> 8, (bottom - 1) & 0xFF)     # Set row addr
            self.command(0x2C)                                                                   # Memory write

            self.data(list(image.tobytes()))

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert 0 <= level <= 255

    def command(self, cmd, *args):
        """
        Sends a command and an (optional) sequence of arguments through to the
        delegated serial interface. Note that the arguments are passed through
        as data.
        """
        self._serial_interface.command(cmd)
        if len(args) > 0:
            self._serial_interface.data(list(args))


class ili9341(backlit_device, __framebuffer_mixin):
    """
    Serial interface to a 262k color (6-6-6 RGB) ILI9341 LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param serial_interface: the serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param width: The number of pixels laid out horizontally.
    :type width: int
    :param height: The number of pixels laid out vertically.
    :type height: int
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param framebuffer: Framebuffering strategy, currently instances of
        ``diff_to_previous()`` or ``full_frame()`` are only supported.
    :type framebuffer: luma.core.framebuffer.framebuffer
    :param bgr: Set to ``True`` if device pixels are BGR order (rather than RGB).
    :type bgr: bool
    :param h_offset: Horizontal offset (in pixels) of screen to device memory
        (default: 0).
    :type h_offset: int
    :param v_offset: Vertical offset (in pixels) of screen to device memory
        (default: 0).
    :type v_offset: int

    .. versionadded:: 2.2.0
    """

    def __init__(self, serial_interface=None, width=320, height=240, rotate=0,
                 framebuffer=None, h_offset=0, v_offset=0, bgr=False, **kwargs):
        super(ili9341, self).__init__(luma.lcd.const.ili9341, serial_interface, **kwargs)
        self.capabilities(width, height, rotate, mode="RGB")
        self.init_framebuffer(framebuffer, 25)

        if h_offset != 0 or v_offset != 0:
            def offset(bbox):
                left, top, right, bottom = bbox
                return (left + h_offset, top + v_offset, right + h_offset, bottom + v_offset)
            self.apply_offsets = offset
        else:
            self.apply_offsets = lambda bbox: bbox

        # Supported modes
        supported = (width, height) in [(320, 240), (240, 240), (320, 180)]  # full, 1x1, 16x9
        if not supported:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        # RGB or BGR order
        order = 0x00 if bgr else 0x08

        # Note: based on the Adafruit implementation at
        # `https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display` (MIT licensed)

        self.command(0xef, 0x03, 0x80, 0x02)              # ?
        self.command(0xcf, 0x00, 0xc1, 0x30)              # Power control B
        self.command(0xed, 0x64, 0x03, 0x12, 0x81)        # Power on sequence control
        self.command(0xe8, 0x85, 0x00, 0x78)              # Driver timing control A
        self.command(0xcb, 0x39, 0x2c, 0x00, 0x34, 0x02)  # Power control A
        self.command(0xf7, 0x20)                          # Pump ratio control
        self.command(0xea, 0x00, 0x00)                    # Driver timing control B
        self.command(0xc0, 0x23)                          # Power Control 1, VRH[5:0]
        self.command(0xc1, 0x10)                          # Power Control 2, SAP[2:0], BT[3:0]
        self.command(0xc5, 0x3e, 0x28)                    # VCM Control 1
        self.command(0xc7, 0x86)                          # VCM Control 2
        self.command(0x36, 0x20 | order)                  # Memory Access Control
        self.command(0x3a, 0x46)                          # Pixel Format 6-6-6
        self.command(0xb1, 0x00, 0x18)                    # FRMCTR1
        self.command(0xb6, 0x08, 0x82, 0x27)              # Display Function Control
        self.command(0xf2, 0x00)                          # 3Gamma Function Disable
        self.command(0x26, 0x01)                          # Gamma Curve Selected
        self.command(0xe0,                                # Set Gamma (+ polarity)
                     0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1,
                     0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00)
        self.command(0xe1,                                # Set Gamma (- polarity)
                     0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1,
                     0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f)
        self.command(0x11)                                # Sleep out
        sleep(0.12)
        self.clear()
        self.show()

    def display(self, image):
        """
        Renders a 24-bit RGB image to the ILI9341 LCD display. The 8-bit RGB
        values are passed directly to the devices internal storage, but only
        the 6 most-significant bits are used by the display.

        :param image: The image to render.
        :type image: PIL.Image.Image
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        for image, bounding_box in self.framebuffer.redraw(image):
            left, top, right, bottom = self.apply_offsets(bounding_box)

            self.command(0x2a, left >> 8, left & 0xff, (right - 1) >> 8, (right - 1) & 0xff)     # Set column addr
            self.command(0x2b, top >> 8, top & 0xff, (bottom - 1) >> 8, (bottom - 1) & 0xff)     # Set row addr
            self.command(0x2c)                                                                   # Memory write

            self.data(image.tobytes())

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert 0 <= level <= 255

    def command(self, cmd, *args):
        """
        Sends a command and an (optional) sequence of arguments through to the
        delegated serial interface. Note that the arguments are passed through
        as data.
        """
        self._serial_interface.command(cmd)
        if len(args) > 0:
            self._serial_interface.data(list(args))


class ili9486(backlit_device, __framebuffer_mixin):
    """
    Serial interface to a 262k color (6-6-6 RGB) ILI9486 LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness (if implemented) and other settings.

    Note that the ILI9486 display used for development -- a Waveshare
    3.5-inch IPS LCD(B) -- used a portrait orientation.  Images were
    rendered correctly only when specifying that height was 480 pixels
    and the width was 320.

    :param serial_interface: the serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param width: The number of pixels laid out horizontally.
    :type width: int
    :param height: The number of pixels laid out vertically.
    :type height: int
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param framebuffer: Framebuffering strategy, currently instances of
        ``diff_to_previous()`` or ``full_frame()`` are only supported.
    :type framebuffer: luma.core.framebuffer.framebuffer
    :param bgr: Set to ``True`` if device pixels are BGR order (rather than RGB).
    :type bgr: bool
    :param h_offset: Horizontal offset (in pixels) of screen to device memory
        (default: 0).
    :type h_offset: int
    :param v_offset: Vertical offset (in pixels) of screen to device memory
        (default: 0).
    :type v_offset: int

    .. versionadded:: 2.8.0
    """

    def __init__(self, serial_interface=None, width=320, height=480, rotate=0,
                 framebuffer=None, h_offset=0, v_offset=0, bgr=False, **kwargs):
        super(ili9486, self).__init__(luma.lcd.const.ili9486, serial_interface, **kwargs)
        self.capabilities(width, height, rotate, mode="RGB")
        self.init_framebuffer(framebuffer, 25)

        if h_offset != 0 or v_offset != 0:
            def offset(bbox):
                left, top, right, bottom = bbox
                return (left + h_offset, top + v_offset, right + h_offset, bottom + v_offset)
            self.apply_offsets = offset
        else:
            self.apply_offsets = lambda bbox: bbox

        # Supported modes
        supported = (width, height) in [(320, 480)]  # full
        if not supported:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        # RGB or BGR order
        order = 0x00 if bgr else 0x08

        # Initialization sequence, adapted from MIT Licensed
        #
        #   `https://github.com/juj/fbcp-ili9341/blob/master/ili9486.cpp`
        #
        # and peer files.  The sequence targets the ILI9486-based
        # Waveshare "Wavepear" 3.5 inch 320x480 LCD (B)
        # implementation.  Per comments in the above file and issue
        # discussion for juj/fbcp-ili9341, the Waveshare
        # implementation makes use of 16-bit shift register for the
        # SPI interface, leaving the ILI9486 itself in a parallel
        # mode.
        #
        # The result of that implementation is that registers
        # effectively become 16-bit quantities.  The sequence below
        # (and in the display() function) thus ends up padding
        # commands and subsequent values.  It doesn't seem to have
        # affected pixel transfers, though.
        #
        # A different ILI9486 implementation may NOT need the padding
        # zeros.  The juj/fbcp-ili9341 code handles that possibility
        # via a DISPLAY_SPI_BUS_IS_16BITS_WIDE ifdef.

        self.command(0xb0, 0x00, 0x00)                      # Interface Mode Control
        self.command(0x11)                                  # sleep out
        sleep(0.150)
        self.command(0x3a, 0x00, 0x66)                      # Interface Pixel Format 6-6-6
        self.command(0x21)                                  # Display inversion ON for LCD(B)
        self.command(0xc0, 0x00, 0x09, 0x00, 0x09)          # Power Control 1
        self.command(0xc1, 0x00, 0x41, 0x00, 0x00)          # Power Control 2
        self.command(0xc2, 0x00, 0x33)                      # Power Control 3 (for normal mode)
        self.command(0xc5, 0x00, 0x00, 0x00, 0x36)          # VCOM control

        self.command(0x36, 0x00, 0x00 | order)              # Memory Access control (MAD), rotations and color order
        # self.command(0xb1, 0x00, 0xb0, 0x00, 0xe0)          # Frame Rate Control (needed?)

        self.command(0xb6, 0x00, 0x00, 0x00, 0x42, 0x00, 59)        # Display Function Control

        # Initial trials didn't seem to need Positive, Negative, or
        # Digital Gamma Control settings.

        self.command(0x13)                                  # Normal mode ON
        self.command(0x34)                                  # Tearing effect line oFF
        self.command(0x38)                                  # Idle mode OFF

        self.command(0x11)                                  # sleep out
        sleep(0.150)
        self.clear()
        self.show()

    def display(self, image):
        """
        Renders a 24-bit RGB image to the ILI9486 LCD display. The 8-bit RGB
        values are passed directly to the devices internal storage, but only
        the 6 most-significant bits are used by the display.

        :param image: The image to render.
        :type image: PIL.Image.Image
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        for image, bounding_box in self.framebuffer.redraw(image):
            # Transposing the display shifts the dimension measurements
            top, left, bottom, right = self.apply_offsets(bounding_box)

            # Per earlier comments, Waveshare's display needs padding
            # for commands.
            self.command(0x2a, 0, top >> 8, 0, top & 0xff, 0, (bottom - 1) >> 8, 0, (bottom - 1) & 0xff)     # Set row addr
            self.command(0x2b, 0, left >> 8, 0, left & 0xff, 0, (right - 1) >> 8, 0, (right - 1) & 0xff)     # Set column addr
            self.command(0x2c)                                                                   # Memory write

            self.data(image.tobytes())

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert 0 <= level <= 255

    def command(self, cmd, *args):
        """
        Sends a command and an (optional) sequence of arguments through to the
        delegated serial interface. Note that the arguments are passed through
        as data.
        """
        self._serial_interface.command(cmd)
        if len(args) > 0:
            self._serial_interface.data(list(args))


class ili9488(backlit_device, __framebuffer_mixin):
    """
    Serial interface to a 262k color (6-6-6 RGB) ILI9488 LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param serial_interface: the serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param width: The number of pixels laid out horizontally.
    :type width: int
    :param height: The number of pixels laid out vertically.
    :type height: int
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param framebuffer: Framebuffering strategy, currently instances of
        ``diff_to_previous()`` or ``full_frame()`` are only supported.
    :type framebuffer: luma.core.framebuffer.framebuffer
    :param bgr: Set to ``True`` if device pixels are BGR order (rather than RGB).
    :type bgr: bool
    :param h_offset: Horizontal offset (in pixels) of screen to device memory
        (default: 0).
    :type h_offset: int
    :param v_offset: Vertical offset (in pixels) of screen to device memory
        (default: 0).
    :type v_offset: int

    .. versionadded:: 2.11.0
    """

    def __init__(self, serial_interface=None, width=480, height=320, rotate=0,
                 framebuffer=None, h_offset=0, v_offset=0, bgr=False, **kwargs):
        super(ili9488, self).__init__(luma.lcd.const.ili9488, serial_interface, **kwargs)
        self.capabilities(width, height, rotate, mode="RGB")
        self.init_framebuffer(framebuffer, 25)

        if h_offset != 0 or v_offset != 0:
            def offset(bbox):
                left, top, right, bottom = bbox
                return (left + h_offset, top + v_offset, right + h_offset, bottom + v_offset)
            self.apply_offsets = offset
        else:
            self.apply_offsets = lambda bbox: bbox

        # Supported modes
        supported = (width, height) in [(480, 320)]
        if not supported:
            raise luma.core.error.DeviceDisplayModeError(
                f"Unsupported display mode: {width} x {height}")

        # RGB or BGR order
        order = 0x00 if bgr else 0x08

        # Initialization sequence, adapted from
        #
        # https://github.com/birdtechstep/fbtft/blob/master/fb_ili9488.c
        #

        self.command(0xe0, 0x00, 0x03, 0x09, 0x08, 0x16, 0x0a, 0x37,   # Positive Gamma Control
                     0x78, 0x4c, 0x09, 0x0a, 0x08, 0x16, 0x1a, 0x0f)
        self.command(0xe1, 0x00, 0x16, 0x19, 0x03, 0x0f, 0x05, 0x32,
                     0x45, 0x46, 0x04, 0x0e, 0x0d, 0x35, 0x37, 0x0f)  # Negative Gamma Control
        self.command(0xc0, 0x17, 0x15)                                 # Power Control 1
        self.command(0xc1, 0x41)                                       # Power Control 2
        self.command(0xc5, 0x00, 0x12, 0x80)                           # VCOM Control
        self.command(0x36, 0x20 | order)                               # Memory Access Control
        self.command(0x3a, 0x66)                                       # Interface Pixel Format 6-6-6
        self.command(0xb0, 0x00)                                       # Interface Mode Control
        self.command(0xb1, 0xa0)                                       # Frame Rate Control
        self.command(0xb4, 0x02)                                       # Display Inversion Control
        self.command(0xb6, 0x02, 0x02, 0x3b)                           # Display Function Control
        self.command(0xb7, 0xc6)                                       # Entry Mode Set
        self.command(0xf7, 0xa9, 0x51, 0x2c, 0x82)                     # Interface Mode Control
        self.command(0x11)                                             # Sleep Out
        sleep(0.120)
        self.clear()
        self.show()

    def display(self, image):
        """
        Renders a 24-bit RGB image to the ILI9488 LCD display. The 8-bit RGB
        values are passed directly to the devices internal storage, but only
        the 6 most-significant bits are used by the display.

        :param image: The image to render.
        :type image: PIL.Image.Image
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        for image, bounding_box in self.framebuffer.redraw(image):
            left, top, right, bottom = self.apply_offsets(bounding_box)

            self.command(0x2a, left >> 8, left & 0xff, (right - 1) >> 8, (right - 1) & 0xff)     # Set column addr
            self.command(0x2b, top >> 8, top & 0xff, (bottom - 1) >> 8, (bottom - 1) & 0xff)     # Set row addr
            self.command(0x2c)                                                                   # Memory write

            self.data(image.tobytes())

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert 0 <= level <= 255

    def command(self, cmd, *args):
        """
        Sends a command and an (optional) sequence of arguments through to the
        delegated serial interface. Note that the arguments are passed through
        as data.
        """
        self._serial_interface.command(cmd)
        if len(args) > 0:
            self._serial_interface.data(list(args))


@rpi_gpio
class ht1621(backlit_device):
    """
    Serial interface to a seven segment HT1621 monochrome LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param gpio: The GPIO library to use (usually RPi.GPIO)
        to delegate sending data and commands through.
    :param width: The number of 7 segment characters laid out horizontally.
    :type width: int
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param WR: The write (SPI clock) pin to connect to, default BCM 11.
    :type WR: int
    :param DAT: The data pin to connect to, default BCM 10.
    :type DAT: int
    :param CS: The chip select pin to connect to, default BCM 8.
    :type CS: int

    .. versionadded:: 0.4.0
    """

    def __init__(self, gpio=None, width=6, rotate=0, WR=11, DAT=10, CS=8, **kwargs):
        if 'serial_interface' in kwargs:
            del kwargs['serial_interface']
        super(ht1621, self).__init__(luma.lcd.const.ht1621, noop(), gpio=gpio, **kwargs)
        self.capabilities(width, 8, rotate)
        self.segment_mapper = dot_muncher
        self._gpio = gpio or self.__rpi_gpio__()

        self._WR = self._configure(WR)
        self._DAT = self._configure(DAT)
        self._CS = self._configure(CS)

        self.command(0x30)   # Internal RC oscillator @ 256KHz
        self.command(0x52)   # 1/2 Bias and 4 commons
        self.command(0x02)   # System enable

        self.clear()
        self.show()

    def _configure(self, pin):
        if pin is not None:
            self._gpio.setup(pin, self._gpio.OUT)
            return pin

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and dumps it to the PCD8544
        LCD display.
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        buf = []

        for x in range(self._w):
            byte = 0
            for y in range(self._h):
                if image.getpixel((x, y)) > 0:
                    byte |= 1 << y

            buf.append(byte)

        self.data(buf)

    def command(self, cmd):
        gpio = self._gpio
        gpio.output(self._CS, gpio.LOW)
        self._write_bits(0x80, 4)   # Command mode
        self._write_bits(cmd, 8)
        gpio.output(self._CS, gpio.HIGH)

    def data(self, data):
        gpio = self._gpio
        gpio.output(self._CS, gpio.LOW)
        self._write_bits(0xA0, 3)   # Write mode
        self._write_bits(0x00, 6)   # Address
        for byte in data:
            self._write_bits(byte, 8)
        gpio.output(self._CS, gpio.HIGH)

    def _write_bits(self, value, num_bits):
        gpio = self._gpio
        for _ in range(num_bits):
            gpio.output(self._WR, gpio.LOW)
            bit = gpio.HIGH if value & 0x80 > 0 else gpio.LOW
            gpio.output(self._DAT, bit)
            value <<= 1
            gpio.output(self._WR, gpio.HIGH)

    def cleanup(self):
        """
        Attempt to reset the device & switching it off prior to exiting the
        python process.
        """
        super(ht1621, self).cleanup()
        self.command(0x00)   # System disable
        self._gpio.cleanup()


class uc1701x(backlit_device):
    """
    Serial interface to a monochrome UC1701X LCD display.

    On creation, an initialization sequence is pumped to the display to properly
    configure it. Further control commands can then be called to affect the
    brightness and other settings.

    :param serial_interface: The serial interface (usually a
        :py:class:`luma.core.interface.serial.spi` instance) to delegate sending
        data and commands through.
    :param rotate: An integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int

    .. versionadded:: 0.5.0
    """

    def __init__(self, serial_interface=None, rotate=0, **kwargs):
        super(uc1701x, self).__init__(luma.lcd.const.uc1701x, serial_interface, **kwargs)
        self.capabilities(128, 64, rotate)

        self._pages = self._h // 8

        self.command(0xE2)          # System reset
        self.command(0x2C)          # Power: Boost ON
        self.command(0x2E)          # Power: Voltage Regulator ON
        self.command(0x2F)          # Power: Voltage Follower ON
        self.command(0xF8, 0x00)    # Booster ratio to 4x
        self.command(0x23)          # Set resistor ratio = 3
        self.command(0xA2)          # Bias 1/9
        self.command(0xC0)          # Set COM direction
        self.command(0xA1)          # Set SEG direction
        self.command(0xAC)          # Static indicator
        self.command(0xA6)          # Disable inverse
        self.command(0xA5)          # Display all points
        self.command(0xA4)          # Normal Display

        self.contrast(0xB0)

        self.clear()
        self.show()

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and dumps it to the UC1701X
        LCD display.
        """
        assert image.mode == self.mode
        assert image.size == self.size

        image = self.preprocess(image)

        set_page_address = 0xB0
        image_data = image.getdata()
        pixels_per_page = self.width * 8
        buf = bytearray(self.width)

        for y in range(0, int(self._pages * pixels_per_page), pixels_per_page):
            self.command(set_page_address, 0x04, 0x10)
            set_page_address += 1
            offsets = [y + self.width * i for i in range(8)]

            for x in range(self.width):
                buf[x] = \
                    (image_data[x + offsets[0]] and 0x01) | \
                    (image_data[x + offsets[1]] and 0x02) | \
                    (image_data[x + offsets[2]] and 0x04) | \
                    (image_data[x + offsets[3]] and 0x08) | \
                    (image_data[x + offsets[4]] and 0x10) | \
                    (image_data[x + offsets[5]] and 0x20) | \
                    (image_data[x + offsets[6]] and 0x40) | \
                    (image_data[x + offsets[7]] and 0x80)

            self.data(list(buf))

    def contrast(self, value):
        """
        Sets the LCD contrast
        """
        assert 0 <= value <= 255
        self.command(0x81, value >> 2)


class hd44780(backlit_device, parallel_device, character, __framebuffer_mixin):
    """
    Driver for a HD44780 style LCD display.  This class provides a ``text``
    property which can be used to set and get a text value, which will be
    rendered to the display's screen using the display's built-in font.

    :param serial_interface: The serial interface (usually a
        :py:class:`luma.core.interface.serial.parallel` instance) to delegate
        sending data and commands through.
    :param width: The number of characters that can be displayed on a line.
    :type width: int
    :param height: The number of lines the display supports.
    :type height: int
    :param undefined: character to use if a requested character is not in the
        font tables
    :type undefined: str
    :param selected_font: the font table appropriate for the model of display
        you are using.  The hd44780 normally comes in a version with font A00
        (ENGLISH_JAPANESE) or A02 (ENGLISH_EUROPEAN).  You can provide either
        the name ('A00' or 'A02') or the number (0 for 'A00', 1 for 'A02') for
        the font your display contains.
    :type selected_font: int or str
    :param exec_time: Time in seconds to wait for a command to complete.
        Default is 50 μs (1e-6 * 50) which typically is long enough for commands
        to finish.  If your display is not working correctly, you may want to
        try increasing the exec_time delay.
    :type exec_time: float
    :param gpio_LIGHT: The GPIO pin to use for the backlight if it is controlled by
        one of the GPIO pins.
    :type gpio_LIGHT: int
    :param active_low: Set to true if backlight is active low (default), false
        otherwise.
    :type active_low: bool
    :param pwm_frequency: Use PWM for backlight brightness control with the
        specified frequency when provided.
    :type pwm_frequency: float
    :type backpack_pin: If using an I2C backpack, sets the pin on the backpack that
        is connected to the backlight.  This is unnecessary if it has already been
        configured on the interface.
    :type backpack_pin: int
    :param framebuffer: Framebuffering strategy, currently instances of
        ``diff_to_previous()`` or ``full_frame()`` are only supported.
    :type framebuffer: luma.core.framebuffer.framebuffer

    To place text on the display, simply assign the text to the ``text``
    instance variable::

        p = parallel(RS=7, E=8, PINS=[25,24,23,18])
        my_display = hd44780(p, selected_font='A00')
        my_display.text = 'HD44780 Display\\nFont A00 Eng/Jap'

    For more details on how to use the 'text' interface see
    :class:`luma.core.virtual.character`

    ..note:
        This driver currently only supports the hd44780 5x8 display mode.

    .. versionadded:: 2.5.0
    """

    def __init__(self, serial_interface=None, width=16, height=2, undefined='_',
                 selected_font=0, exec_time=0.000001, framebuffer=None, **kwargs):
        super(hd44780, self).__init__(luma.lcd.const.hd44780, serial_interface,
        exec_time=exec_time, **kwargs)

        # Inherited from parallel_device class but multi-inheritence with
        # backlit_device requires it to be initialized here
        self._exec_time = exec_time

        self.capabilities(width * 5, height * 8, 0)
        self.init_framebuffer(framebuffer, 1)

        # Currently only support 5x8 fonts for the hd44780
        self.font = embedded_fonts(self._const.FONTDATA,
            selected_font=selected_font)
        self.glyph_index = self.font.current.glyph_index
        self.device = self
        self._undefined = undefined
        self._custom = {}

        # Supported modes
        supported = (width, height) in [(16, 2), (16, 4), (20, 2), (20, 4)]
        if not supported:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        self._initialize_device()
        self.text = ''
        self.command(self._const.CLEAR, exec_time=1e-3 * 1.5)

    def _initialize_device(self):
        """
        HD44780 Initialization Routine

        Command Values
        FUNCTIONSET = 0x20
        DL8 = 0x10
        DL4 = 0x00
        LINES2 = 0x08
        LINES1 = 0x00
        CHAR5x8 = 0x00
        CHAR5x10 = 0x04
        DISPLAYOFF = 0x08
        DISPLAYON = 0x0C
        CLEAR = 0x01
        ENTRY = 0x06

        8 bit mode
        Action                                                            Delay
        ----------------------------------------------------------------  -------
        PowerOn                                                           40.0ms
        Command 0x30                                                       4.1ms
        Command 0x30                                                       100μs
        Command 0x30                                                        40μs
        Command FUNCTIONSET|DL8|(LINES2 or LINES1)|(CHAR5x8 or CHAR5x10)    40μs
        Command DISPLAYOFF                                                  40μs
        Command CLEAR                                                       40μs
        Command ENTRY ; No shift, incrementing display                      40μs

        4bit mode
        Action                                                            Delay
        ----------------------------------------------------------------  -------
        PowerOn                                                           40.0ms
        Command 0x03 ; 4 bit write                                         4.1ms
        Command 0x03 ; 4 bit write                                         100μs
        Command 0x32                                                        40μs
        Command FUNCTIONSET|DL4|(LINES2 or LINES1)|(CHAR5x8 or CHAR5x10)    40μs
        Command DISPLAYOFF                                                  40μs
        Command CLEAR                                                       40μs
        Command ENTRY ; No shift, incrementing display                      40μs

        Device is now ready to receive data
        """
        sleep(1e-3 * 100)
        if self._bitmode == 8:
            self.command(0x30, exec_time=1e-3 * 10)
            self.command(0x30, exec_time=1e-6 * 200)
            self.command(0x30)
        else:
            # In case of stubborn display place in 8 bit mode three times and
            # and then try to get it into four bit mode
            for _ in range(3):
                self.command(0x03, exec_time=1e-3 * 10, only_low_bits=True)
                self.command(0x03, exec_time=1e-3 * 10, only_low_bits=True)
                self.command(0x33, exec_time=1e-3 * 100)
            self.command(0x03, exec_time=1e-3 * 10, only_low_bits=True)
            self.command(0x03, exec_time=1e-6 * 200, only_low_bits=True)
            self.command(0x32)

        dl = self._const.DL8 if self._bitmode == 8 else self._const.DL4
        self.command(self._const.FUNCTIONSET | dl | self._const.LINES2)
        self.command(self._const.DISPLAYOFF)  # Set Display Off
        self.command(self._const.ENTRY)  # Set entry mode to right, no shift
        self.command(self._const.DISPLAYON, exec_time=1e-3 * 100)  # Turn display on

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and converts it to text data
        by reversing from glyphs from the image back to the correct
        value from the displays font table.

        :param image: the image to place on the display
        :type image: :py:class:`PIL.Image.Image`

        If needed, it will create custom characters if a glyph is not found
        within the font table.

        .. note:
            Most hd44780s have limited memory to support custom characters
            and typically can only support 8 at any one time.  If this is
            exceeded, the remaining unmatched characters will be replaced by
            the ``undefined`` character.
        """
        assert image.mode == self.mode
        assert image.size == self.size

        for image_segment, bounding_box in self.framebuffer.redraw(image):
            self._cleanup_custom(image_segment)
            # Expand bounding box to align to cell boundaries (5,8)
            left, top, right, bottom = bounding_box
            left = left // 5 * 5
            right = right // 5 * 5 if not right % 5 else (right // 5 + 1) * 5
            top = top // 8 * 8
            bottom = bottom // 8 * 8 if not bottom % 8 else (bottom // 8 + 1) * 8

            for j in range(top // 8, bottom // 8):
                buf = []
                for i in range(left // 5, right // 5):
                    img = image.crop((i * 5, j * 8, (i + 1) * 5, (j + 1) * 8))
                    bytes = img.tobytes()
                    c = self.glyph_index[bytes] if bytes in self.glyph_index else \
                        self._custom[bytes] if bytes in self._custom else None
                    if c is None:
                        self._make_custom(img)
                        c = self._custom.get(bytes, ord(self._undefined))
                    buf.append(c)
                self.command(self._const.DDRAMADDR | (self._const.LINES[j] + (left // 5)))
                self.data(buf)

    def _make_custom(self, img):
        """
        Create a new custom character based upon the provided image

        .. note:
            The image must be the same size as the font mode of the display.
        """
        assert img.size == (5, 8)
        if len(self._custom) == self._const.CUSTOMCHARS:
            # Max custom characters already reached
            return
        idx = 0
        for _ in range(self._const.CUSTOMCHARS):
            if idx not in self._custom.values():
                break
            idx += 1
        assert idx < self._const.CUSTOMCHARS

        self.command(self._const.CGRAMADDR + (idx * 8))
        data = [int(bool(i)) for i in img.getdata()]
        buf = []
        for j in range(8):
            buf.append(sum(v << (4 - i) for i, v in
                enumerate(data[j * 5:(j + 1) * 5])))
        self.data(buf)
        self._custom[img.tobytes()] = idx

    def _cleanup_custom(self, img):
        """
        Look across new image and remove any custom characters that are not
        needed to render the image
        """

        # If no custom characters then we can exit without the search
        if len(self._custom) == 0:
            return

        in_use = []
        for j in range(img.size[1] // 8):
            for i in range(img.size[0] // 5):
                data = img.crop((i * 5, j * 8, (i + 1) * 5, (j + 1) * 8)).tobytes()
                if data in self._custom:
                    in_use.append(data)
        self._custom = {k: v for k, v in self._custom.items() if k in in_use}

    def get_font(self, ft):
        """
        Return one of the devices built-in fonts as a :py:mod:`PIL.ImageFont`
        object

        :param ft: name or number of the font to return (0 - A00, 1 - A02)
        :type ft: int or str
        """
        return self.font.load(ft)

    def contrast(self, *args):
        """
        Not support on this device.  Ignore.
        """
        pass
