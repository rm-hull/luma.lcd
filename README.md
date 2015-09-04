PDC8544 LCD python bindings for the Raspberry Pi
================================================

Documentation and Python library module for interfacing a PCD8544 LCD 
screen to a Rasbperry Pi. Cheap Nokia 5110 modules can be picked up
on ebay with a breakout board for a few pounds.

![PCD8544](https://raw.github.com/rm-hull/pcd8544/master/doc/pcd8544.png) ![Spec](https://raw.github.com/rm-hull/pcd8544/master/doc/tech-spec/spec.png)

Further technical details for the LCD screen can be found in the 
[datasheet](https://raw.github.com/rm-hull/pcd8544/master/doc/tech-spec/datasheet.pdf) [PDF].

Pre-requisites
--------------
Compile and install the wiringPi python bindings from https://github.com/rm-hull/wiringPi. Make sure you install both python-dev and libi2c-dev. 
This library specifically requires the python binding baked into this software, which have
not been pushed back to drogon.

Next, install PIL (Python Imaging Library) as follows:

    $ sudo apt-get install zlibc libpng3 libfreetype6 libfreetype6-dev python-pip
    $ sudo pip install pillow

Building and installing the software
------------------------------------
After having cloned from github:

    $ python setup.py clean build
    $ sudo python setup.py install

This should install the files in your local dist-files ares (somewhere
like `/usr/local/lib/python2.7/distfiles/pcd8544`).

Next, test at the hardware and software is working:

    $ cd examples
    $ sudo ./alphabet_text.py

Most of the ASCII character set should be displayed. There are a few
other examples of graphics rendering in the same directory.

Wiring schematic
----------------
There appears to be different pin-out configurations on PCD8544 modules - beware!

![Wiring Schematic](https://raw.github.com/rm-hull/pcd8544/master/doc/wiring-diagram.png)

Although the python library (currently) used software-base bit-banging to do the SPI chattering, 
the pins chosen should be compatible with hardware SPI. The above diagram was modified for 
*my* wiring setup from an SVG from http://shiro.be/ - all rights of the original author reserved.

Stripboard Layout
-----------------
With 4 push-buttons, resistor values 10K.

![Stripboard Layout](https://raw.github.com/rm-hull/pcd8544/master/doc/schematic_bb.png)

Buttons (from top to bottom) are wired onto BCM pins as follows:

* GPIO 14 (TxD)
* GPIO 17 
* GPIO 25
* GPIO 22 

The finished article, and a [video](https://vimeo.com/58752313):

![Built stripboard](https://github.com/rm-hull/pcd8544/blob/master/doc/images/IMG_2544.JPG?raw=true)

TODO
----
* Documentation

* More examples

* Introduce small/tiny font handling onto drawable PIL surfaces

* Implement module for scanning push buttons 

* Hardware SPI rather than software emulation

References
----------
* http://elinux.org/Rpi_Low-level_peripherals#General_Purpose_Input.2FOutput_.28GPIO.29

* http://binerry.de/post/25787954149/pcd8544-library-for-raspberry-pi

* http://www.avdweb.nl/arduino/hardware-interfacing/nokia-5110-lcd.html

* http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=9814&start=100

* https://projects.drogon.net/raspberry-pi/wiringpi/pins/

* http://www.henningkarlsen.com/electronics/t_imageconverter_mono.php

* https://vimeo.com/41393421

* http://fritzing.org


The MIT License (MIT)
---------------------

Copyright (c) 2015 Richard Hull

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


