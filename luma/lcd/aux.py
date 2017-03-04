# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.


class backlight(object):
    """
    Controls a backlight (assumed to be on GPIO 18 (PWMCLK0)).

    :param gpio:
    :param bcm_LIGHT:
    :type bcm_LIGHT: int
    """
    def __init__(self, gpio=None, bcm_LIGHT=18):
        self._bcm_LIGHT = bcm_LIGHT
        self._gpio = gpio or self.__rpi_gpio__()
        self._gpio.setmode(self._gpio.BCM)
        self._gpio.setup(self._bcm_LIGHT, self._gpio.OUT)
        self.enable(True)

    def enable(self, value):
        """
        Switches on the backlight when ``True`` supplied, else ``False``
        switches it off
        """
        assert(value in [True, False])
        self._gpio.output(self._bcm_LIGHT,
                          self._gpio.LOW if value else self._gpio.HIGH)

    def __rpi_gpio__(self):
        # RPi.GPIO _really_ doesn't like being run on anything other than
        # a Raspberry Pi... this is imported here so we can swap out the
        # implementation for a mock
        import RPi.GPIO
        return RPi.GPIO
