
from asiri import GPIO
from time import sleep


LED = 8

gpio = GPIO(num_gpios=16)
gpio.setup(LED, GPIO.OUT)

try:
    while True:
        gpio.output(LED, GPIO.LOW)
        sleep(1)
        gpio.output(LED, GPIO.HIGH)
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    gpio.cleanup()

