#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-18 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.ht1621` device.
"""

from luma.lcd.device import ht1621
from luma.core.virtual import sevensegment

from helpers import call, Mock  # noqa: F401

gpio = Mock(unsafe=True)


def setup_function(function):
    """
    Called before a test runs.
    """
    gpio.reset_mock()
    gpio.command.side_effect = None
    gpio.OUT = 23
    gpio.HIGH = 7
    gpio.LOW = 4


def test_init_6x8():
    ht1621(gpio, WR=99, DAT=88, CS=77)
    gpio.setup.assert_has_calls([
        call(99, 23),
        call(88, 23),
        call(77, 23)
    ])

    gpio.output.assert_has_calls([
        call(77, 4), call(99, 4), call(88, 7), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 7), call(99, 7), call(99, 4), call(88, 7), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(77, 7), call(77, 4), call(99, 4),
        call(88, 7), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 7), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 7), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 7), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(77, 7), call(77, 4), call(99, 4), call(88, 7), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 7), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(77, 7), call(77, 4),
        call(99, 4), call(88, 7), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 7), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(77, 7), call(77, 4), call(99, 4), call(88, 7),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 4), call(99, 7), call(99, 4), call(88, 4),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(99, 4),
        call(88, 4), call(99, 7), call(99, 4), call(88, 4), call(99, 7),
        call(99, 4), call(88, 7), call(99, 7), call(99, 4), call(88, 7),
        call(99, 7), call(99, 4), call(88, 4), call(99, 7), call(77, 7)
    ])


def test_hide():
    device = ht1621(gpio)
    gpio.reset_mock()
    device.hide()
    gpio.output.assert_has_calls([
        call(8, 4), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 7),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(8, 7)
    ])


def test_show():
    device = ht1621(gpio)
    gpio.reset_mock()
    device.show()
    gpio.output.assert_has_calls([
        call(8, 4), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 7),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(8, 7)
    ])


def test_display():
    device = ht1621(gpio)
    gpio.reset_mock()

    sevensegment(device).text = "HELLO"
    gpio.output.assert_has_calls([
        call(8, 4), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 7), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(8, 7), call(8, 4), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 7), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 7),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 7), call(11, 7),
        call(11, 4), call(10, 7), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 7), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 4), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 7), call(11, 7), call(11, 4), call(10, 7),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 4), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 7), call(11, 7),
        call(11, 4), call(10, 7), call(11, 7), call(11, 4), call(10, 7),
        call(11, 7), call(11, 4), call(10, 4), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 7), call(11, 7),
        call(11, 4), call(10, 4), call(11, 7), call(11, 4), call(10, 4),
        call(11, 7), call(11, 4), call(10, 7), call(11, 7), call(11, 4),
        call(10, 7), call(11, 7), call(11, 4), call(10, 7), call(11, 7),
        call(8, 7)
    ])
