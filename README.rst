Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython_i2c_encoder/badge/?version=latest
    :target: https://circuitpython_i2c_encoder.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://travis-ci.com/schlafsack/CircuitPython_I2CEncoder.svg?branch=master
    :target: https://travis-ci.com/schlafsack/CircuitPython_I2CEncoder
    :alt: Build Status

A CircuitPython driver for the DuPPa I2C Encoder v2.1 board.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://github.com/adafruit/Adafruit_CircuitPython_Bundle>`_.

Usage Example
=============

.. todo:: Add a quick, simple example. It and other examples should live in the examples folder and be included in docs/examples.rst.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/schlafsack/CircuitPython_I2CEncoder/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Sphinx documentation
-----------------------

Sphinx is used to build the documentation based on rST files and comments in the code. First,
install dependencies (feel free to reuse the virtual environment from above):

.. code-block:: shell

    python3 -m venv .env
    source .env/bin/activate
    pip install Sphinx sphinx-rtd-theme

Now, once you have the virtual environment activated:

.. code-block:: shell

    cd docs
    sphinx-build -E -W -b html . _build/html

This will output the documentation to ``docs/_build/html``. Open the index.html in your browser to
view them. It will also (due to -W) error out on any warning like Travis will. This is a good way to
locally verify it will pass.
