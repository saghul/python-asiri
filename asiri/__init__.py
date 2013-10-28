
from .mcp230xx import MCP230XX

__all__ = ['GPIO']


class GPIO(object):
    """
    RPi.GPIO-like interface for MCP23017 and MCP23008
    """

    OUT = MCP230XX.OUTPUT
    IN = MCP230XX.INPUT

    def __init__(self, num_gpios=16, busnum=1, address=0x20):
        self._chip = MCP230XX(busnum, address, num_gpios)

    def setup(self, pin, mode):
        self._chip.config(pin, mode)

    def input(self, pin):
        return self._chip.input(pin)

    def output(self, pin, value):
        self._chip.output(pin, value)

    def pullup(self, pin, value):
        self._chip.pullup(pin, value)

    def cleanup(self):
        try:
            self._chip.reset()
        except Exception:
            pass

