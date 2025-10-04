import board
from cd74hc4067 import CD74HC4067
from kontrolleur import Kontrolleur
from kontrolleur.control import Potentiometer


def main():
    multiplexer = CD74HC4067(
        s0=board.IO38, s1=board.IO37, s2=board.IO36, s3=board.IO35, sig=board.IO1
    )

    kontrolleur = Kontrolleur(
        {
            0: Potentiometer(multiplexer[15]),
            1: Potentiometer(multiplexer[8]),
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
