#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-19 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.ili9341` device.
"""

import pytest

from luma.lcd.device import ili9341
from luma.core.render import canvas
from luma.core.framebuffer import full_frame

from baseline_data import get_reference_data, primitives
from helpers import serial, setup_function, assert_invalid_dimensions  # noqa: F401
from unittest.mock import Mock


def test_init_320x240():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9341(serial, gpio=Mock(), framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xef]}, {'data': [0x03, 0x80, 0x02]},
        {'command': [0xcf]}, {'data': [0x00, 0xc1, 0x30]},
        {'command': [0xed]}, {'data': [0x64, 0x03, 0x12, 0x81]},
        {'command': [0xe8]}, {'data': [0x85, 0x00, 0x78]},
        {'command': [0xcb]}, {'data': [0x39, 0x2c, 0x00, 0x34, 0x02]},
        {'command': [0xf7]}, {'data': [0x20]},
        {'command': [0xea]}, {'data': [0x00, 0x00]},
        {'command': [0xc0]}, {'data': [0x23]},
        {'command': [0xc1]}, {'data': [0x10]},
        {'command': [0xc5]}, {'data': [0x3e, 0x28]},
        {'command': [0xc7]}, {'data': [0x86]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x46]},
        {'command': [0xb1]}, {'data': [0x00, 0x18]},
        {'command': [0xb6]}, {'data': [0x08, 0x82, 0x27]},
        {'command': [0xf2]}, {'data': [0x00]},
        {'command': [0x26]}, {'data': [0x01]},
        {'command': [0xe0]}, {'data': [0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1, 0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00]},
        {'command': [0xe1]}, {'data': [0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1, 0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f]},
        {'command': [0x11]},
        {'command': [0x2a]}, {'data': [0x00, 0x00, 0x01, 0x3f]},
        {'command': [0x2b]}, {'data': [0x00, 0x00, 0x00, 0xef]},
        {'command': [0x2c]},
        {'data': bytearray([0x00] * (320 * 240 * 3))},
        {'command': [0x29]},
    ]


def test_init_240x240():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9341(serial, gpio=Mock(), width=240, height=240, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xef]}, {'data': [0x03, 0x80, 0x02]},
        {'command': [0xcf]}, {'data': [0x00, 0xc1, 0x30]},
        {'command': [0xed]}, {'data': [0x64, 0x03, 0x12, 0x81]},
        {'command': [0xe8]}, {'data': [0x85, 0x00, 0x78]},
        {'command': [0xcb]}, {'data': [0x39, 0x2c, 0x00, 0x34, 0x02]},
        {'command': [0xf7]}, {'data': [0x20]},
        {'command': [0xea]}, {'data': [0x00, 0x00]},
        {'command': [0xc0]}, {'data': [0x23]},
        {'command': [0xc1]}, {'data': [0x10]},
        {'command': [0xc5]}, {'data': [0x3e, 0x28]},
        {'command': [0xc7]}, {'data': [0x86]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x46]},
        {'command': [0xb1]}, {'data': [0x00, 0x18]},
        {'command': [0xb6]}, {'data': [0x08, 0x82, 0x27]},
        {'command': [0xf2]}, {'data': [0x00]},
        {'command': [0x26]}, {'data': [0x01]},
        {'command': [0xe0]}, {'data': [0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1, 0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00]},
        {'command': [0xe1]}, {'data': [0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1, 0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f]},
        {'command': [0x11]},
        {'command': [0x2A]}, {'data': [0x00, 0x00, 0x00, 0xef]},
        {'command': [0x2B]}, {'data': [0x00, 0x00, 0x00, 0xef]},
        {'command': [0x2C]},
        {'data': bytearray([0x00] * (240 * 240 * 3))},
        {'command': [0x29]},
    ]


def test_init_320x180():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9341(serial, gpio=Mock(), width=320, height=180, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xef]}, {'data': [0x03, 0x80, 0x02]},
        {'command': [0xcf]}, {'data': [0x00, 0xc1, 0x30]},
        {'command': [0xed]}, {'data': [0x64, 0x03, 0x12, 0x81]},
        {'command': [0xe8]}, {'data': [0x85, 0x00, 0x78]},
        {'command': [0xcb]}, {'data': [0x39, 0x2c, 0x00, 0x34, 0x02]},
        {'command': [0xf7]}, {'data': [0x20]},
        {'command': [0xea]}, {'data': [0x00, 0x00]},
        {'command': [0xc0]}, {'data': [0x23]},
        {'command': [0xc1]}, {'data': [0x10]},
        {'command': [0xc5]}, {'data': [0x3e, 0x28]},
        {'command': [0xc7]}, {'data': [0x86]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x46]},
        {'command': [0xb1]}, {'data': [0x00, 0x18]},
        {'command': [0xb6]}, {'data': [0x08, 0x82, 0x27]},
        {'command': [0xf2]}, {'data': [0x00]},
        {'command': [0x26]}, {'data': [0x01]},
        {'command': [0xe0]}, {'data': [0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1, 0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00]},
        {'command': [0xe1]}, {'data': [0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1, 0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f]},
        {'command': [0x11]},
        {'command': [0x2A]}, {'data': [0x00, 0x00, 0x01, 0x3f]},
        {'command': [0x2B]}, {'data': [0x00, 0x00, 0x00, 0xb3]},
        {'command': [0x2C]},
        {'data': bytearray([0x00] * (320 * 180 * 3))},
        {'command': [0x29]},
    ]


def test_init_invalid_dimensions():
    """
    ILI9341 LCD with an invalid resolution raises a
    :py:class:`luma.core.error.DeviceDisplayModeError`.
    """
    assert_invalid_dimensions(ili9341, serial, 128, 77)


def test_offsets():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9341(serial, gpio=Mock(), width=240, height=240, h_offset=2, v_offset=1, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xef]}, {'data': [0x03, 0x80, 0x02]},
        {'command': [0xcf]}, {'data': [0x00, 0xc1, 0x30]},
        {'command': [0xed]}, {'data': [0x64, 0x03, 0x12, 0x81]},
        {'command': [0xe8]}, {'data': [0x85, 0x00, 0x78]},
        {'command': [0xcb]}, {'data': [0x39, 0x2c, 0x00, 0x34, 0x02]},
        {'command': [0xf7]}, {'data': [0x20]},
        {'command': [0xea]}, {'data': [0x00, 0x00]},
        {'command': [0xc0]}, {'data': [0x23]},
        {'command': [0xc1]}, {'data': [0x10]},
        {'command': [0xc5]}, {'data': [0x3e, 0x28]},
        {'command': [0xc7]}, {'data': [0x86]},
        {'command': [0x36]}, {'data': [0x28]},
        {'command': [0x3a]}, {'data': [0x46]},
        {'command': [0xb1]}, {'data': [0x00, 0x18]},
        {'command': [0xb6]}, {'data': [0x08, 0x82, 0x27]},
        {'command': [0xf2]}, {'data': [0x00]},
        {'command': [0x26]}, {'data': [0x01]},
        {'command': [0xe0]}, {'data': [0x0f, 0x31, 0x2b, 0x0c, 0x0e, 0x08, 0x4e, 0xf1, 0x37, 0x07, 0x10, 0x03, 0x0e, 0x09, 0x00]},
        {'command': [0xe1]}, {'data': [0x00, 0x0e, 0x14, 0x03, 0x11, 0x07, 0x31, 0xc1, 0x48, 0x08, 0x0f, 0x0c, 0x31, 0x36, 0x0f]},
        {'command': [0x11]},
        {'command': [0x2A]}, {'data': [0x00, 0x02, 0x00, 0xef + 0x02]},
        {'command': [0x2B]}, {'data': [0x00, 0x01, 0x00, 0xef + 0x01]},
        {'command': [0x2C]},
        {'data': bytearray([0x00] * (240 * 240 * 3))},
        {'command': [0x29]},
    ]


def test_contrast():
    device = ili9341(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_hide():
    device = ili9341(serial, gpio=Mock())
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(40)


def test_show():
    device = ili9341(serial, gpio=Mock())
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(41)


def test_display_full_frame():
    device = ili9341(serial, gpio=Mock(), framebuffer=full_frame())
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
    # save_reference_data("demo_ili9341", recordings)

    assert recordings == get_reference_data('demo_ili9341')
