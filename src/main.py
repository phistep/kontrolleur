import board
from digitalio import DigitalInOut

from cd74hc4067 import AnalogMultiplexer
from kontrolleur import Kontrolleur
from kontrolleur.control import Button, Potentiometer
from wws_74hc165 import ShiftRegister74HC165


def main():
    spi = board.SPI()  # MISO=IO37 SCK=IO36, MOSI=IO35

    mp1_core = AnalogMultiplexer(
        s0=board.IO16,
        s1=board.IO15,
        s2=board.IO14,
        s3=board.IO12,
        sig=board.IO1,
        enable=board.IO11,
    )

    srin1_core = ShiftRegister74HC165(spi, DigitalInOut(board.IO33), polarity=1)

    #  +-| CORE |------------------------+
    #  |                   (enc)   [RST] |
    #  |                                 |
    #  | (pot1)  (pot2)   [btn1]  [btn2] |
    #  |                                 |
    #  | [btn3]  [btn4]   (pot3)  (pot4) |
    #  +---------------------------------+
    #          +-| JOY |---------+
    #          | (joy1)   (joy2) |
    #          +-----------------+

    kontrolleur = Kontrolleur(
        {
            # Potentiometer
            1: Potentiometer(mp1_core[12]),  # pot1
            2: Potentiometer(mp1_core[13]),  # pot2
            3: Potentiometer(mp1_core[14]),  # pot4
            4: Potentiometer(mp1_core[15]),  # pot3
            #  System
            # TODO need to write own encoder library that supports shift register input
            # (6, 7, 8): Encoder(
            #     a=srin1_core.get_pin(1),
            #     b=srin1_core.get_pin(2),
            #     btn=srin1_core.get_pin(3),
            #     toggle=True,
            # ),
            5: Button(srin1_core.get_pin(0)),  # reset
            6: Button(srin1_core.get_pin(1)),  # enc A
            7: Button(srin1_core.get_pin(2)),  # enc B
            8: Button(srin1_core.get_pin(3)),  # enc button8
            # Buttons
            9: Button(srin1_core.get_pin(4)),  # button2
            10: Button(srin1_core.get_pin(5)),  # button3
            11: Button(srin1_core.get_pin(6)),  # button4
            12: Button(srin1_core.get_pin(7)),  # button1
        }
    )

    kontrolleur.run()


if __name__ == "__main__":
    main()
