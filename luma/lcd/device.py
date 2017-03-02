# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

# Example usage:
#
#   from luma.core.serial import spi
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

from luma.core.device import device
import luma.core.error
import luma.core.framebuffer
import luma.lcd.const


__all__ = ["pcd8544"]


class pcd8544(device):
    """
    Encapsulates the serial interface to the monochrome PCD8544 LCD display
    hardware. On creation, an initialization sequence is pumped to the display
    to properly configure it. Further control commands can then be called to
    affect the brightness and other settings.
    """
    def __init__(self, serial_interface=None, width=84, height=48, rotate=0,
                 backlight=18, **kwargs):
        super(pcd8544, self).__init__(luma.lcd.const.pcd8544, serial_interface)
        self.capabilities(width, height, rotate)

        if width != 84 or height != 48:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        self._mask = [1 << (i // width) % 8 for i in range(width * height)]
        self._offsets = [(width * (i // (width * 8))) + (i % width) for i in range(width * height)]

        self.contrast(0xB0)
        self.clear()
        self.show()

    def display(self, image):
        """
        Takes a 1-bit :py:mod:`PIL.Image` and dumps it to the PCD8544
        LCD display.
        """
        assert(image.mode == self.mode)
        assert(image.size == self.size)

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
        assert(0 <= value <= 255)
        self.command(0x21, 0x14, value | 0x80, 0x20)


class st7735(device):
    """
    Encapsulates the serial interface to the 262K color (6-6-6 RGB) ST7735
    LCD display hardware. On creation, an initialization sequence is pumped to
    the display to properly configure it. Further control commands can then be
    called to affect the brightness and other settings.

    :param serial_interface: the serial interface (usually a
        :py:class`luma.core.serial.spi` instance) to delegate sending data and
        commands through.
    :param width: the number of horizontal pixels (optional, defaults to 160)
    :type width: int
    :param height: the number of vertical pixels (optional, defaults to 128)
    :type height: int
    :param rotate: an integer value of 0 (default), 1, 2 or 3 only, where 0 is
        no rotation, 1 is rotate 90° clockwise, 2 is 180° rotation and 3
        represents 270° rotation.
    :type rotate: int
    :param framebuffer: Framebuffering strategy, currently values of
        "diff_to_previous" or "full_frame" are only supported
    :param framebuffer: str
    :param bgr: set to `True` if device pixels are BGR order (rather than RGB)
    :type bgr: bool
    """
    def __init__(self, serial_interface=None, width=160, height=128, rotate=0,
                 framebuffer="diff_to_previous", bgr=False, **kwargs):
        super(st7735, self).__init__(luma.lcd.const.st7735, serial_interface)
        self.capabilities(width, height, rotate, mode="RGB")
        self.framebuffer = getattr(luma.core.framebuffer, framebuffer)(self)

        # RGB or BGR order
        order = 0x08 if bgr else 0x00

        if width != 160 or height != 128:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        self.command(0x01)                      # reset
        self.command(0x11)                      # sleep out & booster on
        self.command(0xB1, 0x01, 0x2C, 0x2D)    # frame rate control: normal mode
        self.command(0xB2, 0x01, 0x2C, 0x2D)    # frame rate control: idle mode
        self.command(0xB3, 0x01, 0x2C, 0x2D,    # frame rate control: partial mode dot inversion mode
                     0x01, 0x2C, 0x2D)          # frame rate control: line inversion mode
        self.command(0xB4, 0x07)                # display inversion: none
        self.command(0xC0, 0xA2, 0x02, 0x84)    # power control 1: -4.6V auto mode
        self.command(0xC1, 0xC5)                # power control 2: VGH
        self.command(0xC2, 0x0A, 0x00)          # power control 3: OpAmp current small, boost freq
        self.command(0xC3, 0x8A, 0x2A)          # power control 4: BCLK/2, Opamp current small & Medium low
        self.command(0xC4, 0x8A, 0xEE)          # power control 5: partial mode/full-color
        self.command(0xC5, 0x0E)                # VCOM Control 1
        self.command(0x36, 0x60 | order)        # memory data access control
        self.command(0x20)                      # display inversion off
        self.command(0x3A, 0x06)                # interface pixel format
        self.command(0x13)                      # partial off (normal)
        self.command(0xE0,                      # gamma adjustment (+ polarity)
                     0x0F, 0x1A, 0x0F, 0x18, 0x2F, 0x28, 0x20, 0x22,
                     0x1F, 0x1B, 0x23, 0x37, 0x00, 0x07, 0x02, 0x10)
        self.command(0xE1,                      # gamma adjustment (- polarity)
                     0x0F, 0x1B, 0x0F, 0x17, 0x33, 0x2C, 0x29, 0x2E,
                     0x30, 0x30, 0x39, 0x3F, 0x00, 0x07, 0x03, 0x10)

        self.clear()
        self.show()

    def display(self, image):
        """
        Renders a 24-bit RGB image to the ST7735 LCD display

        :param image: the image to render
        :type image: PIL.Image.Image
        """
        assert(image.mode == self.mode)
        assert(image.size == self.size)

        image = self.preprocess(image)

        if self.framebuffer.redraw_required(image):
            left, top, right, bottom = self.framebuffer.bounding_box
            width = right - left
            height = bottom - top

            self.command(0x2A, left >> 8, left & 0xFF, (right - 1) >> 8, (right - 1) & 0xFF)     # Set column addr
            self.command(0x2B, top >> 8, top & 0xFF, (bottom - 1) >> 8, (bottom - 1) & 0xFF)     # Set row addr
            self.command(0x2C)                                                                   # Memory write

            i = 0
            buf = bytearray(width * height * 3)
            for r, g, b in self.framebuffer.getdata():
                if not(r == g == b == 0):
                    # 262K format
                    buf[i] = r
                    buf[i + 1] = g
                    buf[i + 2] = b
                i += 3

            self.data(list(buf))

    def contrast(self, level):
        """
        NOT SUPPORTED

        :param level: Desired contrast level in the range of 0-255.
        :type level: int
        """
        assert(0 <= level <= 255)
        pass

    def command(self, cmd, *args):
        """
        Sends a command and an (optional) sequence of arguments through to the
        delegated serial interface. Note that the arguments are passed through
        as data.
        """
        self._serial_interface.command(cmd)
        if len(args) > 0:
            self._serial_interface.data(list(args))


class backlight(object):
    """
    Controls a backlight (assumed to be on GPIO 18 (PWMCLK0))
    """
    def __init__(self, gpio=None, bcm_LIGHT=18):
        self._bcm_LIGHT = bcm_LIGHT
        self._gpio = gpio or self.__rpi_gpio__()
        self._gpio.setmode(self._gpio.BCM)
        self._gpio.setup(self._bcm_LIGHT, self._gpio.OUT)
        self.enable(True)

    def enable(self, value):
        """
        Switches on the backlight when ``True`` supplied, else ``False``
        switches it off
        """
        assert(value in [True, False])
        self._gpio.output(self._bcm_LIGHT,
                          self._gpio.LOW if value else self._gpio.HIGH)

    def __rpi_gpio__(self):
        # RPi.GPIO _really_ doesn't like being run on anything other than
        # a Raspberry Pi... this is imported here so we can swap out the
        # implementation for a mock
        import RPi.GPIO
        return RPi.GPIO
