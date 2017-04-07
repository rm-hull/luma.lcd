#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

import pytest

import luma.core.error
from luma.lcd.aux import backlight

from helpers import Mock


gpio = Mock(unsafe=True)


def setup_function(function):
    gpio.reset_mock()
    gpio.BCM = 1
    gpio.OUT = 2
    gpio.HIGH = 3
    gpio.LOW = 4


def test_unsupported_platform():
    e = RuntimeError('Module not imported correctly!')
    errorgpio = Mock(unsafe=True)
    errorgpio.setmode.side_effect = e

    try:
        backlight(gpio_LIGHT=19, gpio=errorgpio)
    except luma.core.error.UnsupportedPlatform as ex:
        assert str(ex) == 'GPIO access not available'


def test_init():
    gpio_LIGHT = 11
    backlight(gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.setmode.assert_called_once_with(gpio.BCM)
    gpio.setup.assert_called_once_with(gpio_LIGHT, gpio.OUT)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_active_low_enable_on():
    gpio_LIGHT = 14
    light = backlight(gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.reset_mock()
    light.enable(True)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_active_low_enable_off():
    gpio_LIGHT = 19
    light = backlight(gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.reset_mock()
    light.enable(False)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.HIGH)


def test_active_high_enable_on():
    gpio_LIGHT = 14
    light = backlight(gpio=gpio, gpio_LIGHT=gpio_LIGHT, active_low=False)
    gpio.reset_mock()
    light.enable(True)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.HIGH)


def test_active_high_enable_off():
    gpio_LIGHT = 19
    light = backlight(gpio=gpio, gpio_LIGHT=gpio_LIGHT, active_low=False)
    gpio.reset_mock()
    light.enable(False)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_params_deprecated():
    msg = 'bcm_LIGHT argument is deprecated in favor of gpio_LIGHT and will be removed in 1.0.0'

    with pytest.deprecated_call() as c:
        backlight(gpio=gpio, bcm_LIGHT=11)
        assert str(c.list[0].message) == msg
