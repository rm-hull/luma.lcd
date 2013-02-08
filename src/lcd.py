#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wiringPy
import time
import struct

from PIL import Image
from pcd8544.font import default_FONT
from pcd8544.util import flatten

# screen size in pixel
HEIGHT = WIDTH = 84

fd = -1 # FIXME bitbang file descriptor

# default PINs, BCM GPIO
pin_CLK   = 11
pin_DIN   = 10
pin_DC    = 23
pin_RST   = 24
pin_LIGHT = 18
pin_CE    = 8

# useful constants
ON,   OFF = [1, 0]
HIGH, LOW = [1, 0]

# contrast
default_contrast = 0xB0

def init(CLK = 11, DIN = 10, DC = 23, RST = 24, LIGHT = 18, CE = 8, contrast = default_contrast):
    """ init screen, clearscreen """
    wiringPy.debug(0)

    if wiringPy.setup_gpio() != 0:
        raise IOError("Failed to initialize wiringPy properly")

    fd = wiringPy.setup_bitbang(CE, DIN, CLK, 0)
    if fd == -1:
        raise IOError("Failed to initialize bitbang properly")

    pins = [CLK, DIN, DC, RST, LIGHT, CE]
    pin_CLK, pin_DIN, pin_DC, pin_RST, pin_LIGHT, pin_CE = pins
    map(lambda p: wiringPy.pin_mode(p, ON), pins)

    # Reset the device
    wiringPy.digital_write(pin_RST, OFF)
    time.sleep(0.1)
    wiringPy.digital_write(pin_RST, ON)
    set_contrast(contrast)
    cls()

def set_contrast(value):
    """ sets the LCD contrast """
    command([0x21, 0x14, value, 0x20, 0x0c])

def backlight(status):
    """ control backlight """
    wiringPy.digital_write(pin_LIGHT, 1 - status)

def command(arr):
    """ write commands """
    bitmap(arr, OFF)

def data(arr):
    """ write data """
    bitmap(arr, ON)

def bitmap(arr, dc):
    """ write a sequence of bytes, either as data or command"""
    wiringPy.digital_write(pin_DC, dc)
    wiringPy.digital_write_serial_array(0, struct.pack('B'*len(arr), *arr))

def position(x, y):
    """ goto to column x in seg y """
    command([x + 0x80, y + 0x40])

def cls():
    """ clear screen """
    position(0, 0)
    data([0] * (HEIGHT * WIDTH / 8))
    position(0, 0)

def locate(x, y):
    """ goto (x,y) to paint a character """
    position(x * 6, y)

def text(string, font = default_FONT, align = 'left'):
    """ draw string at current position """
    map(lambda c: data(font[c] + [0x00]), string)

def smooth_hscroll(string, row, iterations, delay=0.2, font=default_FONT):
    """ scrolls string at given row """
    bytes = list(flatten(map(lambda c: font[c] + [0x00], string)))
    for i in xrange(iterations):
        position(0, row)
        data(bytes[i:i+84])
        time.sleep(delay)

def bit_reverse(value, width=8):
  result = 0
  for _ in xrange(width):
    result = (result << 1) | (value & 1)
    value >>= 1

  return result

BITREVERSE = map(bit_reverse, xrange(256))

def image(im, reverse=False):
    """ draw image """
    mask = 0xFF if reverse else 0x00
    # Rotate and mirror the image
    rim = im.rotate(-90).transpose(Image.FLIP_LEFT_RIGHT)
    command([0x22])  # Change display to vertical write mode for graphics
    position(0, 0)
    data([BITREVERSE[ord(x)] ^ mask for x in list(rim.tostring())])
    command([0x20])  # Switch back to horizontal write mode for text
