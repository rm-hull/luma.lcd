#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the :py:mod:`luma.lcd.segment_mapper` module.
"""

from luma.core.util import mutable_string
from luma.lcd.segment_mapper import dot_muncher


def test_dot_muncher_without_dots():
    buf = mutable_string("Hello world")
    results = dot_muncher(buf)
    assert list(results) == [0x67, 0x3f, 0x05, 0x05, 0x4e, 0x00, 0x08, 0x4e, 0x06, 0x05, 0x6e]


def test_dot_muncher_with_dot():
    buf = mutable_string("3.14159")
    results = dot_muncher(buf)
    assert list(results) == [0x7a, 0x60 | 0x80, 0x63, 0x60, 0x5b, 0x7b]


def test_dot_muncher_with_dot_at_end():
    buf = mutable_string("  525920")
    buf[7:] = ".0"
    print(buf)
    results = dot_muncher(buf)
    assert list(results) == [0x00, 0x00, 0x5b, 0x3e, 0x5b, 0x7b, 0x3e, 0x7d | 0x80]


def test_dot_muncher_with_multiple_dot():
    buf = mutable_string("127.0.0.1")
    results = dot_muncher(buf)
    assert list(results) == [0x60, 0x3e, 0x70, 0x7d | 0x80, 0x7d | 0x80, 0x60 | 0x80]
