#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.st7567` device.
"""

import pytest

from luma.lcd.device import st7567
from luma.core.render import canvas

from baseline_data import get_reference_data, primitives
from helpers import serial, setup_function, assert_invalid_dimensions  # noqa: F401
from unittest.mock import Mock, call


def test_init_128x64():
    st7567(serial, gpio=Mock())
    serial.command.assert_has_calls([
        call(0xA3),
        call(0xA1),
        call(0xC0),
        call(0xA6),
        call(0x40),
        call(0x2F),
        call(0x22),
        call(0xAF),
        call(0x81, 57)
    ])

    # Next 1024 are all data: zeros to clear the RAM
    # (1024 = 128 * 64 / 8)
    serial.data.assert_has_calls([call([0] * 128)] * 8)


def test_contrast():
    device = st7567(serial, gpio=Mock())
    serial.reset_mock()
    with pytest.raises(AssertionError):
        device.contrast(300)


def test_display():
    device = st7567(serial, gpio=Mock())
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
    # save_reference_data("demo_st7567", recordings)

    assert recordings == get_reference_data('demo_st7567')
