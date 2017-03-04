Installation
------------
.. warning::
   Ensure that the :ref:`pre-requisites` from the previous section
   have been performed, checked and tested before proceeding.

.. note:: The library has been tested against Python 2.7, 3.4 and 3.5.

   For **Python3** installation, substitute the following in the
   instructions below.

   * ``pip`` ⇒ ``pip3``,
   * ``python`` ⇒ ``python3``,
   * ``python-dev`` ⇒ ``python3-dev``,
   * ``python-pip`` ⇒ ``python3-pip``.

   It was *originally* tested with Raspbian on a rev.2 model B, with a vanilla
   kernel version 4.1.16+, and has subsequently been tested on Raspberry Pi
   model A, model B2 and 3B (Debian Jessie) and OrangePi Zero (Armbian Jessie).

From PyPI
^^^^^^^^^
Install the dependencies for library first with::

  $ sudo usermod -a -G spi,gpio pi
  $ sudo apt-get install python-dev python-pip
  $ sudo -i pip install --upgrade pip
  $ sudo apt-get purge python-pip

.. warning:: The default pip bundled with apt on Raspbian is really old, and can 
   cause components to not be installed properly. Please ensure that **pip 9.0.1** 
   is installed prior to continuing::
   
      $ pip --version
      pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)

Proceed to install latest version of the library directly from
`PyPI <https://pypi.python.org/pypi?:action=display&name=luma.led_matrix>`_::

  $ sudo -H pip install --upgrade luma.lcd

