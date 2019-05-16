====================
pylibmodbus Rpi GPIO
====================

Original code: https://github.com/stephane/pylibmodbus

Changes: Added support to use Raspberry Pi GPIO pins to toggle a Drive Enable / ~ Read Enable signal for RS485 devices that don't have a hardware TX Enable signal. 

First install libmodbus from this branch: https://github.com/dhruvvyas90/libmodbus

Configure, compile and install with:
    
    $ ./autogen.sh && ./configure --prefix=/usr && make && sudo make install

Then clone and install pylibmodbus with GPIO support:
    
    $ sudo python setup.py install
    
Required packages:

- python-dev and libffi-dev (these can be installed with pip)
- libmodbus (from https://github.com/dhruvvyas90/libmodbus do NOT install with apt-get)
- libmodbus-dev (original package, it can be installed with sudo aptg-get install libmodbus-dev)

Licensed under BSD 3-Clause (see LICENSE file for details).

Tests
-----
See test.py for a Modbus client basic example
