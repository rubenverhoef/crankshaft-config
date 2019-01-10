#!/usr/bin/python

# do whatever you need to do here
# by default this does nothing

import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "custom/obd"))
import obd
from obd import OBDCommand
from obd.protocols import ECU

# a callback that prints every new value to the console
def clb_sw(r):
    print r.value

def sw_decode(messages):
    """ decoder for Steering Wheel messages """
    d = messages[0].data # only operate on a single message
    d = d[2:] # chop off mode and PID bytes
    v = d & 0x000010  # helper function for converting byte arrays to ints
    return v

sw = OBDCommand("Steering Wheel",
               "Decode SW Commands",
               b"010C",
               4,
               sw_decode,
               ECU.ALL,
               False,
               7E0)


connection = obd.Async() # auto-connects to USB or RF port

# add your commands to the set of supported commands
connection.supported_commands.add(sw)
connection.watch(sw, callback=clb_sw)
connection.start()
