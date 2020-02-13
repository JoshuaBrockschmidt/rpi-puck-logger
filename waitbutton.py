#!/usr/bin/env python3
"""
Waits for a button press, then terminates.
"""

# GPIO pin for detecting button input
# Feel free to change this
PIN = 18


import RPi.GPIO as GPIO
import signal
import sys

def catchTerm(signal, frame):
    # Called when SIGTERM is detected
    sys.exit(0)

def main():
    signal.signal(signal.SIGTERM, catchTerm)
    signal.signal(signal.SIGINT, catchTerm)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        btnInp = GPIO.input(PIN)
        if not btnInp:
            print("Button press detected")
            break

if __name__ == "__main__":
    main()
