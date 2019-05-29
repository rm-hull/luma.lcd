#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

import luma.core.error
from luma.lcd.device import backlit_device
from luma.core.interface.serial import noop
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
        backlit_device(serial_interface=noop(), gpio_LIGHT=19, gpio=errorgpio)
    except luma.core.error.UnsupportedPlatform as ex:
        assert str(ex) == 'GPIO access not available'


def test_init():
    gpio_LIGHT = 11
    backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.setmode.assert_called_once_with(gpio.BCM)
    gpio.setup.assert_called_once_with(gpio_LIGHT, gpio.OUT)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_active_low_enable_on():
    gpio_LIGHT = 14
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.reset_mock()
    device.backlight(True)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_active_low_enable_off():
    gpio_LIGHT = 19
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.reset_mock()
    device.backlight(False)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.HIGH)


def test_active_high_enable_on():
    gpio_LIGHT = 14
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, active_low=False)
    gpio.reset_mock()
    device.backlight(True)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.HIGH)


def test_active_high_enable_off():
    gpio_LIGHT = 19
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, active_low=False)
    gpio.reset_mock()
    device.backlight(False)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)
