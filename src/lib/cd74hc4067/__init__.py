from analogio import AnalogIn
from digitalio import DigitalInOut, Direction
from microcontroller import Pin

# http://adam-meyer.com/arduino/CD74HC4067
# https://38-3d.co.uk/blogs/blog/using-the-cd74hc4067-multiplexer-with-the-raspberry-pi
# https://github.com/gsampallo/micropython_examples/blob/master/74HC4067/multiplexor.py

# TODO reference count in parent mutliplexer object, cleanup once all children
#      are cleaned up
# TODO enable pin support
# TODO address as `bytes`

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


def CD74HC4067(s0: Pin, s1: Pin, s2: Pin, s3: Pin, sig: Pin):
    pin_s0 = DigitalInOut(s0)
    pin_s1 = DigitalInOut(s1)
    pin_s2 = DigitalInOut(s2)
    pin_s3 = DigitalInOut(s3)
    for pin in (pin_s0, pin_s1, pin_s2, pin_s3):
        pin.direction = Direction.OUTPUT

    pin_sig = AnalogIn(sig)

    return [
        AnalogInMultiplexed(pin_s0, pin_s1, pin_s2, pin_s3, pin_sig, channel)
        for channel in CHANNELS
    ]


class AnalogInMultiplexed:
    def __init__(
        self,
        s0: DigitalInOut,
        s1: DigitalInOut,
        s2: DigitalInOut,
        s3: DigitalInOut,
        sig: AnalogIn,
        channel: int,
    ):
        if not 0 <= channel <= 15:
            raise ValueError("'channel' must be betweeen 0 and 15")
        self.channel = channel

        self.s0 = s0
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.sig = sig
        self.b0, self.b1, self.b2, self.b3 = CHANNELS[channel]

    def __str__(self):
        return f"C{self.channel}"

    def __repr__(self):
        return (
            f"<AnalogInMultiplexed"
            f" s0={self.s0} s1={self.s1} s2={self.s2} s3={self.s3}"
            f" sig={self.sig} channel={self.channel}"
            f">"
        )

    @property
    def value(self):
        self.s0.value = self.b0
        self.s1.value = self.b1
        self.s2.value = self.b2
        self.s3.value = self.b3
        return self.sig.value
