# Kontrolleur

## ESP32-S3-Pico

- https://de.aliexpress.com/item/1005006444134211.html
- https://www.waveshare.com/wiki/ESP32-S3-Pico#Flash_Firmware
- https://docs.micropython.org/en/latest/esp32/tutorial/intro.html


### MicroPython

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
