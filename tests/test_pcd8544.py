#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

try:
    from unittest.mock import call, Mock
except ImportError:
    from mock import call, Mock

import pytest
import luma.core.error
from luma.lcd.device import pcd8544
from luma.core.render import canvas
import baseline_data

serial = Mock(unsafe=True)


def setup_function(function):
    serial.reset_mock()
    serial.command.side_effect = None


def test_init_84x48():
    pcd8544(serial)
    serial.command.assert_has_calls([
        # Initial burst are initialization commands
        call(174, 213, 128, 168, 63, 211, 0, 64, 141, 20, 32, 0,
             160, 200, 218, 18, 217, 241, 219, 64, 164, 166),
        # set contrast
        call(129, 207),
        # reset the display
        call(33, 0, 127, 34, 0, 7),
        # called last, is a command to show the screen
        call(175)
    ])

    # Next 1024 are all data: zero's to clear the RAM
    # (1024 = 128 * 64 / 8)
    serial.data.assert_called_once_with([0] * (128 * 64 // 8))


def test_init_invalid_dimensions():
    with pytest.raises(luma.core.error.DeviceDisplayModeError) as ex:
        pcd8544(serial, width=59, height=22)
    assert "Unsupported display mode: 59 x 22" in str(ex.value)


def test_hide():
    device = pcd8544(serial)
    serial.reset_mock()
    device.hide()
    serial.command.assert_called_once_with(174)


def test_show():
    device = pcd8544(serial)
    serial.reset_mock()
    device.show()
    serial.command.assert_called_once_with(175)


def test_display():
    device = pcd8544(serial)
    serial.reset_mock()

    # Use the same drawing primitives as the demo
    with canvas(device) as draw:
        baseline_data.primitives(device, draw)

    # Initial command to reset the display
    serial.command.assert_called_once_with(33, 0, 127, 34, 0, 7)

    # Next 1024 bytes are data representing the drawn image
    serial.data.assert_called_once_with(baseline_data.demo_pcd8544)
