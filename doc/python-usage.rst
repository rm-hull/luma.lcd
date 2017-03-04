Python usage
------------
The PCD8544 is driven with python using the implementation in the
:py:class:`luma.lcd.device.pcd8544` class. Likewise, to drive the ST7735, use
the :py:class:`luma.lcd.device.st7735` class. Usage is very simple if you have
ever used `Pillow <https://pillow.readthedocs.io/en/latest/>`_ or PIL.

First, import and initialise the device:

.. code:: python

  from luma.core.serial import spi
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544, st7735

  serial = spi(port=0, device=0, bcm_DC=23, bcm_RST=24)
  device = pcd8544(serial)

The display device should now be configured for use. Note, all the example code
snippets in this section are interchangeable between PCD8544 and ST7735
devices.

Both the :py:class:`~luma.lcd.device.pcd8544` and
:py:class:`~luma.lcd.device.st7735` classes expose a
:py:meth:`~luma.lcd.device.pcd8544.display` method which takes an image with
attributes consistent with the capabilities of the device. However, for most
cases, for drawing text and graphics primitives, the canvas class should be
used as follows:

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

Color Model
^^^^^^^^^^^
Any of the standard :py:mod:`PIL.ImageColor` color formats may be used, but
since the PCD8544 LCD is monochrome, only the HTML color names
:py:const:`"black"` and :py:const:`"white"` values should really be used; in
fact, by default, any value *other* than black is treated as white. The
:py:class:`luma.core.render.canvas` object does have a :py:attr:`dither` flag
which if set to True, will convert color drawings to a dithered monochrome
effect (see the *3d_box.py* example, below).

.. code:: python

  with canvas(device, dither=True) as draw:
      draw.rectangle((10, 10, 30, 30), outline="white", fill="red")

Note that there is no such limitation for the ST7735 device which supports 262K
colour RGB images, whereby 24-bit RGB images are downscaled to 18-bit RGB.

Landscape / Portrait Orientation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default the PCD8544 and ST7735 displays will both be oriented in landscape
mode (84x48 and 160x128 pixels respectively). Should you have an application
that requires the display to be mounted in a portrait aspect, then add a
:py:attr:`rotate=N` parameter when creating the device:

.. code:: python

  from luma.core.serial import spi
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544
  
  serial = spi(port=0, device=0, bcm_DC=23, bcm_RST=23)
  device = pcd8544(serial, rotate=1)

  # Box and text rendered in portrait mode
  with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="white", fill="black")
      draw.text((10, 40), "Hello World", fill="red")

*N* should be a value of 0, 1, 2 or 3 only, where 0 is no rotation, 1 is
rotate 90° clockwise, 2 is 180° rotation and 3 represents 270° rotation.

The :py:attr:`device.size`, :py:attr:`device.width` and :py:attr:`device.height`
properties reflect the rotated dimensions rather than the physical dimensions.

Backlight Control
^^^^^^^^^^^^^^^^^
These displays typically require a backlight to illuminate the liquid crystal
display: the :py:class:`luma.lcd.aux.backlight` class allows a BCM pin to
be specified to control the backlight through software.

Examples
^^^^^^^^
After installing the library, download the `luma.examples
<https://github.com/rm-hull/luma.examples>`_ directory and try running the
following examples:

=============== ========================================================
Example         Description
=============== ========================================================
3d_box.py       Rotating 3D box wireframe & color dithering
bounce.py       Display a bouncing ball animation and frames per second
carousel.py     Showcase viewport and hotspot functionality
clock.py        An analog clockface with date & time
colors.py       Color rendering demo
crawl.py        A vertical scrolling demo, which should be familiar
demo.py         Use misc draw commands to create a simple image
game_of_life.py Conway's game of life
grayscale.py    Greyscale rendering demo
invaders.py     Space Invaders demo
maze.py         Maze generator
perfloop.py     Simple benchmarking utility to measure performance
pi_logo.py      Display the Raspberry Pi logo (loads image as .png)
savepoint.py    Example of savepoint/restore functionality
starfield.py    3D starfield simulation
sys_info.py     Display basic system information
terminal.py     Simple println capabilities
tv_snow.py      Example image-blitting
welcome.py      Unicode font rendering & scrolling
=============== ========================================================

See the README in that project for further information on how to run the demos.

Emulators
^^^^^^^^^
There are various display emulators available for running code against, for
debugging and screen capture functionality:

* The :py:class:`luma.emulator.device.capture` device will persist a numbered
  PNG file to disk every time its :py:meth:`~luma.emulator.device.capture.display`
  method is called.

* The :py:class:`luma.emulator.device.gifanim` device will record every image
  when its :py:meth:`~luma.emulator.device.gifanim.display` method is called,
  and on program exit (or Ctrl-C), will assemble the images into an animated GIF.

* The :py:class:`luma.emulator.device.pygame` device uses the :py:mod:`pygame`
  library to render the displayed image to a pygame display surface.

Invoke the demos with::

  $ python examples/clock.py -d capture

or::

  $ python examples/clock.py -d pygame
  
.. note::
   *Pygame* is required to use any of the emulated devices, but it is **NOT**
   installed as a dependency by default, and so must be manually installed
   before using any of these emulation devices (e.g. ``pip install pygame``).
   See the install instructions in `luma.emulator  <http://github.com/rm-hull/luma.emulator>`_
   for further details.


