#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013-17 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:class:`luma.lcd.device.ht1621` device.
"""

from luma.lcd.device import ht1621
from luma.core.virtual import sevensegment
from unittest.mock import Mock


class MockHT1621:
    """
    Mock the HT1621 internal state machine.

    Decodes the 3-pin serial data back into
    the expected data packets.
    """

    HIGH = 1
    LOW = 0
    OUT = 1
    IN = 0

    def __init__(self, WR=11, DAT=10, CS=8):
        self._pin_wr = WR
        self._pin_dat = DAT
        self._pin_cs = CS
        self.reset_mock()

    def command(self, data):
        """
        Build a command representation.
        """
        return ('cmd', data)

    def data(self, data):
        """
        Built a data representation.
        """
        return ('data', data)

    def setup(self, pin, state):
        """
        Mock GPIO.setup.
        """
        self._pin_states[pin] = state

    def output(self, pin, state):
        """
        Mock GPIO.output.
        """
        if pin == self._pin_wr:
            if self._state_wr == 0 and state == 1:  # Rising edge
                self._data <<= 1
                self._data |= self._state_dat
                self._bit_count += 1
            self._state_wr = state

        if pin == self._pin_dat and self._state_wr == 0:
            self._state_dat = state

        # Handle 4-bit command SOF
        if self._bit_count == 4 and self._state == 'none' and self._data == 0b1000:
            self._state = 'cmd'
            self._data = 0
            self._bit_count = 0

        # Handle 3-bit data SOF
        if self._bit_count == 3 and self._state == 'none' and self._data == 0b101:
            self._state = 'addr'
            self._data = 0
            self._bit_count = 0

        # Discard 6-bit address (it's always 0)
        if self._bit_count == 6 and self._state == 'addr':
            self._state = 'data'
            self._data = 0
            self._bit_count = 0

        # If we hit 8 bits, treat it as one packet
        if self._bit_count == 8:
            self._values.append((self._state, self._data))
            self._data = 0
            self._bit_count = 0

        # Reset state machine on CS rising edge
        if pin == self._pin_cs:
            if self._state_cs == 0 and state == 1:  # Rising edge
                self._data = 0
                self._bit_count = 0
                self._state = 'none'

    def reset_mock(self):
        """
        Reset state machine.
        """
        self._state_wr = 0     # Read/Write State
        self._state_dat = 0    # Data state
        self._state_cs = 0     # Chip-select state
        self._data = 0         # Current value
        self._bit_count = 0    # Count of bits in _data
        self._values = []      # All clocked-in values
        self._pin_states = {}  # Pin IO states
        self._state = 'none'   # Current state

    def cleanup(self, *args):
        """
        Mock GPIO.cleanup.
        """
        self.reset_mock()

    def get_data(self):
        """
        Return stored values.
        """
        return self._values

    def get_pin_states(self):
        """
        Return stored pin output states.
        """
        return self._pin_states


gpio = MockHT1621()


def setup_function(function):
    """
    Called before a test runs.
    """
    gpio.reset_mock()


def test_init_6x8():
    ht1621(gpio, serial_interface=Mock())

    assert gpio.get_pin_states() == {
        11: gpio.OUT,
        10: gpio.OUT,
        8: gpio.OUT,
        18: gpio.OUT
    }

    assert gpio.get_data() == [
        gpio.command(0x30),  # Internal RC oscillator @ 256KHz
        gpio.command(0x52),  # 1/2 Bias and 4 commons
        gpio.command(0x02),  # System enable
        gpio.data(0),        # Column Data
        gpio.data(0),        # "
        gpio.data(0),        #
        gpio.data(0),        #
        gpio.data(0),        #
        gpio.data(0),        #
        gpio.command(0x06)   # Display On
    ]


def test_cleanup():
    device = ht1621(gpio)
    gpio.reset_mock()
    device.cleanup()
    assert gpio.get_data() == []  # No activity unless persist is True


def test_hide():
    device = ht1621(gpio)
    gpio.reset_mock()
    device.hide()
    assert gpio.get_data() == [gpio.command(0x04)]  # Display Off


def test_show():
    device = ht1621(gpio)
    gpio.reset_mock()
    device.show()
    assert gpio.get_data() == [gpio.command(0x06)]  # Display On


def test_display():
    device = ht1621(gpio)
    gpio.reset_mock()

    sevensegment(device).text = "HELLO"

    assert gpio.get_data() == [
        gpio.data(0), gpio.data(0), gpio.data(0),     # _ _ _
        gpio.data(0), gpio.data(0), gpio.data(0),     # _ _ _
        gpio.data(0), gpio.data(125), gpio.data(13),  # _ O L
        gpio.data(13), gpio.data(31), gpio.data(103)  # L E H
    ]
