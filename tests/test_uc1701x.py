#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.uc1701x` device.
"""

from luma.lcd.device import uc1701x
from luma.core.render import canvas

from baseline_data import get_reference_data, primitives
from helpers import serial
from unittest.mock import Mock, call


def test_init_128x64():
    """
    UC1701X LCD with a 128 x 64 resolution works correctly.
    """
    uc1701x(serial, gpio=Mock())
    serial.command.assert_has_calls([
        # Initial burst are initialization commands
        call(226),
        call(44),
        call(46),
        call(47),
        call(248, 0),
        call(35),
        call(162),
        call(192),
        call(161),
        call(172),
        call(166),
        call(165),
        call(164),
        # set contrast
        call(129, 44),
        # reset the display
        call(176, 4, 16),
        call(177, 4, 16),
        call(178, 4, 16),
        call(179, 4, 16),
        call(180, 4, 16),
        call(181, 4, 16),
        call(182, 4, 16),
        call(183, 4, 16),
        call(175)])

    # Next 1024 are all data: zero's to clear the RAM
    # (1024 = 128 * 64 / 8)
    serial.data.assert_has_calls([call([0] * 128)] * 8)


def test_display():
    """
    UC1701X LCD screen can draw and display an image.
    """
    device = uc1701x(serial, gpio=Mock())
    serial.reset_mock()

    recordings = []

    def data(data):
        recordings.append({'data': data})

    def command(*cmd):
        recordings.append({'command': list(cmd)})

    serial.command = Mock(side_effect=command, unsafe=True)
    serial.data = Mock(side_effect=data, unsafe=True)

    # Use the same drawing primitives as the demo
    with canvas(device) as draw:
        primitives(device, draw)

    serial.data.assert_called()
    serial.command.assert_called()

    # To regenerate test data, uncomment the following (remember not to commit though)
    # ================================================================================
    # from baseline_data import save_reference_data
    # save_reference_data("demo_uc1701x", recordings)

    assert recordings == get_reference_data('demo_uc1701x')
