import board
from cd74hc4067 import CD74HC4067
from digitalio import DigitalInOut, Direction, Pull
from kontrolleur import Kontrolleur
from kontrolleur.control import (
    Button,
    Distance,
    Encoder,
    Joystick,
    Potentiometer,
    Toggle,
)


def main():
    # TODO move into CD74GC4067 driver
    mp1_core = CD74HC4067(
        s0=board.IO16, s1=board.IO15, s2=board.IO14, s3=board.IO12, sig=board.IO1
    )
    mp1_core_enable = DigitalInOut(board.IO11)
    mp1_core_enable.direction = Direction.OUTPUT
    mp1_core_enable.value = False

    kontrolleur = Kontrolleur(
        {
            1: Potentiometer(mp1_core[12]),
            2: Potentiometer(mp1_core[13]),
            3: Potentiometer(mp1_core[14]),
            4: Potentiometer(mp1_core[15]),
        }
    )

    kontrolleur.run()


def main_dev():
    io41 = DigitalInOut(board.IO41)
    io41.direction = Direction.INPUT
    io41.pull = Pull.UP

    io1_multi = CD74HC4067(
        s0=board.IO16, s1=board.IO15, s2=board.IO14, s3=board.IO13, sig=board.IO1
    )

    # TODO 74HC595 is SIPO, we want 74HC165 PISO woolseyworkshop_circuitpython_74hc165
    # from adafruit_74hc595 import ShiftRegister74HC595
    # spi = board.SPI()  # SCK=IO36, MOSI=IO35
    # io42_multi = ShiftRegister74HC595(spi, DigitalInOut(board.IO42))
    # io42_multi.get_pin(7)),

    kontrolleur = Kontrolleur(
        {
            # 0: Toggle(board.IO33),
            # 1: Potentiometer(io1_multi[9]),
            # (2, 3, 4): Joystick(io1_multi[7], io1_multi[8], board.IO8),
            5: Distance(trig=board.IO18, echo=board.IO17, max_=50),
            # (6, 7, 8): Encoder(a=board.IO39, b=board.IO40, btn=board.IO38, toggle=True),
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
