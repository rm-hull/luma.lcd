#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2023 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.ili9488` device.
"""

import pytest

from luma.lcd.device import ili9488
from luma.core.render import canvas
from luma.core.framebuffer import full_frame

from baseline_data import get_reference_data, primitives
from helpers import serial, setup_function, assert_invalid_dimensions  # noqa: F401
from unittest.mock import Mock


def test_init_480x320():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9488(serial, gpio=Mock(), framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xe0]}, {'data': [0x00, 0x03, 0x09, 0x08, 0x16, 0x0a, 0x37, 0x78, 0x4c, 0x09, 0x0a, 0x08, 0x16, 0x1a, 0x0f]},
        {'command': [0xe1]}, {'data': [0x00, 0x16, 0x19, 0x03, 0x0f, 0x05, 0x32, 0x45, 0x46, 0x04, 0x0e, 0x0d, 0x35, 0x37, 0x0f]},
        {'command': [0xc0]}, {'data': [0x17, 0x15]},
        {'command': [0xc1]}, {'data': [0x41]},
        {'command': [0xc5]}, {'data': [0x00, 0x12, 0x80]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x66]},
        {'command': [0xb0]}, {'data': [0x00]},
        {'command': [0xb1]}, {'data': [0xa0]},
        {'command': [0xb4]}, {'data': [0x02]},
        {'command': [0xb6]}, {'data': [0x02, 0x02, 0x3b]},
        {'command': [0xb7]}, {'data': [0xc6]},
        {'command': [0xf7]}, {'data': [0xa9, 0x51, 0x2c, 0x82]},
        {'command': [0x11]},
        {'command': [0x2a]}, {'data': [0x00, 0x00, 0x01, 0xdf]},
        {'command': [0x2b]}, {'data': [0x00, 0x00, 0x01, 0x3f]},
        {'command': [0x2c]},
        {'data': bytearray([0x00] * (480 * 320 * 3))},
        {'command': [0x29]},
    ]


def test_init_invalid_dimensions():
    """
    ILI9488 LCD with an invalid resolution raises a
    :py:class:`luma.core.error.DeviceDisplayModeError`.
    """
    assert_invalid_dimensions(ili9488, serial, 128, 77)


def test_offsets():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9488(serial, gpio=Mock(), width=480, height=320, h_offset=2, v_offset=1, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xe0]}, {'data': [0x00, 0x03, 0x09, 0x08, 0x16, 0x0a, 0x37, 0x78, 0x4c, 0x09, 0x0a, 0x08, 0x16, 0x1a, 0x0f]},
        {'command': [0xe1]}, {'data': [0x00, 0x16, 0x19, 0x03, 0x0f, 0x05, 0x32, 0x45, 0x46, 0x04, 0x0e, 0x0d, 0x35, 0x37, 0x0f]},
        {'command': [0xc0]}, {'data': [0x17, 0x15]},
        {'command': [0xc1]}, {'data': [0x41]},
        {'command': [0xc5]}, {'data': [0x00, 0x12, 0x80]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x66]},
        {'command': [0xb0]}, {'data': [0x00]},
        {'command': [0xb1]}, {'data': [0xa0]},
        {'command': [0xb4]}, {'data': [0x02]},
        {'command': [0xb6]}, {'data': [0x02, 0x02, 0x3b]},
        {'command': [0xb7]}, {'data': [0xc6]},
        {'command': [0xf7]}, {'data': [0xa9, 0x51, 0x2c, 0x82]},
        {'command': [0x11]},
        {'command': [0x2a]}, {'data': [0x00, 0x02, 0x01, 0xdf + 0x02]},
        {'command': [0x2b]}, {'data': [0x00, 0x01, 0x01, 0x3f + 0x01]},
        {'command': [0x2c]},
        {'data': bytearray([0x00] * (480 * 320 * 3))},
        {'command': [0x29]},
    ]


def test_contrast():
    device = ili9488(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_hide():
    device = ili9488(serial, gpio=Mock())
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(40)


def test_show():
    device = ili9488(serial, gpio=Mock())
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(41)


def test_display_full_frame():
    device = ili9488(serial, gpio=Mock(), framebuffer=full_frame())
    serial.reset_mock()

    recordings = []

    def data(data):
        recordings.append({'data': list(data)})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    # Use the same drawing primitives as the demo
    with canvas(device) as draw:
        primitives(device, draw)

    assert serial.data.called
    assert serial.command.called

    # To regenerate test data, uncomment the following (remember not to commit though)
    # ================================================================================
    # from baseline_data import save_reference_data
    # save_reference_data("demo_ili9488", recordings)

    assert recordings == get_reference_data('demo_ili9488')
