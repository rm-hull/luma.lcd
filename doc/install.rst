Installation
------------
.. warning::
   Ensure that the :ref:`Pre-requisites` from the Hardware section
   have been performed, checked and tested before proceeding.

.. note:: The library has been tested against Python 3.5, 3.6, 3.7 and 3.8.

   It was *originally* tested with Raspbian on a rev.2 model B, with a vanilla
   kernel version 4.1.16+, and has subsequently been tested on Raspberry Pi
   (both Raspbian Jessie and Stretch) models A, B2, 3B, Zero, Zero W and
   OrangePi Zero (Armbian Jessie).

Installing from PyPI
^^^^^^^^^^^^^^^^^^^^
First, install the dependencies for the library with::

  $ sudo usermod -a -G spi,gpio pi
  $ sudo apt-get install python-dev python-pip

And finally, install the latest version of the library directly from
`PyPI <https://pypi.python.org/pypi?:action=display&name=luma.lcd>`__
with::

  $ sudo -H pip install --upgrade luma.lcd
