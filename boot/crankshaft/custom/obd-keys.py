#!/usr/bin/python3

import os, sys, math, time

sys.path.append(os.path.join(os.path.dirname(__file__), "keyboard"))
sys.path.append(os.path.join(os.path.dirname(__file__), "obd"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pint"))

import keyboard # import for emulating keyboard presses

import obd #import for reading/sending obd messages
from obd import OBDCommand
from obd.protocols import ECU
from obd.utils import bytes_to_int
import obd.decoders as d

# # 223B541 response: 623B5400000000
# REV_GEAR	= 7 # 623B5400010000

# # 2271511 response: 62715100000000
# LIGHT		= 12 # 62715100080000
# LIGHT_1		= 11 # 62715100100000
# LIGHT_2		= 9  # 62715100400000

# HAND_BRAKE  = 0

class Button:
    def __init__(self, bitSelect, isPressing, button):
        self.bitSelect  = bitSelect
        self.isPressing = False
        self.button     = button

    def press(self):
        keyboard.press(self.button)

    def release(self):
        keyboard.release(self.button)

# 22833C1 response: 62833C00
swCMD     = b"22833C"
swHeader  = b'0007A5'
swBytes   = 1
swBase    = 0x62833C00
# swVolUp   = Button((0x62833C80 ^ swBase), False, "H")
# swVolDown = Button((0x62833C40 ^ swBase), False, "H")
swVoice   = Button((0x62833C08 ^ swBase), False, "M")      # Voice Command
swNext    = Button((0x62833C04 ^ swBase), False, "N")      # Next
swPrev    = Button((0x62833C02 ^ swBase), False, "V")      # Previous
swM       = Button((0x62833C01 ^ swBase), False, "return") # Enter

swButtons   = [swVoice, swNext, swPrev, swM]

sw = OBDCommand("Steering Wheel",
               "Decode SW Commands",
               swCMD,
               (3 + swBytes),
               d.drop,
               ECU.ALL,
               True,
               swHeader)

def sw_clb(data):
    if(data.is_null): # Something to test data before using it..
        return
    data = bytes_to_int(data.messages[0].data[3:])
    if(data == 0): # no key pressed, jump out
        return

    for c, swButton in enumerate(swButtons, 1):
        if(swButton.bitSelect & data):
            if(swButton.isPressing is False):
                swButton.isPressing = True
                swButton.press()
        elif(swButton.isPressing is True):
            swButton.release()
    return

# 2280511 response: 62805100000000
keyCMD     = b"228051"
keyHeader  = b'0007A5'
keyBytes   = 4
keyBase    = 0x62805100000000
key0       = Button((0x62805100000400 ^ keyBase), False, "0")           # Number 0
key1       = Button((0x62805100000800 ^ keyBase), False, "1")           # Number 1
key2       = Button((0x62805100001000 ^ keyBase), False, "2")           # Number 2
key3       = Button((0x62805100002000 ^ keyBase), False, "3")           # Number 3
key4       = Button((0x62805100004000 ^ keyBase), False, "4")           # Number 4
key5       = Button((0x62805100008000 ^ keyBase), False, "5")           # Number 5
key6       = Button((0x62805100000001 ^ keyBase), False, "6")           # Number 6
key7       = Button((0x62805100000002 ^ keyBase), False, "7")           # Number 7
key8       = Button((0x62805100000004 ^ keyBase), False, "8")           # Number 8
key9       = Button((0x62805100000008 ^ keyBase), False, "9")           # Number 9
keyStar    = Button((0x628051FFFFFFFF ^ keyBase), False, "P")           # Phone
keyHash    = Button((0x628051FFFFFFFF ^ keyBase), False, "escape")      # Esc
keyInfo    = Button((0x628051FFFFFFFF ^ keyBase), False, "left arrow")  # Hamburger Menu
# keyReject  = Button((0x628051FFFFFFFF ^ keyBase), False, "a")
keyLL      = Button((0x628051FFFFFFFF ^ keyBase), False, "left arrow")  # Hamburger Menu
keyLR      = Button((0x628051FFFFFFFF ^ keyBase), False, "B")           # Play/Pause
keyRL      = Button((0x628051FFFFFFFF ^ keyBase), False, "H")           # Home
keyRR      = Button((0x628051FFFFFFFF ^ keyBase), False, "M")           # Voice Command
keyTA      = Button((0x628051FFFFFFFF ^ keyBase), False, "H")           # Home
keyMusic   = Button((0x628051FFFFFFFF ^ keyBase), False, "H")           # Home
keyNext    = Button((0x628051FFFFFFFF ^ keyBase), False, "N")           # Next
keyPrev    = Button((0x628051FFFFFFFF ^ keyBase), False, "V")           # Previous
# keyLeft    = Button((0x628051FFFFFFFF ^ keyBase), False, "num 1")
# keyRight   = Button((0x628051FFFFFFFF ^ keyBase), False, "num 2")
keyUp      = Button((0x628051FFFFFFFF ^ keyBase), False, "num 1")       # Wheel Left
keyDown    = Button((0x628051FFFFFFFF ^ keyBase), False, "num 2")       # Wheel Right
keyOK      = Button((0x628051FFFFFFFF ^ keyBase), False, "return")      # Enter
# keyCD      = Button((0x628051FFFFFFFF ^ keyBase), False, "H")
# keyRadio   = Button((0x628051FFFFFFFF ^ keyBase), False, "H")
keyAUX     = Button((0x62805110000000 ^ keyBase), False, "H")           # Home
# keyPhone   = Button((0x628051FFFFFFFF ^ keyBase), False, "H")
# keyMenu    = Button((0x628051FFFFFFFF ^ keyBase), False, "H")
# keyVolUp   = Button((0x628051FFFFFFFF ^ keyBase), False, "H")
# keyVolDown = Button((0x628051FFFFFFFF ^ keyBase), False, "H")

keyButtons  = [key0, key1, key2, key3, key4, key5, key6, key7, key8, key9,
               keyStar, keyHash, keyInfo, keyLL, keyLR, keyRL, keyRR, keyTA,
               keyMusic, keyNext, keyPrev, keyUp, keyDown, keyOK]

key = OBDCommand("Radio Keys",
               "Decode Radio Keys",
               keyCMD,
               (3 + keyBytes),
               d.drop,
               ECU.ALL,
               True,
               keyHeader)

def key_clb(data):
    if(data.is_null): # Something to test data before using it..
        return
    data = bytes_to_int(data.messages[0].data[3:])
    if(data == 0): # no key pressed, jump out
        return

    for c, keyButton in enumerate(keyButtons, 1):
        if(keyButton.bitSelect & data):
            if(keyButton.isPressing is False):
                keyButton.isPressing = True
                keyButton.press()
        elif(keyButton.isPressing is True):
            keyButton.release()
    return

# obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.OBD("COM9", protocol = "B")

connection.supported_commands.add(sw)
connection.supported_commands.add(key)

while(True):
    sw_clb(connection.query(sw))
    key_clb(connection.query(key))
    # time.sleep(0.01)
    
