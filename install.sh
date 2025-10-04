#!/bin/bash
set -o xtrace

circup install --requirement requirements.circup.txt
circup install --upgrade ./src/kontrolleur
cp src/{boot.py,main.py} /Volumes/CIRCUITPY
