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

    io6_multi = AnalogMultiplexer(
        s0=board.IO16,
        s1=board.IO15,
        s2=board.IO14,
        s3=board.IO13,
        sig=board.IO6,
    )

    io40_shift_in = ShiftRegister74HC165(spi, DigitalInOut(board.IO40), polarity=1)

    # from adafruit_74hc595 import ShiftRegister74HC595
    # io42_multi = ShiftRegister74HC595(spi, DigitalInOut(board.IO42))
    # io42_multi.get_pin(7)

    kontrolleur = Kontrolleur(
        {
            0: Toggle(io40_shift_in.get_pin(7)),
            1: Potentiometer(io6_multi[7]),
            (2, 3, 4): Joystick(
                x=io6_multi[10],
                y=io6_multi[9],
                sw=io40_shift_in.get_pin(4),
                tolerance=300,
            ),
            # TODO works, but check on shift registers. slows everything else down
            # 5: Distance(trig=board.IO18, echo=board.IO17, max_=50),
            (6, 7, 8): Encoder(
                # TODO need to write own encoder library that supports shift register input
                # a=io40_shift_in.get_pin(0),
                # b=io40_shift_in.get_pin(1),
                a=board.IO1,
                b=board.IO2,
                # TODO button not working?
                btn=io40_shift_in.get_pin(6),
                toggle=True,
            ),
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
