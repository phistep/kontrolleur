from time import sleep

from machine import Pin

led = Pin(40, Pin.OUT)

if __name__ == "__main__":
    while True:
        led.value(not led.value())
        sleep(0.1)
