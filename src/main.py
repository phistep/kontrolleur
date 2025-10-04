import board
from cd74hc4067 import CD74HC4067
from digitalio import DigitalInOut, Direction, Pull
from kontrolleur import Kontrolleur
from kontrolleur.control import Distance, Joystick, Potentiometer


def main():
    io41 = DigitalInOut(board.IO41)
    io41.direction = Direction.INPUT
    io41.pull = Pull.UP

    io1_multi = CD74HC4067(
        s0=board.IO38, s1=board.IO37, s2=board.IO36, s3=board.IO35, sig=board.IO1
    )

    kontrolleur = Kontrolleur(
        {
            0: Potentiometer(io1_multi[15]),
            1: Potentiometer(io1_multi[8]),
            (2, 3, 4): Joystick(io1_multi[7], io1_multi[6], io41),
            5: Distance(trig=board.IO17, echo=board.IO16),
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
