# The MIT License (MIT)
#
# Copyright (c) 2019 Tom Greasley
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`circuitpython_i2c_encoder`
================================================================================

A CircuitPython driver for the DuPPa I2C Encoder v2.1 board.


* Author(s): Tom Greasley

Implementation Notes
--------------------

**Hardware:**

   `DaPPa I2C Encoder v2.1 <https://www.duppa.net/i2c-encoder-v2-1/>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
* Adafruit's Register library:
  https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

import sys

from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_register import i2c_bit, i2c_bits, i2c_struct
from micropython import const

# pylint: disable=wrong-import-position
try:
    lib_index = sys.path.index("/lib")  # pylint: disable=invalid-name
    if lib_index < sys.path.index(".frozen"):
        # Prefer frozen modules over those in /lib.
        sys.path.insert(lib_index, ".frozen")
except ValueError:
    # Don't change sys.path if it doesn't contain "lib" or ".frozen".
    pass

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/schlafsack/CircuitPython_I2CEncoder.git"

# Register addresses:
# pylint: disable=bad-whitespace
_REG_GCONF = const(0x00)
_REG_GCONF2 = const(0x30)
_REG_GP1CONF = const(0x01)
_REG_GP2CONF = const(0x02)
_REG_GP3CONF = const(0x03)
_REG_INTCONF = const(0x03)
_REG_ESTATUS = const(0x05)
_REG_I2STATUS = const(0x06)
_REG_FSTATUS = const(0x07)
_REG_CVAL = const(0x08)
_REG_CMAX = const(0x0C)
_REG_CMIN = const(0x10)
_REG_ISTEP = const(0x14)
_REG_RLED = const(0x18)
_REG_GLED = const(0x19)
_REG_BLED = const(0x1A)
_REG_GP1 = const(0x1B)
_REG_GP2 = const(0x1C)
_REG_GP3 = const(0x1D)
_REG_ANTBOUNC = const(0x1E)
_REG_DPPERIOD = const(0x1F)
_REG_FADERGB = const(0x20)
_REG_FADEGP = const(0x21)
_REG_GAMRLED = const(0x27)
_REG_GAMGLED = const(0x28)
_REG_GAMBLED = const(0x29)
_REG_GAMMAGP1 = const(0x2A)
_REG_GAMMAGP2 = const(0x2B)
_REG_GAMMAGP3 = const(0x2C)
_REG_IDCODE = const(0x70)
_REG_VERSION = const(0x71)
_REG_EEPROM = const(0x80)


# noinspection PyTypeChecker
class Encoder:

    def __init__(self, i2c, device_address):
        self.i2c_device = I2CDevice(i2c, device_address)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    # GCONF
    gconf_dtype = i2c_bit.RWBit(_REG_GCONF, 0x00)
    gconf_wrape = i2c_bit.RWBit(_REG_GCONF, 0x01)
    gconf_dire = i2c_bit.RWBit(_REG_GCONF, 0x02)
    gconf_ipud = i2c_bit.RWBit(_REG_GCONF, 0x03)
    gconf_rmod = i2c_bit.RWBit(_REG_GCONF, 0x04)
    gconf_etype = i2c_bit.RWBit(_REG_GCONF, 0x05)
    gconf_mbank = i2c_bit.RWBit(_REG_GCONF, 0x06)
    gconf_rst = i2c_bit.RWBit(_REG_GCONF, 0x07)

    # GCONF2
    gconf2_cksrc = i2c_bit.RWBit(_REG_GCONF, 0x00)
    gconf2_relmod = i2c_bit.RWBit(_REG_GCONF, 0x01)

    # GP1CONF
    gp1conf = i2c_bits.RWBits(8, _REG_GP1CONF, 0x00)
    gp1conf_mode = i2c_bits.RWBits(2, _REG_GP1CONF, 0x00)
    gp1conf_pul = i2c_bit.RWBit(_REG_GP1CONF, 0x02)
    gp1conf_int = i2c_bits.RWBits(2, _REG_GP1CONF, 0x03)

    # GP2CONF
    gp2conf = i2c_bits.RWBits(8, _REG_GP2CONF, 0x00)
    gp2conf_mode = i2c_bits.RWBits(2, _REG_GP2CONF, 0x00)
    gp2conf_pul = i2c_bit.RWBit(_REG_GP2CONF, 0x02)
    gp2conf_int = i2c_bits.RWBits(2, _REG_GP2CONF, 0x03)

    # GP3CONF
    gp3conf = i2c_bits.RWBits(8, _REG_GP3CONF, 0x00)
    gp3conf_mode = i2c_bits.RWBits(2, _REG_GP3CONF, 0x00)
    gp3conf_pul = i2c_bit.RWBit(_REG_GP3CONF, 0x02)
    gp3conf_int = i2c_bits.RWBits(2, _REG_GP3CONF, 0x03)

    # INTCONF
    intconf_ipushr = i2c_bit.RWBit(_REG_INTCONF, 0x00)
    intconf_ipushp = i2c_bit.RWBit(_REG_INTCONF, 0x01)
    intconf_ipushd = i2c_bit.RWBit(_REG_INTCONF, 0x02)
    intconf_irinc = i2c_bit.RWBit(_REG_INTCONF, 0x03)
    intconf_irdec = i2c_bit.RWBit(_REG_INTCONF, 0x04)
    intconf_irmax = i2c_bit.RWBit(_REG_INTCONF, 0x05)
    intconf_irmin = i2c_bit.RWBit(_REG_INTCONF, 0x06)
    intconf_int2 = i2c_bit.RWBit(_REG_INTCONF, 0x07)

    # ESTATUS - TODO: Break this into a set of flags
    estatus = i2c_bits.ROBits(8, _REG_ESTATUS, 0x00)

    # I2STATUS - TODO: Break this into a set of flags
    i2status = i2c_bits.ROBits(8, _REG_I2STATUS, 0x00)

    # FSTATUS - TODO: Break this into a set of flags
    fstatus = i2c_bits.ROBits(8, _REG_FSTATUS, 0x00)

    # CVAL FLOAT
    cval_float = i2c_struct.UnaryStruct(_REG_CVAL, ">f")

    # CVAL LONG
    cval_long = i2c_struct.UnaryStruct(_REG_CVAL, ">l")

    # CMAX FLOAT
    cmax_float = i2c_struct.UnaryStruct(_REG_CMAX, ">f")

    # CMAX LONG
    cmax_long = i2c_struct.UnaryStruct(_REG_CMAX, ">l")

    # CMIN FLOAT
    cmin_float = i2c_struct.UnaryStruct(_REG_CMIN, ">f")

    # CMIN LONG
    cmin_long = i2c_struct.UnaryStruct(_REG_CMIN, ">l")

    # ISTEP FLOAT
    istep_float = i2c_struct.UnaryStruct(_REG_ISTEP, ">f")

    # ISTEP INT
    istep_long = i2c_struct.UnaryStruct(_REG_ISTEP, ">l")

    # R/G/B LED
    rled = i2c_bits.RWBits(8, _REG_RLED, 0x00)
    gled = i2c_bits.RWBits(8, _REG_GLED, 0x00)
    bled = i2c_bits.RWBits(8, _REG_BLED, 0x00)

    # GP 1/2/3
    gp1 = i2c_bits.RWBits(8, _REG_GP1, 0x00)
    gp2 = i2c_bits.RWBits(8, _REG_GP2, 0x00)
    gp3 = i2c_bits.RWBits(8, _REG_GP3, 0x00)

    # ANTI BOUNCE
    antbounc = i2c_bits.RWBits(8, _REG_ANTBOUNC, 0x00)

    # DP PERIOD
    dpperiod = i2c_bits.RWBits(8, _REG_DPPERIOD, 0x00)

    # FADE RGB
    fadergb = i2c_bits.RWBits(8, _REG_FADERGB, 0x00)

    # FADE GP
    fadegp = i2c_bits.RWBits(8, _REG_FADEGP, 0x00)

    # GAMMA R/G/B
    gamrled = i2c_bits.RWBits(3, _REG_GAMRLED, 0x00)
    gamgled = i2c_bits.RWBits(3, _REG_GAMGLED, 0x00)
    gambled = i2c_bits.RWBits(3, _REG_GAMBLED, 0x00)

    # GAMMA GP 1/2/3
    gammagp1 = i2c_bits.RWBits(3, _REG_GAMMAGP1, 0x00)
    gammagp2 = i2c_bits.RWBits(3, _REG_GAMMAGP2, 0x00)
    gammagp3 = i2c_bits.RWBits(3, _REG_GAMMAGP3, 0x00)

    # ID CODE
    idcode = i2c_bits.ROBits(8, _REG_IDCODE, 0x00)

    # VERSION
    version = i2c_bits.ROBits(8, _REG_VERSION, 0x00)

    # EEPROM
    eeprom = i2c_bits.ROBits(1024, _REG_EEPROM, 0x00, register_width=128)
