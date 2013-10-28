
from asiri import GPIO
from time import sleep


LED = 8

gpio = GPIO(num_gpios=16)
gpio.setup(LED, GPIO.OUT)

state = False
try:
    while True:
        gpio.output(LED, state)
        sleep(1)
        state = not state
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()

