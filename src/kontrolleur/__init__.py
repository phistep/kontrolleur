import time

import adafruit_midi
import board
import usb_midi
from adafruit_midi.control_change import ControlChange

from .cd74hc4067 import CD74HC4067

ANALOG_MAX = 65535
MIDI_MAX = 127


class Kontrolleur:
    def __init__(self):
        midi_in, midi_out = usb_midi.ports
        self.midi = adafruit_midi.MIDI(midi_out=midi_out, out_channel=0)
        print("Default output MIDI channel:", self.midi.out_channel + 1)

        multiplexer = CD74HC4067(
            s0=board.IO38, s1=board.IO37, s2=board.IO36, s3=board.IO35, sig=board.IO1
        )

        self.pots = [multiplexer[15], multiplexer[8]]
        self._values = [None, None]

    def run(self):
        while True:
            for n, pot in enumerate(self.pots):
                pot_value = pot.value
                value = int(pot_value / ANALOG_MAX * MIDI_MAX)
                if value != self._values[n]:
                    self._values[n] = value
                    msg = ControlChange(n, value)
                    print(n, pot, pot_value, msg)
                    self.midi.send(msg)

                time.sleep(1e-3)
