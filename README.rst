
python-asiri
============

Overview
--------

python-asiri provides a Python interface similar to the Raspberry Pi GPIO libery for working
with GPIO in Asri, using a MCP230xx chip.


Features
--------

* Handling of digital inputs / outputs
* Support for builtin pullup resistors


API
---

All functionality is baked into the ``GPIO`` class.

Importing the ``GPIO`` object::

    from asiri import GPIO

Creating a ``GPIO`` instance for working with the MCP23017::

    my_gpio = GPIO(num_gpios=16)

Configuring a pin as output::

    my_gpio.setup(8, GPIO.OUT)

Setting an output pin to high::

    my_gpio.output(8, GPIO.HIGH)

Setting an output pin to low::

    my_gpio.output(8, GPIO.LOW)

Configuring a pin as input::

    my_gpio.setup(8, GPIO.IN)

Read the value of a given pin::

    value = my_gpio.input(8)

NOTE: The pin numbering is as follows (for the MCP23017): bank A: pins 0-7, bank B: ping 8-15.
On these examples pin 8 was used, that is, B0, or pin 0 from bank B.


ToDo
----

* Add support for interrupts
* Add functions to read all inputs from a given bank


License
-------

BSD, derived from Adafruit's helper libraries.

