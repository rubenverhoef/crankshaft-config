#!/usr/bin/python3

# do whatever you need to do here
# by default this does nothing

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "keyboard"))
sys.path.append(os.path.join(os.path.dirname(__file__), "obd"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pint"))

import keyboard # import for emulating keyboard presses

import obd #import for reading/sending obd messages
from obd import OBDCommand
from obd.protocols import ECU

# a callback that prints every new value to the console
def clb_sw(r):
    print("TEST")

def sw_decode(messages):
    """ decoder for Steering Wheel messages """
    # d = messages[0].data # only operate on a single message
    # d = d[2:] # chop off mode and PID bytes
    # v = d & 0x000010  # helper function for converting byte arrays to ints
    # keyboard.press("1")
    # keyboard.release(buttons[data])
    return 0

sw = OBDCommand("Steering Wheel",
               "Decode SW Commands",
               "ATE1",
               4,
               sw_decode,
               ECU.ALL,
               False)
obd.logger.setLevel(obd.logging.DEBUG) # enables all debug information

connection = obd.Async() # auto-connects to USB or RF port

# add your commands to the set of supported commands
connection.supported_commands.add(sw)
connection.watch(sw, callback=clb_sw)
connection.start()
