`luma.core <https://github.com/rm-hull/luma.core>`__ **|**
`luma.docs <https://github.com/rm-hull/luma.docs>`__ **|**
`luma.emulator <https://github.com/rm-hull/luma.emulator>`__ **|**
`luma.examples <https://github.com/rm-hull/luma.examples>`__ **|**
luma.lcd **|**
`luma.led_matrix <https://github.com/rm-hull/luma.led_matrix>`__ **|**
`luma.oled <https://github.com/rm-hull/luma.oled>`__

luma.lcd
========
**HD44780, PCD8544, ST7735, ST7567, HT1621, UC1701X, ILI9341 Display Drivers**

.. image:: https://github.com/rm-hull/luma.lcd/workflows/luma.lcd/badge.svg?branch=master
   :target: https://github.com/rm-hull/luma.lcd/actions?workflow=luma.lcd

.. image:: https://coveralls.io/repos/github/rm-hull/luma.lcd/badge.svg?branch=master
   :target: https://coveralls.io/github/rm-hull/luma.lcd?branch=master

.. image:: https://readthedocs.org/projects/luma-lcd/badge/?version=latest
   :target: http://luma-lcd.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://img.shields.io/pypi/pyversions/luma.lcd.svg
   :target: https://pypi.python.org/pypi/luma.lcd

.. image:: https://img.shields.io/pypi/v/luma.lcd.svg
   :target: https://pypi.python.org/pypi/luma.lcd

.. image:: https://img.shields.io/pypi/dm/luma.lcd
   :target: https://pypi.python.org/project/luma.lcd

.. image:: https://img.shields.io/maintenance/yes/2020.svg?maxAge=2592000

luma.lcd provides a Python 3 interface to small LCD displays connected to
Raspberry Pi and other Linux-based single-board computers (SBC).  It provides a
Pillow-compatible drawing canvas, and other functionality to support:

* scrolling/panning capability,
* terminal-style printing,
* state management,
* color/greyscale (where supported),
* dithering to monochrome

It currently supports devices using the HD44780, PCD8544, ST7735, HT1621,
and UC1701X controllers.

All modules can be picked up on ebay with a breakout board for a few pounds.

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/hd44780_20x4.jpg

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/pcd8544.png

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/st7735.jpg

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/ht1621.jpg

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/uc1701x.png

.. image:: https://raw.github.com/rm-hull/luma.lcd/master/doc/images/ili9341.jpg

Documentation
-------------
Full documentation with installation instructions and examples can be found on
https://luma-lcd.readthedocs.io.

Breaking changes
----------------
Version 2.0.0 was released on 2 June 2019: this came with the removal of the
``luma.lcd.aux.backlight`` class. The equivalent functionality has now
been subsumed into the device classes that have a backlight capability.

License
-------
The MIT License (MIT)

Copyright (c) 2013-2020 Richard Hull & Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
