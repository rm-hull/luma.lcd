# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

_DIGITS = {
    ' ': 0x00,
    '\'': 0x01,
    ',': 0x80,
    '-': 0x02,
    '.': 0x80,
    '0': 0x7d,
    '1': 0x60,
    '2': 0x3e,
    '3': 0x7a,
    '4': 0x63,
    '5': 0x5b,
    '6': 0x5f,
    '7': 0x70,
    '8': 0x7f,
    '9': 0x7b,
    'A': 0x77,
    'B': 0x7f,
    'C': 0x1d,
    'D': 0x7d,
    'E': 0x1f,
    'F': 0x17,
    'G': 0x5d,
    'H': 0x67,
    'I': 0x60,
    'J': 0x68,
    # 'K': cant represent
    'L': 0x0d,
    # 'M': cant represent
    'N': 0x75,
    'O': 0x7d,
    'P': 0x37,
    'Q': 0x73,
    'R': 0x15,
    'S': 0x5b,
    'T': 0x0f,
    'U': 0x6d,
    'V': 0x6d,
    # 'W': cant represent
    # 'X': cant represent
    'Y': 0x6b,
    'Z': 0x3e,
    '_': 0x08,
    'a': 0x7e,
    'b': 0x4f,
    'c': 0x0e,
    'd': 0x6e,
    'e': 0x3f,
    'f': 0x17,
    'g': 0x7b,
    'h': 0x47,
    'i': 0x40,
    'j': 0x48,
    # 'k': cant represent
    'l': 0x05,
    # 'm': cant represent
    'n': 0x46,
    'o': 0x4e,
    'p': 0x37,
    'q': 0x73,
    'r': 0x06,
    's': 0x5b,
    't': 0x0f,
    'u': 0x4c,
    'v': 0x4c,
    # 'w': cant represent
    # 'x': cant represent
    'y': 0x6b,
    'z': 0x3e
}


def dot_muncher(text, notfound="_"):
    undefined = _DIGITS[notfound]
    iterator = iter(text)
    try:
        while True:
            curr = _DIGITS.get(next(iterator), undefined)

            if curr == 0x80:
                curr = _DIGITS.get(next(iterator), undefined) | 0x80

            yield curr

    except StopIteration:
        pass
