Installation
------------

.. note:: The library has been tested against Python 2.7, 3.4, 3.5 and 3.6.

   For **Python3** installation, substitute the following in the
   instructions below.

   * ``pip`` ⇒ ``pip3``,
   * ``python`` ⇒ ``python3``,
   * ``python-dev`` ⇒ ``python3-dev``,
   * ``python-pip`` ⇒ ``python3-pip``.

   It was *originally* tested with Raspbian on a rev.2 model B, with a vanilla
   kernel version 4.1.16+, and has subsequently been tested on Raspberry Pi
   (both Raspbian Jessie and Stretch) models A, B2, 3B, Zero, Zero W and
   OrangePi Zero (Armbian Jessie).

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

  $ sudo usermod -a -G spi pi
  $ sudo usermod -a -G gpio pi

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
    you can select other pins and pass :py:attr:`gpio_DC` and/or :py:attr:`gpio_RST`
    argument specifying the new *GPIO* pin numbers in your serial interface create
    call (this applies to PCD8544, ST7567 and ST7735).

  * Because CE is connected to CE0, the display is available on SPI port 0. You
    can connect it to CE1 to have it available on port 1. If so, pass
    :py:attr:`port=1` in your serial interface create call.

PCD8544
"""""""

======== ============ ======== ==============
LCD Pin  Remarks      RPi Pin  RPi Function
======== ============ ======== ==============
RST      Reset        P01-18   GPIO 24 
CE       Chip Enable  P01-24   GPIO 8 (CE0)
DC       Data/Command P01-16   GPIO 23
DIN      Data In      P01-19   GPIO 10 (MOSI)
CLK      Clock        P01-23   GPIO 11 (SCLK)
VCC      +3.3V Power  P01-01   3V3
LIGHT    Backlight    P01-12   GPIO 18 (PCM_CLK)
GND      Ground       P01-06   GND
======== ============ ======== ==============

ST7735
""""""
Depending on the board you bought, there may be different names for the same
pins, as detailed below.

============= ================= ======== ==============
LCD Pin       Remarks           RPi Pin  RPi Function
============= ================= ======== ==============
GND           Ground            P01-06   GND
VCC           +3.3V Power       P01-01   3V3
RESET or RST  Reset             P01-18   GPIO 24
A0 or D/C     Data/command      P01-16   GPIO 23
SDA or DIN    SPI data          P01-19   GPIO 10 (MOSI)
SCK or CLK    SPI clock         P01-23   GPIO 11 (SCLK)
CS            SPI chip select   P01-24   GPIO 8 (CE0)
LED+ or BL    Backlight control P01-12   GPIO 18 (PCM_CLK)
LED-          Backlight ground  P01-06   GND
============= ================= ======== ==============

ST7567
""""""
This driver is designed for the ST7567 in 4-line SPI mode and does not include
parallel bus support.

Pin names may differ across different breakouts, but will generally be something
like the below.

============= ================= ======== ==============
LCD Pin       Remarks           RPi Pin  RPi Function
============= ================= ======== ==============
GND           Ground            P01-06   GND
3v3           +3.3V Power       P01-01   3V3
RESET or RST  Reset             P01-18   GPIO 24
SA0 or D/C    Data/command      P01-16   GPIO 23
SDA or DATA   SPI data          P01-19   GPIO 10 (MOSI)
SCK or CLK    SPI clock         P01-23   GPIO 11 (SCLK)
CS            SPI chip select   P01-24   GPIO 8 (CE0)
============= ================= ======== ==============

HT1621
""""""

============= ================= ======== ==============
LCD Pin       Remarks           RPi Pin  RPi Function
============= ================= ======== ==============
GND           Ground            P01-06   GND
VCC           +3.3V Power       P01-01   3V3
DAT           SPI data          P01-19   GPIO 10 (MOSI)
WR            SPI clock         P01-23   GPIO 11 (SCLK)
CS            SPI chip select   P01-24   GPIO 8 (CE0)
LED           Backlight control P01-12   GPIO 18 (PCM_CLK)
============= ================= ======== ==============

UC1701X
"""""""
The UC1701X doesn't appear to work from 3.3V, but does on
the 5.0V rail.

============= ================= ======== ==============
LCD Pin       Remarks           RPi Pin  RPi Function
============= ================= ======== ==============
ROM_IN        Unused
ROM_OUT       Unused
ROM_SCK       Unused
ROM_CS        Unused
LED A         Backlight control P01-12   GPIO 18 (PCM_CLK)
VSS           Ground            P01-06   GND
VDD           +5.0V             P01-02   5V0
SCK           SPI clock         P01-23   GPIO 11 (SCLK)
SDA           SPI data          P01-19   GPIO 10 (MOSI)
RS            Data/command      P01-16   GPIO 23
RST           Reset             P01-18   GPIO 24
CS            SPI chip select   P01-24   GPIO 8 (CE0)	Chip Select
============= ================= ======== ==============

Installing from PyPI
^^^^^^^^^^^^^^^^^^^^
First, install the dependencies for the library with::

  $ sudo usermod -a -G spi,gpio pi
  $ sudo apt-get install python-dev python-pip

And finally, install the latest version of the library directly from
`PyPI <https://pypi.python.org/pypi?:action=display&name=luma.lcd>`__
with::

  $ sudo -H pip install --upgrade luma.lcd

.. warning:: The default pip bundled with apt on Raspbian Jessie is really old, and can 
   cause components to not be installed properly. Please ensure that **pip 9.0.1** 
   is installed prior to continuing::
   
      $ pip --version
      pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)
