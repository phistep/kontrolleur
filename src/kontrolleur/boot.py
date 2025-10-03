import usb_hid
import usb_midi

# need to give up HID to accomodate MIDI
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#midi-3096586
usb_hid.disable()
usb_midi.enable()
