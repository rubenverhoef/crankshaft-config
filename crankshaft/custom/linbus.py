#!/usr/bin/env python

import serial
import binascii
import keyboard

buttons = {
    # "00" : '',              # Number 0
    # "01" : '',              # Number 1
    # "02" : '',              # Number 2
    # "03" : '',              # Number 3
    # "04" : '',              # Number 4
    # "05" : '',              # Number 5
    # "06" : '',              # Number 6
    # "07" : '',              # Number 7
    # "08" : '',              # Number 8
    # "09" : '',              # Number 9
    "0a" : 'P',             # Star (*)          | Phone
    "0b" : 'escape',        # Hashtag (#)       | Esc
    # "18" : '',              # Music
    "28" : 'return',        # OK                | Enter
    "29" : 'num 1',         # Left              | Wheel Left
    "2a" : 'num 2',         # Right             | Wheel Right
    "2b" : 'up arrow',      # Up                | UP
    "2c" : 'down arrow',    # Down              | Down
    "32" : 'V',             # Previous          | Previous
    "33" : 'N',             # Next              | Next
    # "36" : '',              # TA
    "3c" : 'left arrow',    # Button Left/Left  | Hamburger Menu
    "3d" : 'B',             # Button Left/Right | Play/Pause
    "3e" : 'H',             # Button Right/Left | Home
    "3f" : 'M',             # Button Right/Right| Voice Command
}

value = {
    "00" : 'press',
    "01" : 'holding',
    "02" : 'release'
}

ser = serial.Serial('/dev/ttyAMA0', 9600)  # open serial port
while 1:
    if binascii.hexlify(ser.read(1)) == "55":   # if Start byte is read
        if binascii.hexlify(ser.read(1)) == "50": # if Node is 0x11 == 0x50 ??
            data = binascii.hexlify(ser.read(1)) # Read Button data byte
            if data in buttons:
                binascii.hexlify(ser.read(3)) # The 3 next bytes are not necessary, throw them away
                status = binascii.hexlify(ser.read(1))  # Read Status byte
                if value.get(status, 'release') == 'press':
                    keyboard.press(buttons[data])
                elif value.get(status, 'release') == 'release':
                    keyboard.release(buttons[data])
