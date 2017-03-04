Hardware
--------

Pre-requisites
^^^^^^^^^^^^^^
Enable the SPI port::

  $ sudo raspi-config
  > Advanced Options > A6 SPI

If ``raspi-config`` is not available, enabling the SPI port can be done
`manually <http://elinux.org/RPiconfig#Device_Tree>`_.

Ensure that the SPI kernel driver is enabled::

  $ ls -l /dev/spi*
  crw-rw---- 1 root spi 153, 0 Nov 25 08:32 /dev/spidev0.0
  crw-rw---- 1 root spi 153, 1 Nov 25 08:32 /dev/spidev0.1

or::

  $ lsmod | grep spi
  spi_bcm2835             6678  0

Then add your user to the *spi* and *gpio* groups::

  $ sudo usermod -a G spi pi
  $ sudo usermod -a G gpio pi

Log out and back in again to ensure that the group permissions are applied
successfully.

Connecting the display
^^^^^^^^^^^^^^^^^^^^^^
* If you don't want to solder directly on the Pi, get 2.54mm 40 pin female
  single row headers, cut them to length, push them onto the Pi pins, then
  solder wires to the headers.

* If you need to remove existing pins to connect wires, be careful to heat
  each pin thoroughly, or circuit board traces may be broken.

* Triple check your connections. In particular, do not reverse VCC and GND.

The GPIO pins used for this SPI connection are the same for all versions of the
Raspberry Pi, up to and including the Raspberry Pi 3 B.

.. warning::
   There appears to be varying pin-out configurations on different modules - beware!

.. note::

  * If you're already using the listed GPIO pins for Data/Command and/or Reset,
    you can select other pins and pass :py:attr:`bcm_DC` and/or :py:attr:`bcm_RST`
    argument specifying the new *BCM* pin numbers in your serial interface create
    call (this applies to both PCD8544 and ST7735).

  * Because CE is connected to CE0, the display is available on SPI port 0. You
    can connect it to CE1 to have it available on port 1. If so, pass
    :py:attr:`port=1` in your serial interface create call.

PCD8544
"""""""
========== ====== ============ ======== ==============
LCD Pin    Name   Remarks      RPi Pin  RPi Function
========== ====== ============ ======== ==============
1          RST    Reset        P01-18   GPIO 24 
2          CE     Chip Enable  P01-24   GPIO 8 (CE0)
3          DC     Data/Command P01-16   GPIO 23
4          DIN    Data In      P01-19   GPIO 10 (MOSI)
5          CLK    Clock        P01-23   GPIO 11 (SCLK)
6          VCC    +3.3V Power  P01-01   3V3
7          LIGHT  Backlight    P01-12   GPIO 18 (PCM_CLK)
8          GND    Ground       P01-06   GND
========== ====== ============ ======== ==============

ST7735
""""""
========== ======= ================= ======== ==============
LCD Pin    Name    Remarks           RPi Pin  RPi Function
========== ======= ================= ======== ==============
1          GND     Ground            P01-06   GND
2          VCC     +3.3V Power       P01-01   3V3
3          NC      Not connected     -        -
4          NC      Not connected     -        -
5          NC      Not connected     -        -
6          RESET   Reset             P01-18   GPIO 24
7          A0      Data/command      P01-16   GPIO 23
8          SDA     SPI data          P01-19   GPIO 10 (MOSI)
9          SCK     SPI clock         P01-23   GPIO 11 (SCLK)
10         CS      SPI chip select   P01-24   GPIO 8 (CE0)
11         SD-SCK  SD serial clock   -        -
12         SD-MISO SD data in        -        -
13         SD-MOSI SD data out       -        -
14         SD-CS   SD chip select    -        -
15         LED+    Backlight control P01-12   GPIO 18 (PCM_CLK)
16         LED-    Backlight ground  P01-06   GND
========== ======= ================= ======== ==============

