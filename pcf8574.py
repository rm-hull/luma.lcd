# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

class pcf8574(object):

    def __init__(self, bus=None, port=1, address=0x27):
        import smbus2

        self._addr = int(str(address), 0)
        self._managed = bus is None
        self._bus = bus or smbus2.SMBus(port)

    def command(self, *cmd):
        for value in cmd:
            self._write_4bits(value >> 4, False)
            self._write_4bits(value & 0x0F, False)

    def data(self, data):
        for value in data:
            self._write_4bits(value >> 4, True)
            self._write_4bits(value & 0x0F, True)

    def _write_4bits(self, value, register_select):
        value <<= 4

        # Backlight control
        value |= 0x08

        if register_select:
            value |= 0x01

        self._bus.write_byte_data(self._addr, 0, value & ~0x04)  # enable low
        time.sleep(1 / 1000000)
        self._bus.write_byte_data(self._addr, 0, value | 0x04)  # enable high
        time.sleep(1 / 1000000)
        self._bus.write_byte_data(self._addr, 0, value & ~0x04)  # enable low
        time.sleep(100 / 1000000)

    def cleanup(self):
        """
        Clean up I²C resources
        """
        if self._managed:
            self._bus.close()


import time

i2c = pcf8574()

# Hitachi manual page 46
i2c.command(0x03)
time.sleep(4.5 / 1000)
i2c.command(0x03)
time.sleep(4.5 / 1000)
i2c.command(0x03)
time.sleep(100 / 1000000)
i2c.command(0x02)

i2c.command(0x20) # Function set
i2c.command(0x01) # Clear display
i2c.command(0x06) # Entry mode
i2c.command(0x0F) # Display on / cursor on / blinking on

i2c.data([65, 66, 67, 68, 69])

