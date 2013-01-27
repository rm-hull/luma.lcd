PDC8544 LCD python bindings for the Raspberry Pi
================================================

Documentation and Python library module for interfacing a PCD8544 LCD 
screen to a Rasbperry Pi.

![PCD8544](https://raw.github.com/rm-hull/pcd8544/master/doc/pcd8544.png) ![Spec](https://raw.github.com/rm-hull/pcd8544/master/doc/tech-spec/spec.png)

Further technical details for the LCD screen can be found in the 
[datasheet](https://raw.github.com/rm-hull/pcd8544/master/doc/tech-spec/datasheet.pdf) [PDF].

Pre-requisites
--------------
Compile and install the wiringPi python bindings from https://github.com/rm-hull/wiringPi

Building and installing the software
------------------------------------
TODO

Wiring schematic
----------------
There appears to be different pin-out configurations on PCD8544 modules - beware!

![Wiring Schematic](https://raw.github.com/rm-hull/pcd8544/master/doc/wiring-diagram.png)

Modified for my wiring setup from an SVG from http://shiro.be/ - all 
rights of the original author respected.

Stripboard Layout
-----------------
With 4 push-buttons, resistor values 10K.

![Stripboard Layout](https://raw.github.com/rm-hull/pcd8544/master/doc/schematic_bb.png)

Buttons (from top to bottom) are wired onto BCM pins as follows:

* GPIO 14 (TxD)
* GPIO 17 
* GPIO 25
* GPIO 22 

TODO
----
* Documentation

* Examples

* Implement video ram & get/set_pixel

* Setup / installer

References
----------
* http://elinux.org/Rpi_Low-level_peripherals#General_Purpose_Input.2FOutput_.28GPIO.29

* http://binerry.de/post/25787954149/pcd8544-library-for-raspberry-pi

* http://www.avdweb.nl/arduino/hardware-interfacing/nokia-5110-lcd.html

* http://www.raspberrypi.org/phpBB3/viewtopic.php?f=32&t=9814&start=100

* https://projects.drogon.net/raspberry-pi/wiringpi/pins/

* http://www.henningkarlsen.com/electronics/t_imageconverter_mono.php

* http://fritzing.org
