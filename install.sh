#!/bin/bash
set -o xtrace

circup install --requirement requirements.circup.txt
# circup install --upgrade ./src/{kontrolleur,cd74hc4067}
# cp -r src/ /Volumes/CIRCUITPY
rsync -Przh ./src/ /Volumes/CIRCUITPY
cp /Volumes/CIRCUITPY/dev.py /Volumes/CIRCUITPY/main.py
