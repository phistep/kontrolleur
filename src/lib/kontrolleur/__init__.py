import time

import adafruit_midi
import usb_midi
from adafruit_midi.control_change import ControlChange

from .control import Control

MIDI_MAX = 127


class Kontrolleur:
    def __init__(self, controls: dict[int, Control], freq=120):
        self.controls = controls
        self._interval = 1 / freq

        midi_in, midi_out = usb_midi.ports
        self.midi = adafruit_midi.MIDI(midi_out=midi_out, out_channel=0)
        print("Default output MIDI channel:", self.midi.out_channel + 1)

    def run(self):
        while True:
            for cc, control in self.controls.items():
                if control.poll():
                    value = int(control.value * MIDI_MAX)
                    msg = ControlChange(cc, value)
                    print(cc, control, value, msg)
                    self.midi.send(msg)

                time.sleep(self._interval)
