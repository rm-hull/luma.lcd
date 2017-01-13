Introduction
------------

Interfacing small `LCD displays
<https://github.com/rm-hull/luma.lcd/wiki/Usage-&-Benchmarking>`_ with the
PCD8544 driver in Python 2 or 3 using I2C/SPI on the Raspberry Pi and other
linux-based single-board computers: the library provides a Pillow-compatible
drawing canvas, and other functionality to support:

* scrolling/panning capability,
* terminal-style printing,
* state management,
* color/greyscale (where supported),
* dithering to monochrome

The PCD8544 display pictured below was used originally as the display for
`Nokia 5110 <https://en.wikipedia.org/wiki/Nokia_5110>`_ mobile phones,
supporting a resolution of 84 x 48 monochrome pixels and a switchable
backlight:

.. image:: images/pcd8544.png

They are now commonly recycled, and sold on ebay with a breakout board and SPI
interface.

.. seealso::
   Further technical information for the specific device can be found in the
   datasheet below: 
   
   - :download:`PCD8544 <tech-spec/PCD8544.pdf>`

As well as display drivers for the physical device, there are emulators that
run in real-time (with pygame) and others that can take screenshots, or
assemble animated GIFs, as per the examples below (source code for these is
available in the `examples <https://github.com/rm-hull/luma.examples>`_
repository.
