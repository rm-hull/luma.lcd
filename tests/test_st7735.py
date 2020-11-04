#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.st7735` device.
"""

import pytest

from luma.lcd.device import st7735
from luma.core.render import canvas
from luma.core.framebuffer import full_frame

from baseline_data import get_reference_data, primitives
from helpers import serial, setup_function, assert_invalid_dimensions  # noqa: F401
from unittest.mock import Mock


def test_init_160x128():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    st7735(serial, gpio=Mock(), framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [1]},
        {'command': [17]},
        {'command': [177]}, {'data': [1, 44, 45]},
        {'command': [178]}, {'data': [1, 44, 45]},
        {'command': [179]}, {'data': [1, 44, 45, 1, 44, 45]},
        {'command': [180]}, {'data': [7]},
        {'command': [192]}, {'data': [162, 2, 132]},
        {'command': [193]}, {'data': [197]},
        {'command': [194]}, {'data': [10, 0]},
        {'command': [195]}, {'data': [138, 42]},
        {'command': [196]}, {'data': [138, 238]},
        {'command': [197]}, {'data': [14]},
        {'command': [54]}, {'data': [96]},
        {'command': [32]},
        {'command': [58]}, {'data': [6]},
        {'command': [19]},
        {'command': [224]}, {'data': [15, 26, 15, 24, 47, 40, 32, 34, 31, 27, 35, 55, 0, 7, 2, 16]},
        {'command': [225]}, {'data': [15, 27, 15, 23, 51, 44, 41, 46, 48, 48, 57, 63, 0, 7, 3, 16]},
        {'command': [42]}, {'data': [0, 0, 0, 159]},
        {'command': [43]}, {'data': [0, 0, 0, 127]},
        {'command': [44]}, {'data': [0] * (160 * 128 * 3)},
        {'command': [41]}
    ]


def test_init_128x128():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    st7735(serial, gpio=Mock(), width=128, height=128, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [1]},
        {'command': [17]},
        {'command': [177]}, {'data': [1, 44, 45]},
        {'command': [178]}, {'data': [1, 44, 45]},
        {'command': [179]}, {'data': [1, 44, 45, 1, 44, 45]},
        {'command': [180]}, {'data': [7]},
        {'command': [192]}, {'data': [162, 2, 132]},
        {'command': [193]}, {'data': [197]},
        {'command': [194]}, {'data': [10, 0]},
        {'command': [195]}, {'data': [138, 42]},
        {'command': [196]}, {'data': [138, 238]},
        {'command': [197]}, {'data': [14]},
        {'command': [54]}, {'data': [96]},
        {'command': [32]},
        {'command': [58]}, {'data': [6]},
        {'command': [19]},
        {'command': [224]}, {'data': [15, 26, 15, 24, 47, 40, 32, 34, 31, 27, 35, 55, 0, 7, 2, 16]},
        {'command': [225]}, {'data': [15, 27, 15, 23, 51, 44, 41, 46, 48, 48, 57, 63, 0, 7, 3, 16]},
        {'command': [42]}, {'data': [0, 0, 0, 127]},
        {'command': [43]}, {'data': [0, 0, 0, 127]},
        {'command': [44]}, {'data': [0] * (128 * 128 * 3)},
        {'command': [41]}
    ]


def test_init_160x80():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    st7735(serial, gpio=Mock(), width=160, height=80, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [1]},
        {'command': [17]},
        {'command': [177]}, {'data': [1, 44, 45]},
        {'command': [178]}, {'data': [1, 44, 45]},
        {'command': [179]}, {'data': [1, 44, 45, 1, 44, 45]},
        {'command': [180]}, {'data': [7]},
        {'command': [192]}, {'data': [162, 2, 132]},
        {'command': [193]}, {'data': [197]},
        {'command': [194]}, {'data': [10, 0]},
        {'command': [195]}, {'data': [138, 42]},
        {'command': [196]}, {'data': [138, 238]},
        {'command': [197]}, {'data': [14]},
        {'command': [54]}, {'data': [96]},
        {'command': [32]},
        {'command': [58]}, {'data': [6]},
        {'command': [19]},
        {'command': [224]}, {'data': [15, 26, 15, 24, 47, 40, 32, 34, 31, 27, 35, 55, 0, 7, 2, 16]},
        {'command': [225]}, {'data': [15, 27, 15, 23, 51, 44, 41, 46, 48, 48, 57, 63, 0, 7, 3, 16]},
        {'command': [42]}, {'data': [0, 0, 0, 159]},
        {'command': [43]}, {'data': [0, 0, 0, 79]},
        {'command': [44]}, {'data': [0] * (160 * 80 * 3)},
        {'command': [41]}
    ]


def test_init_invalid_dimensions():
    """
    ST7735 LCD with an invalid resolution raises a
    :py:class:`luma.core.error.DeviceDisplayModeError`.
    """
    assert_invalid_dimensions(st7735, serial, 128, 77)


def test_offsets():
    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command.side_effect = command
    serial.data.side_effect = data

    st7735(serial, gpio=Mock(), width=128, height=128, h_offset=2, v_offset=1, framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        {'command': [1]},
        {'command': [17]},
        {'command': [177]}, {'data': [1, 44, 45]},
        {'command': [178]}, {'data': [1, 44, 45]},
        {'command': [179]}, {'data': [1, 44, 45, 1, 44, 45]},
        {'command': [180]}, {'data': [7]},
        {'command': [192]}, {'data': [162, 2, 132]},
        {'command': [193]}, {'data': [197]},
        {'command': [194]}, {'data': [10, 0]},
        {'command': [195]}, {'data': [138, 42]},
        {'command': [196]}, {'data': [138, 238]},
        {'command': [197]}, {'data': [14]},
        {'command': [54]}, {'data': [96]},
        {'command': [32]},
        {'command': [58]}, {'data': [6]},
        {'command': [19]},
        {'command': [224]}, {'data': [15, 26, 15, 24, 47, 40, 32, 34, 31, 27, 35, 55, 0, 7, 2, 16]},
        {'command': [225]}, {'data': [15, 27, 15, 23, 51, 44, 41, 46, 48, 48, 57, 63, 0, 7, 3, 16]},
        {'command': [42]}, {'data': [0, 2, 0, 129]},
        {'command': [43]}, {'data': [0, 1, 0, 128]},
        {'command': [44]}, {'data': [0] * (128 * 128 * 3)},
        {'command': [41]}
    ]


def test_contrast():
    device = st7735(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_hide():
    device = st7735(serial, gpio=Mock())
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(40)


def test_show():
    device = st7735(serial, gpio=Mock())
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(41)


def test_display():
    device = st7735(serial, gpio=Mock(), framebuffer=full_frame())
    serial.reset_mock()

    recordings = []

    def data(data):
        recordings.append({'data': data})

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
    # save_reference_data("demo_st7735", recordings)

    assert recordings == get_reference_data('demo_st7735')
