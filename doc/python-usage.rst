Python usage
------------
PCD8544 displays can be driven with python using the implementation in the
:py:class:`luma.lcd.device.pcd8544` class: usage is very simple if you have 
ever used `Pillow <https://pillow.readthedocs.io/en/latest/>`_ or PIL.

First, import and initialise the device:

.. code:: python

  from luma.core.serial import spi
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544

  serial = serial(port=0, device=0)

  device = pcd8544(serial)

The display device should now be configured for use. 
The class exposes a ``display()`` method
which takes an image with attributes consistent with the capabilities of the
device. However, for most cases, for drawing text and graphics primitives, the
canvas class should be used as follows:

.. code:: python

  with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="white", fill="black")
      draw.text((30, 40), "Hello World", fill="white")

The :class:`luma.core.render.canvas` class automatically creates an
:mod:`PIL.ImageDraw` object of the correct dimensions and bit depth suitable
for the device, so you may then call the usual Pillow methods to draw onto the
canvas.

As soon as the with scope is ended, the resultant image is automatically
flushed to the device's display memory and the :mod:`PIL.ImageDraw` object is
garbage collected.

Color Model
^^^^^^^^^^^
Any of the standard :mod:`PIL.ImageColor` color formats may be used, but since
the PCD8544 LCD is monochrome, only the HTML color names
``"black"`` and ``"white"`` values should really be used; in fact, by default,
any value *other* than black is treated as white. The :py:class:`luma.core.canvas` object
does have a ``dither`` flag which if set to True, will convert color drawings
to a dithered monochrome effect (see the *3d_box.py* example, below).

.. code:: python

  with canvas(device, dither=True) as draw:
      draw.rectangle((10, 10, 30, 30), outline="white", fill="red")

Landscape / Portrait Orientation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By default the display will be oriented in landscape mode (84x48 pixels).
Should you have an application that requires the display to be mounted in a
portrait aspect, then add a ``rotate=N`` parameter when creating the device:

.. code:: python

  from luma.core.serial import i2c
  from luma.core.render import canvas
  from luma.lcd.device import pcd8544

  serial = serial(port=0, device=0)
  device = pcd8544(serial, rotate=1)

  # Box and text rendered in portrait mode
  with canvas(device) as draw:
      draw.rectangle(device.bounding_box, outline="white", fill="black")
      draw.text((10, 40), "Hello World", fill="white")

*N* should be a value of 0, 1, 2 or 3 only, where 0 is no rotation, 1 is
rotate 90° clockwise, 2 is 180° rotation and 3 represents 270° rotation.

The ``device.size``, ``device.width`` and ``device.height`` properties reflect
the rotated dimensions rather than the physical dimensions.

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
There are various display emulators available for running code against, for debugging
and screen capture functionality:

* The :py:class:`luma.core.emulator.capture` device will persist a numbered PNG file to
  disk every time its ``display`` method is called.

* The :py:class:`luma.core.emulator.gifanim` device will record every image when its ``display``
  method is called, and on program exit (or Ctrl-C), will assemble the images into an
  animated GIF.

* The :py:class:`luma.core.emulator.pygame` device uses the :py:mod:`pygame` library to
  render the displayed image to a pygame display surface. 

Invoke the demos with::

  $ python examples/clock.py -d capture

or::

  $ python examples/clock.py -d pygame
  
.. note::
   *Pygame* is required to use any of the emulated devices, but it is **NOT**
   installed as a dependency by default, and so must be manually installed
   before using any of these emulation devices.
