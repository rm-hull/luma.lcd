# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

# Example usage:
#
#   from luma.core.serial import spi
#   from luma.core.render import canvas
#   from luma.lcd.device import pcd8544
#   from PIL import ImageDraw
#
#   serial = spi(device=0, bus=0)
#   device = ssd1306(serial)
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
import luma.lcd.const


class pcd8544(device):
    """
    Encapsulates the serial interface to the monochrome PCD8544 LCD display
    hardware. On creation, an initialization sequence is pumped to the display
    to properly configure it. Further control commands can then be called to
    affect the brightness and other settings.
    """
    def __init__(self, serial_interface=None, width=84, height=48, rotate=0):
        super(pcd8544, self).__init__(luma.lcd.const.pcd8544, serial_interface)
        self.capabilities(width, height, rotate)
        self._buffer = [0] * self._w * self._h

        if width != 84 or height != 48:
            raise luma.core.error.DeviceDisplayModeError(
                "Unsupported display mode: {0} x {1}".format(width, height))

        self.command(0x20)  # Horizontal write mode
        self.contrast(0x7F)
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

        buf = self._buffer
        for idx, pix in enumerate(image.getdata()):
            buf[idx] = 1 if pix > 0 else 0

        self.data(buf)

    def contrast(self, value):
        """
        Sets the LCD contrast
        """
        assert(0 <= value <= 255)

        self.command(0x21, 0x14, value, 0x20, 0x0c)
