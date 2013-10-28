
from __future__ import print_function

from asiri import GPIO
from time import sleep


BTN = 9

gpio = GPIO(num_gpios=16)
gpio.setup(BTN, GPIO.IN)

try:
    prev_input = 0
    while True:
        input = gpio.input(BTN)
        if not prev_input and input:
            print("Button pressed!")
        prev_input = input
        sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()

