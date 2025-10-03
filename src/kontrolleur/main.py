import time

import adafruit_midi
import board
import usb_midi
from adafruit_midi.control_change import ControlChange
from analogio import AnalogIn

ANALOG_MAX = 65535
MIDI_MAX = 127

midi_in, midi_out = usb_midi.ports
midi = adafruit_midi.MIDI(midi_out=midi_out, out_channel=0)
print("Default output MIDI channel:", midi.out_channel + 1)

potentiometer = AnalogIn(board.IO1)
_value = None

while True:
    potentiometer_value = potentiometer.value
    value = int(potentiometer_value / ANALOG_MAX * MIDI_MAX)
    if value != _value:
        _value = value
        msg = ControlChange(1, value)
        print(potentiometer_value, msg)
        midi.send(msg)

    time.sleep(1e-3)
