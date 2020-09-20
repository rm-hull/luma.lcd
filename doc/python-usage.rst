Python Usage
============
LCD displays can be driven with python using the various implementations in the
:py:mod:`luma.lcd.device` package.  There are several device classes available
and usage is very simple if you have ever used
`Pillow <https://pillow.readthedocs.io/en/latest/>`_ or PIL.

To begin you must import the device class you will be using and the interface
class that you will use to communicate with your device:

In this example, we are using an SPI interface with a pcd8544 display.

.. code:: python

  from luma.core.interface.serial import i2c, spi, parallel, pcf8574
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544, st7735, st7567, uc1701x, ili9341, hd44780

  serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=24)
  device = pcd8544(serial)

The display device should now be properly configured.

The :py:class:`~luma.lcd.device.pcd8544`, :py:class:`~luma.lcd.device.st7735`,
:py:class:`~luma.lcd.device.st7567`, :py:class:`~luma.lcd.device.uc1701x`,  :py:class:`~luma.lcd.device.ili9341` and :py:class:`~luma.lcd.device.hd44780`
classes all expose a :py:meth:`~luma.lcd.device.pcd8544.display` method which
takes an image with attributes consistent with the capabilities of the device.

For most cases when drawing text and graphics primitives, the canvas
class should be used as follows:

.. code:: python

  with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="white", fill="black")
      draw.text((30, 40), "Hello World", fill="red")

The :py:class:`luma.core.render.canvas` class automatically creates an
:py:mod:`PIL.ImageDraw` object of the correct dimensions and bit depth suitable
for the device, so you may then call the usual Pillow methods to draw onto the
canvas.

As soon as the with scope is ended, the resultant image is automatically
flushed to the device's display memory and the :mod:`PIL.ImageDraw` object is
garbage collected.

.. note::
  When a program ends, the display is automatically cleared. This means that a
  fast program that ends quickly may never display a visible image.

.. note::
  The use of the display method for the HD44780 is more limited than the other
  LCDs.  The `text` property is the preferred interface for displaying
  characters.  See :doc:`HD44780` for more details.

Color Model
-----------
Any of the standard :py:mod:`PIL.ImageColor` color formats may be used if your
device supports them.  For monochrome LCDs, only the HTML color names
:py:const:`"black"` and :py:const:`"white"` values should really be used; in
fact, by default, any value *other* than black is treated as white. The
:py:class:`luma.core.render.canvas` object does have a :py:attr:`dither` flag
which if set to True, will convert color drawings to a dithered monochrome
effect (see the *3d_box.py* example, below).

.. code:: python

  with canvas(device, dither=True) as draw:
      draw.rectangle((10, 10, 30, 30), outline="white", fill="red")

The ST7735 and ILI9341 devices can display 262K colour RGB images.  When supplying
24-bit RGB images, they are automatically downscaled to 18-bit RGB to fit
these device's 262K color-space.

Landscape / Portrait Orientation
--------------------------------
By default the PCD8544, ST7735, UC1701X and ILI9341 displays will all be oriented
in landscape mode (84x48, 160x128, 128x64 and 320x240 pixels respectively). Should
you have an application that requires the display to be mounted in a portrait
aspect, then add a :py:attr:`rotate=N` parameter when creating the device:

.. code:: python

  from luma.core.interface.serial import spi
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544

  serial = spi(port=0, device=0, gpio_DC=23, gpio_RST=24)
  device = pcd8544(serial, rotate=1)

  # Box and text rendered in portrait mode
  with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="white", fill="black")
      draw.text((10, 40), "Hello World", fill="red")

*N* should be a value of 0, 1, 2 or 3 only, where 0 is no rotation, 1 is
rotate 90° clockwise, 2 is 180° rotation and 3 represents 270° rotation.

The :py:attr:`device.size`, :py:attr:`device.width` and :py:attr:`device.height`
properties reflect the rotated dimensions rather than the physical dimensions.

The HD44780 does not support display rotation.

Seven-Segment Drivers
---------------------
The HT1621 is driven with the :py:class:`luma.lcd.device.ht1621` class, but is
not accessed directly: it should be wrapped with the
:py:class:`luma.core.virtual.sevensegment` wrapper, as follows:

.. code:: python

   from luma.core.virtual import sevensegment
   from luma.lcd.device import ht1621

   device = ht1621()
   seg = sevensegment(device)


The **seg** instance now has a :py:attr:`~luma.led_matrix.virtual.sevensegment.text`
property which may be assigned, and when it does will update all digits
according to the limited alphabet the 7-segment displays support. For example,
assuming there are 2 cascaded modules, we have 16 character available, and so
can write:

.. code:: python

   seg.text = "HELLO"

Rather than updating the whole display buffer, it is possible to update
'slices', as per the below example:

.. code:: python

   seg.text[0:5] = "BYE"

This replaces ``HELLO`` in the previous example, replacing it with ``BYE``.
The usual python idioms for slicing (inserting / replacing / deleteing) can be
used here, but note if inserted text exceeds the underlying buffer size, a
:py:exc:`ValueError` is raised.

Floating point numbers (or text with '.') are handled slightly differently - the
decimal-place is fused in place on the character immediately preceding it. This
means that it is technically possible to get more characters displayed than the
buffer allows, but only because dots are folded into their host character.

Backlight Control
-----------------
These displays typically require a backlight to illuminate the liquid crystal
display.  If the display's backlight is connected to one of the single-board
computer's gpio pins, you can activate the backlight by specifying
``gpio_LIGHT=n`` where ``n`` = the pin number when initializing the
device (default GPIO 18 (PWM_CLK0)).

If the display uses an I2C backpack with a pin from the backpack connected to
the display's backlight pin, you can activate the backlight by specifying
``backpack_pin=n`` where n = the pin number on the backpack.

The backlight can be programmatically switched on and off by calling
``device.backlight(True)`` or ``device.backlight(False)`` respectively.

.. note::
  If you are using an I2C backpack based device, the backlight will not change
  until the next time you send a command or data to the device.

Examples
--------
After installing the library, head over to the
`luma.examples <https://github.com/rm-hull/luma.examples>`_
repository. Details of how to run the examples is shown in the `README <https://github.com/rm-hull/luma.examples/blob/master/README.rst>`_.
