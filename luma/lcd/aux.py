# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.


from luma.core import lib, error
from luma.core.util import deprecation


__all__ = ["backlight"]


@lib.rpi_gpio
class backlight(object):
    """
    Controls a backlight (active low), assumed to be on GPIO 18 (PWM_CLK0) by default.


    :param gpio: GPIO interface (must be compatible with `RPi.GPIO <https://pypi.python.org/pypi/RPi.GPIO>`_).
    :param gpio_LIGHT: the GPIO pin to use for the backlight.
    :type gpio_LIGHT: int
    :param bcm_LIGHT: Deprecated. Use ``gpio_LIGHT`` instead.
    :type bcm_LIGHT: int
    :raises luma.core.error.UnsupportedPlatform: GPIO access not available.
    """
    def __init__(self, gpio=None, gpio_LIGHT=18, bcm_LIGHT=None, active_low=True):
        if bcm_LIGHT is not None:
            deprecation('bcm_LIGHT argument is deprecated in favor of gpio_LIGHT and will be removed in 1.0.0')
            gpio_LIGHT = bcm_LIGHT

        self._gpio_LIGHT = gpio_LIGHT
        self._gpio = gpio or self.__rpi_gpio__()
        if active_low:
            self._enabled = self._gpio.LOW
            self._disabled = self._gpio.HIGH
        else:
            self._enabled = self._gpio.HIGH
            self._disabled = self._gpio.LOW

        try:
            self._gpio.setmode(self._gpio.BCM)
            self._gpio.setup(self._gpio_LIGHT, self._gpio.OUT)
        except RuntimeError as e:
            if str(e) == 'Module not imported correctly!':
                raise error.UnsupportedPlatform('GPIO access not available')

        self.enable(True)

    def enable(self, value):
        """
        Switches on the backlight on and off.

        :param value: Switched on when ``True`` supplied, else ``False`` switches it off.
        :type value: bool
        """
        assert(value in [True, False])
        self._gpio.output(self._gpio_LIGHT,
                          self._enabled if value else self._disabled)
