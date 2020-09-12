Installation
------------
.. warning::
   Ensure that the :ref:`pre-requisites` from the previous section
   have been performed, checked and tested before proceeding.

.. note:: The library has been tested against Python 3.5, 3.6, 3.7 and 3.8.

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

I
Installing from PyPI
^^^^^^^^^^^^^^^^^^^^
First, install the dependencies for the library with::

  $ sudo usermod -a -G spi,gpio pi
  $ sudo apt-get install python-dev python-pip

And finally, install the latest version of the library directly from
`PyPI <https://pypi.python.org/pypi?:action=display&name=luma.lcd>`__
with::

  $ sudo -H pip install --upgrade luma.lcd

.. warning:: The default pip bundled with apt on Raspbian Jessie is really old,
  and can cause components to not be installed properly. Please ensure that **pip 9.0.1** is installed prior to continuing::

      $ pip --version
      pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)
