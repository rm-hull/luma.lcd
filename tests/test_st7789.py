#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2021 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.st7789` device.
"""
import pytest

from luma.lcd.device import st7789
from luma.core.render import canvas
from luma.core.framebuffer import full_frame

from baseline_data import get_reference_data, primitives
from helpers import serial
from unittest.mock import Mock


def test_init_240x240():
    recordings = []

    def data(data):
        recordings.extend(data)

    def command(*cmd):
        recordings.extend(['command', list(cmd)[0], 'data', *list(cmd)[1:]])

    serial.command.side_effect = command
    serial.data.side_effect = data

    st7789(serial, gpio=Mock(), framebuffer=full_frame())

    assert serial.data.called
    assert serial.command.called

    assert recordings == [
        'command', 54, 'data', 112,
        'command', 58, 'data', 6,
        'command', 178, 'data', 12, 12, 0, 51, 51,
        'command', 183, 'data', 53,
        'command', 187, 'data', 25,
        'command', 192, 'data', 44,
        'command', 194, 'data', 1,
        'command', 195, 'data', 18,
        'command', 196, 'data', 32,
        'command', 198, 'data', 15,
        'command', 208, 'data', 164, 161,
        'command', 224, 'data', 208, 4, 13, 17, 19, 43, 63, 84, 76, 24, 13, 11, 31, 35,
        'command', 225, 'data', 208, 4, 12, 17, 19, 44, 63, 68, 81, 47, 31, 31, 32, 35,
        'command', 33, 'data',
        'command', 17, 'data',
        'command', 41, 'data',
        'command', 42, 'data', 0, 0, 0, 239,
        'command', 43, 'data', 0, 0, 0, 239,
        'command', 44, 'data', *([0] * (240 * 240 * 3)),
        'command', 41, 'data'
    ]


def test_contrast():
    device = st7789(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_hide():
    device = st7789(serial, gpio=Mock())
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(40)


def test_show():
    device = st7789(serial, gpio=Mock())
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(41)


def test_display():
    device = st7789(serial, gpio=Mock(), framebuffer=full_frame())
    serial.reset_mock()

    recordings = []

    def data(data):
        recordings.extend(data)

    def command(*cmd):
        recordings.extend(['command', list(cmd)[0], 'data', *list(cmd)[1:]])

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
    # save_reference_data("demo_st7789", recordings)

    assert recordings == get_reference_data('demo_st7789')
