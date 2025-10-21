import board
from cd74hc4067 import AnalogMultiplexer
from kontrolleur import Kontrolleur
from kontrolleur.control import Potentiometer


def main():
    mp1_core = AnalogMultiplexer(
        s0=board.IO16,
        s1=board.IO15,
        s2=board.IO14,
        s3=board.IO12,
        sig=board.IO1,
        enable=board.IO11,
    )

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
