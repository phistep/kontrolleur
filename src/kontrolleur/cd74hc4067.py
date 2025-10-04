from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from microcontroller import Pin


class CD74HC4067:
    CHANNELS = {
        0: [0, 0, 0, 0],
        1: [1, 0, 0, 0],
        2: [0, 1, 0, 0],
        3: [1, 1, 0, 0],
        4: [0, 0, 1, 0],
        5: [1, 0, 1, 0],
        6: [0, 1, 1, 0],
        7: [1, 1, 1, 0],
        8: [0, 0, 0, 1],
        9: [1, 0, 0, 1],
        10: [0, 1, 0, 1],
        11: [1, 1, 0, 1],
        12: [0, 0, 1, 1],
        13: [1, 0, 1, 1],
        14: [0, 1, 1, 1],
        15: [1, 1, 1, 1],
    }

    def __init__(self, s0: Pin, s1: Pin, s2: Pin, s3: Pin, sig: Pin):
        self.s0 = DigitalInOut(s0)
        self.s1 = DigitalInOut(s1)
        self.s2 = DigitalInOut(s2)
        self.s3 = DigitalInOut(s3)
        for pin in (self.s0, self.s1, self.s2, self.s3):
            pin.direction = Direction.OUTPUT

        self.sig = AnalogIn(sig)

    def read(self, channel: int):
        if not 0 <= channel <= 15:
            raise ValueError("'channel' must be betweeen 0 and 15")

        b0, b1, b2, b3 = self.CHANNELS[channel]
        self.s0.value = b0
        self.s1.value = b1
        self.s2.value = b2
        self.s3.value = b3

        return self.sig.value


# TODO instead return 4 custom AnalogIn pins where value can be read
