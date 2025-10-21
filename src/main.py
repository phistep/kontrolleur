import board
from cd74hc4067 import CD74HC4067
from digitalio import DigitalInOut, Direction
from kontrolleur import Kontrolleur
from kontrolleur.control import Potentiometer


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


if __name__ == "__main__":
    main()
