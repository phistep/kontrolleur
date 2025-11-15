#!/bin/bash
set -o xtrace

function install_lib() {
    TARGET="/Volumes/CIRCUITPY/lib/$(basename $1)"
    [ ! -f "$TARGET" ] && wget "$1" --output-document "$TARGET"
}

circup install --requirement requirements.circup.txt
install_lib "https://raw.githubusercontent.com/WoolseyWorkshop/WoolseyWorkshop_CircuitPython_74HC165/refs/heads/main/wws_74hc165.py"
# circup install --upgrade ./src/{kontrolleur,cd74hc4067}
# cp -r src/ /Volumes/CIRCUITPY
rsync -Przh ./src/ /Volumes/CIRCUITPY
cp /Volumes/CIRCUITPY/dev.py /Volumes/CIRCUITPY/main.py
