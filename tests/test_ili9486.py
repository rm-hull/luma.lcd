#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.ili9486` device.
"""

import pytest

from luma.lcd.device import ili9486
from luma.core.render import canvas
from luma.core.framebuffer import full_frame

from baseline_data import get_reference_data, primitives
from helpers import serial, setup_function, assert_invalid_dimensions  # noqa: F401
from unittest.mock import Mock


def test_init_320x480():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9486(serial, gpio=Mock(), framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    # This set of expected results include the padding bytes that
    # appear necessary with Waveshare's ili9486 implementation.
    assert recordings == [
        {'command': [0xb0]}, {'data': [0x00, 0x00]},
        {'command': [0x11]},
        {'command': [0x3a]}, {'data': [0x00, 0x66]},
        {'command': [0x21]},
        {'command': [0xc0]}, {'data': [0x00, 0x09, 0x00, 0x09]},
        {'command': [0xc1]}, {'data': [0x00, 0x41, 0x00, 0x00]},
        {'command': [0xc2]}, {'data': [0x00, 0x33]},
        {'command': [0xc5]}, {'data': [0x00, 0x00, 0x00, 0x36]},
        {'command': [0x36]}, {'data': [0x00, 0x08]},
        {'command': [0xb6]}, {'data': [0x00, 0x00, 0x00, 0x42, 0x00, 0x3b]},
        {'command': [0x13]},
        {'command': [0x34]},
        {'command': [0x38]},
        {'command': [0x11]},
        {'command': [0x2a]}, {'data': [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x3f]},
        {'command': [0x2b]}, {'data': [0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0xdf]},
        {'command': [0x2c]},
        {'data': bytearray([0x00] * (320 * 480 * 3))},
        {'command': [0x29]},
    ]


def test_init_invalid_dimensions():
    """
    ILI9486 LCD with an invalid resolution raises a
    :py:class:`luma.core.error.DeviceDisplayModeError`.
    """
    assert_invalid_dimensions(ili9486, serial, 128, 77)


def test_offsets():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    ili9486(serial, gpio=Mock(), width=320, height=480, h_offset=2, v_offset=1, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [0xb0]}, {'data': [0x00, 0x00]},
        {'command': [0x11]},
        {'command': [0x3a]}, {'data': [0x00, 0x66]},
        {'command': [0x21]},
        {'command': [0xc0]}, {'data': [0x00, 0x09, 0x00, 0x09]},
        {'command': [0xc1]}, {'data': [0x00, 0x41, 0x00, 0x00]},
        {'command': [0xc2]}, {'data': [0x00, 0x33]},
        {'command': [0xc5]}, {'data': [0x00, 0x00, 0x00, 0x36]},
        {'command': [0x36]}, {'data': [0x00, 0x08]},
        {'command': [0xb6]}, {'data': [0x00, 0x00, 0x00, 0x42, 0x00, 0x3b]},
        {'command': [0x13]},
        {'command': [0x34]},
        {'command': [0x38]},
        {'command': [0x11]},
        {'command': [0x2A]}, {'data': [0x00, 0x00, 0x00, 0x02, 0x00, 0x01, 0x00, 0x3f + 0x02]},
        {'command': [0x2B]}, {'data': [0x00, 0x00, 0x00, 0x01, 0x00, 0x01, 0x00, 0xdf + 0x01]},
        {'command': [0x2C]},
        {'data': bytearray([0x00] * (320 * 480 * 3))},
        {'command': [0x29]},
    ]


def test_contrast():
    device = ili9486(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_hide():
    device = ili9486(serial, gpio=Mock())
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(40)


def test_show():
    device = ili9486(serial, gpio=Mock())
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(41)


def test_display_full_frame():
    device = ili9486(serial, gpio=Mock(), framebuffer=full_frame())
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
    # save_reference_data("demo_ili9486", recordings)

    assert recordings == get_reference_data('demo_ili9486')
