# Kontrolleur

## ESP32-S3-Pico

- https://de.aliexpress.com/item/1005006444134211.html
- https://www.waveshare.com/wiki/ESP32-S3-Pico


### MicroPython

- https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

#### Flashing

- https://micropython.org/download/ESP32_GENERIC_S3/

```sh
uv venv
source .venv/bin/activate
uv pip install esptool
# or uv tool install esptool
```

- Connect directly to mac, not via hub.
- The default port `/dev/cu.usbmodem59720511361` did not work, but the second
  one it created did.

```sh
wget https://micropython.org/resources/firmware/ESP32_GENERIC_S3-20250809-v1.26.0.bin

esptool --chip esp32s3 --port /dev/cu.usbmodem21201 erase-flash
esptool --chip esp32s3 --port /dev/cu.usbmodem21201 --baud 460800 write-flash 0 ESP32_GENERIC_S3-20250809-v1.26.0.bin
```

Re-connect the chip after flashing.

#### REPL

- https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html

```sh
brew install picocom

picocom /dev/cu.usbmodem21201 -b115200
```

#### File Upload

- https://docs.micropython.org/en/latest/reference/mpremote.html

```sh
uv pip install mpremote
# or uv tool install mpremote for Zed Tasks

 # repl:
mpremote connect /dev/cu.usbmodem21201

mpremote run blink.py

mpremote cp blink.py :main.py
```

### CircuitPython

https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython

#### Flashing

- https://circuitpython.org/board/waveshare_esp32_s3_pico/

```sh
uv venv
source .venv/bin/activate
uv pip install esptool
# or uv tool install esptool
```

- Connect directly to mac, not via hub.
- The default port `/dev/cu.usbmodem59720511361` did not work, but the second
  one it created did.

```sh
wget https://adafruit-circuit-python.s3.amazonaws.com/bootloaders/esp32/waveshare_esp32_s3_pico/tinyuf2-waveshare_esp32_s3_pico-0.35.0-combined.bin

esptool --chip esp32s3 --port /dev/cu.usbmodem21201 erase-flash
esptool --chip esp32s3 --port /dev/cu.usbmodem21201 --baud 460800 write-flash 0 tinyuf2-waveshare_esp32_s3_pico-0.35.0-combined.bin
```

Re-connect the chip after flashing.

Double-press the `RESET` button: a new drive appears in the file manager:
`S3DKC1BOOT`.

Next download the CircuitPython distribution and copy it to the new drive

```sh
wget https://downloads.circuitpython.org/bin/waveshare_esp32_s3_pico/en_US/adafruit-circuitpython-waveshare_esp32_s3_pico-en_US-10.0.0.uf2
cp adafruit-circuitpython-waveshare_esp32_s3_pico-en_US-10.0.0.uf2 /Volumes/S3DKC1BOOT/
```

The lights flash, the drive gets unmounted and a new `CIRCUITPY` drive is
mounted.

```sh
ln -s /Volumes/CIRCUITPY ESP32-S3-Pico/circuitpython/CIRCUITPY
```

Now you can edit `CIRCUITPY/code.py`.

Connecting to the serial port

```sh
mpremote connect auto
```

will give you a REPL, after pressing Ctlr-D, the program is run and the output
is shown. After every file save, the program is automatically rerun.

#### MIDI

- https://docs.circuitpython.org/en/latest/shared-bindings/usb_midi/
- https://docs.circuitpython.org/projects/midi/en/latest/index.html

Download the library bundle

```sh
wget https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/download/20251003/adafruit-circuitpython-bundle-10.x-mpy-20251003.zip
unzip adafruit-circuitpython-bundle-10.x-mpy-20251003.zip
```

then install the `adafruit_midi` library

```sh
cp -r ESP32-S3-Pico/circuitpython/adafruit-circuitpython-bundle-10.x-mpy-20251003/lib/adafruit_midi /Volumes/CIRCUITPY/lib/
```

Also [enable `usb_midi` in `boot.py`](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial#midi-3096586):

```python
import usb_hid, usb_midi

# On some boards, we need to give up HID to accomodate MIDI.
usb_hid.disable()
usb_midi.enable()
```
