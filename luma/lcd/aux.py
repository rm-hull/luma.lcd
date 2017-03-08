# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.


from luma.core import lib


__all__ = ["backlight"]


@lib.rpi_gpio
class backlight(object):
    """
    Controls a backlight, assumed to be on GPIO 18 (PWM_CLK0) by default.

    :param gpio: GPIO interface (must be compatible with `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_).
    :param bcm_LIGHT: the GPIO pin to use for the backlight.
    :type bcm_LIGHT: int
    :raises luma.core.error.UnsupportedPlatform: GPIO access not available.
    """
    def __init__(self, gpio=None, bcm_LIGHT=18):
        self._bcm_LIGHT = bcm_LIGHT
        self._gpio = gpio or self.__rpi_gpio__()
        self._gpio.setmode(self._gpio.BCM)
        self._gpio.setup(self._bcm_LIGHT, self._gpio.OUT)
        self.enable(True)

    def enable(self, value):
        """
        Switches on the backlight on and off.

        :param value: Switched on when ``True`` supplied, else ``False`` switches it off.
        :type value: bool
        """
        assert(value in [True, False])
        self._gpio.output(self._bcm_LIGHT,
                          self._gpio.LOW if value else self._gpio.HIGH)
