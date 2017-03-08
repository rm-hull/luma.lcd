#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

import luma.core.error
from luma.lcd.aux import backlight


gpio = Mock(unsafe=True)


def setup_function(function):
    gpio.reset_mock()
    gpio.BCM = 1
    gpio.OUT = 2
    gpio.HIGH = 3
    gpio.LOW = 4


def test_unsupported_platform():
    try:
        e = RuntimeError('Module not imported correctly!')
        errorgpio = Mock(unsafe=True)
        errorgpio.setmode.side_effect = e
        backlight(bcm_LIGHT=19, gpio=errorgpio)
    except luma.core.error.UnsupportedPlatform as ex:
        assert str(ex) == 'GPIO access not available'


def test_init():
    backlight(gpio=gpio, bcm_LIGHT=11)
    gpio.setmode.assert_called_once_with(gpio.BCM)
    gpio.setup.assert_called_once_with(11, gpio.OUT)
    gpio.output.assert_called_once_with(11, gpio.LOW)


def test_enable_on():
    light = backlight(gpio=gpio, bcm_LIGHT=14)
    gpio.reset_mock()
    light.enable(True)
    gpio.output.assert_called_once_with(14, gpio.LOW)


def test_enable_off():
    light = backlight(gpio=gpio, bcm_LIGHT=19)
    gpio.reset_mock()
    light.enable(False)
    gpio.output.assert_called_once_with(19, gpio.HIGH)
