#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

import luma.core.error
from luma.lcd.device import backlit_device
from luma.core.interface.serial import noop
from unittest.mock import Mock
import pytest


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
    errorgpio.setup.side_effect = e

    try:
        backlit_device(serial_interface=noop(), gpio_LIGHT=19, gpio=errorgpio)
    except luma.core.error.UnsupportedPlatform as ex:
        assert str(ex) == 'GPIO access not available'
    else:
        pytest.fail("Didn't raise exception")


def test_init():
    gpio_LIGHT = 11
    backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.setup.assert_called_once_with(gpio_LIGHT, gpio.OUT)
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.LOW)


def test_cleanup():
    gpio_LIGHT = 11
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT)
    gpio.reset_mock()
    device.cleanup()
    gpio.output.assert_called_once_with(gpio_LIGHT, gpio.HIGH)


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


def test_pwm_turn_off():
    gpio_LIGHT = 18
    pwm_mock = Mock()
    gpio.PWM.return_value = pwm_mock
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, pwm_frequency=100)
    gpio.PWM.assert_called_once_with(gpio_LIGHT, 100)
    gpio.reset_mock()
    device.backlight(False)
    pwm_mock.ChangeDutyCycle.assert_called_once_with(0.0)


def test_pwm_turn_on():
    gpio_LIGHT = 18
    pwm_mock = Mock()
    gpio.PWM.return_value = pwm_mock
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, pwm_frequency=100)
    gpio.PWM.assert_called_once_with(gpio_LIGHT, 100)
    gpio.reset_mock()
    device.backlight(True)
    pwm_mock.ChangeDutyCycle.assert_called_once_with(100.0)


def test_pwm_turn_50_percent():
    gpio_LIGHT = 18
    pwm_mock = Mock()
    gpio.PWM.return_value = pwm_mock
    device = backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, pwm_frequency=100)
    gpio.PWM.assert_called_once_with(gpio_LIGHT, 100)
    gpio.reset_mock()
    device.backlight(50.0)
    pwm_mock.ChangeDutyCycle.assert_called_once_with(50.0)


def test_pwm_unsupported_platform():
    gpio_LIGHT = 18
    e = RuntimeError('Module not imported correctly!')
    gpio.PWM.side_effect = e

    try:
        backlit_device(serial_interface=noop(), gpio=gpio, gpio_LIGHT=gpio_LIGHT, pwm_frequency=100)
    except luma.core.error.UnsupportedPlatform as ex:
        assert str(ex) == 'GPIO access not available'
    else:
        pytest.fail("Didn't raise exception")
