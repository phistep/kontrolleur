from time import sleep

import board
import digitalio

led = digitalio.DigitalInOut(board.IO40)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = not led.value
    print(led.value)
    sleep(1)
