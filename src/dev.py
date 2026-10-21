import board
from digitalio import DigitalInOut, Direction, Pull

from cd74hc4067 import AnalogMultiplexer
from kontrolleur import Kontrolleur
from kontrolleur.control import (
    Button,
    Distance,
    Encoder,
    Joystick,
    Potentiometer,
    Toggle,
)
from wws_74hc165 import ShiftRegister74HC165


def main():
    spi = board.SPI()  # MISO=IO37 SCK=IO36, MOSI=IO35

    io41 = DigitalInOut(board.IO41)
    io41.direction = Direction.INPUT
    io41.pull = Pull.UP

    io1_multi = AnalogMultiplexer(
        s0=board.IO16, s1=board.IO15, s2=board.IO14, s3=board.IO13, sig=board.IO1
    )

    io34_multi = ShiftRegister74HC165(spi, DigitalInOut(board.IO40), polarity=1)

    # -- 8< --

    from time import sleep

    while True:
        print([int(io34_multi.get_pin(pin).value) for pin in range(8)])
        sleep(0.01)

    # -- >8 --

    # from adafruit_74hc595 import ShiftRegister74HC595
    # io42_multi = ShiftRegister74HC595(spi, DigitalInOut(board.IO42))
    # io42_multi.get_pin(7)

    kontrolleur = Kontrolleur(
        {
            # 0: Toggle(board.IO33),
            # 1: Potentiometer(io1_multi[9]),
            # (2, 3, 4): Joystick(io1_multi[7], io1_multi[8], board.IO8),
            # 5: Distance(trig=board.IO18, echo=board.IO17, max_=50),
            (6, 7, 8): Encoder(
                a=io34_multi.get_pin(0),
                b=io34_multi.get_pin(1),
                btn=io34_multi.get_pin(2),
                toggle=True,
            ),
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
