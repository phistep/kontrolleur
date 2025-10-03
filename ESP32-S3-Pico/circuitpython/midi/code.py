import random
import time

import adafruit_midi
import usb_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend

print("ports:", usb_midi.ports)

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

print("Midi test")

print("Default output MIDI channel:", midi.out_channel + 1)

while True:
    for msg in [
        NoteOn(44, 120),  # G sharp 2nd octave
        PitchBend(random.randint(0, 16383)),
        [NoteOff("G#2", 120), ControlChange(3, 44)],
    ]:
        midi.send(msg)
        print(msg)
        time.sleep(0.25)
