#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.hd44780` device.
"""

from luma.lcd.device import hd44780
from luma.core.render import canvas
from luma.core.util import bytes_to_nibbles

from PIL import Image, ImageDraw
from unittest.mock import Mock, call

CLEAR = 0x01
HOME = 0x02
ENTRY = 0x06
DISPLAYOFF = 0x08
DISPLAYON = 0x0C
FUNCTIONSET = 0x20
DL8 = 0x10
DL4 = 0x00
LINES2 = 0x08
LINES1 = 0x00
CHAR5x8 = 0x00
CHAR5x10 = 0x04
DL8 = 0x10
DL4 = 0x00
DDRAMADDR = 0x80
CGRAMADDR = 0x40
LINES = [00, 0x40, 0x14, 0x54]

serial = Mock(unsafe=True, _bitmode=4)


def test_init_4bitmode():
    """
    Test initialization of display using 4 bit mode
    """
    hd44780(serial)

    to_8 = \
        [call(0x3), call(0x3), call(0x3, 0x3)] * 3
    to_4 = \
        [call(0x3), call(0x3), call(0x3, 0x02)]

    fs = [FUNCTIONSET | DL4 | LINES2]

    calls = \
        to_8 + \
        to_4 + \
        [call(*bytes_to_nibbles(fs))] + \
        [call(*bytes_to_nibbles([DISPLAYOFF]))] + \
        [call(*bytes_to_nibbles([ENTRY]))] + \
        [call(*bytes_to_nibbles([DISPLAYON]))] + \
        [call(*bytes_to_nibbles([DDRAMADDR]))] + \
        [call(*bytes_to_nibbles([DDRAMADDR | LINES[1]]))] + \
        [call(*bytes_to_nibbles([CLEAR]))]

    serial.command.assert_has_calls(calls)

    # Data to clear the screen
    calls = \
        [call(bytes_to_nibbles([0x20] * 16))] + \
        [call(bytes_to_nibbles([0x20] * 16))]

    serial.data.assert_has_calls(calls)


def test_init_8bitmode():
    """
    Test initialization of display using 4 bit mode
    """
    serial._bitmode = 8
    hd44780(serial)

    to_8 = \
        [call(0x30)] * 3

    fs = [FUNCTIONSET | DL8 | LINES2]

    calls = \
        to_8 + \
        [call(*fs)] + \
        [call(*[DISPLAYOFF])] + \
        [call(*[ENTRY])] + \
        [call(*[DISPLAYON])] + \
        [call(*[DDRAMADDR])] + \
        [call(*[DDRAMADDR | LINES[1]])] + \
        [call(*[CLEAR])]

    serial.command.assert_has_calls(calls)

    # Data to clear the screen
    calls = \
        [call([0x20] * 16)] + \
        [call([0x20] * 16)]

    serial.data.assert_has_calls(calls)


def test_display():
    """
    Test the display of a line of text containing and a rectangle to verify
    auto-create feature
    """
    device = hd44780(serial, bitmode=8)
    serial.reset_mock()

    # Use canvas to create a screen worth of data
    with canvas(device) as drw:
        # Include unprintable character to show it gets ignored
        size = device.font.getsize('This is a test\uFFFF')
        drw.text(((80 - size[0]) // 2, 0), 'This is a test\uFFFF', font=device.font, fill='white')
        drw.rectangle((10, 10, 69, 14), fill='black', outline='white')
        drw.rectangle((10, 10, 49, 14), fill='white', outline='white')

    # Send DDRAMADDR and ascii for the line of text
    line1 = [call.command(0x81)] + \
        [call.data([0x54, 0x68, 0x69, 0x73, 0x20, 0x69, 0x73, 0x20, 0x61, 0x20, 0x74, 0x65, 0x73, 0x74])]

    # Create custom characters for the scrollbar
    custom = [call.command(0x40), call.data([0x00, 0x00, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x00])] + \
        [call.command(0x48), call.data([0x00, 0x00, 0x1f, 0x00, 0x00, 0x00, 0x1f, 0x00])] + \
        [call.command(0x50), call.data([0x00, 0x00, 0x1f, 0x01, 0x01, 0x01, 0x1f, 0x00])]

    # Print the resulting custom characters to form the image of the scrollbar
    line2 = [call.command(0xc1), call.data([0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x01, 0x01, 0x02, 0x20])]

    serial.assert_has_calls(line1 + custom + line2)


def test_custom_full():
    """
    Test of behavior when auto-create feature runs out of custom character
    space
    """
    device = hd44780(serial, bitmode=8)

    # Consume 8 special character positions
    img = Image.new('1', (80, 16), 0)
    drw = ImageDraw.Draw(img)
    for i in range(8):
        drw.rectangle((i * 5, 0, (i + 1) * 5, i), fill='white', outline='white')
    device.display(img)

    serial.reset_mock()

    # Consume one more (on the last char position on screen)
    drw.line((75, 8, 79, 15), fill='white')
    device.display(img)

    serial.assert_has_calls([call.command(0xcf), call.data([0x5f])])


def test_get_font():
    """
    Verify get font capability by requesting two fonts and printing a single
    character from each that will be different between the two fonts
    """
    device = hd44780(serial, bitmode=8)

    img = Image.new('1', (10, 8), 0)
    a00 = device.get_font(0)
    a02 = device.get_font(1)
    drw = ImageDraw.Draw(img)

    assert a00.getsize('\u00E0') == (5, 8)

    drw.text((0, 0), '\u00E0', font=a00, fill='white')
    drw.text((5, 0), '\u00E0', font=a02, fill='white')

    assert img.tobytes() == \
        b'\x02\x00\x01\x00H\x00\xab\x80\x90@\x93\xc0l@\x03\xc0'


def test_unsupported_display_mode():
    """
    Verify exception is thrown if an unsupported display mode is requested
    """
    import luma.core
    try:
        hd44780(serial, width=12, height=3)
    except luma.core.error.DeviceDisplayModeError as ex:
        assert str(ex) == "Unsupported display mode: 12 x 3"
