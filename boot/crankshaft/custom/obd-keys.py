#!/usr/bin/python3

import os, sys

sys.path.append(os.path.join(os.path.dirname(__file__), "keyboard"))
sys.path.append(os.path.join(os.path.dirname(__file__), "obd"))
sys.path.append(os.path.join(os.path.dirname(__file__), "pint"))

import keyboard # import for emulating keyboard presses

import obd #import for reading/sending obd messages
from obd import OBDCommand
from obd.protocols import ECU

SW_BASE     = 0x28000000
SW_NEXT     = 0x00020000
SW_PREV     = 0x00010000
SW_VOLUP    = 0x00010000
SW_VOLDOWN  = 0x00010000
SW_M        = 0x00010000
SW_VOICE    = 0x00010000

KEY_BASE    = 0x33000000
KEY_0       = 0x00010000
KEY_1       = 0x00010000
KEY_2       = 0x00010000
KEY_3       = 0x00010000
KEY_4       = 0x00010000
KEY_5       = 0x00010000
KEY_6       = 0x00010000
KEY_7       = 0x00010000
KEY_8       = 0x00010000
KEY_9       = 0x00010000
KEY_STAR    = 0x00010000
KEY_HASH    = 0x00010000
KEY_LL      = 0x00010000
KEY_LR      = 0x00010000
KEY_RL      = 0x00010000
KEY_RR      = 0x00010000
KEY_TA      = 0x00010000
KEY_MUSIC   = 0x00010000
KEY_NEXT    = 0x00010000
KEY_PREV    = 0x00010000
KEY_LEFT    = 0x00010000
KEY_RIGHT   = 0x00010000
KEY_UP      = 0x00010000
KEY_DOWN    = 0x00010000
KEY_OK      = 0x00010000

def sw_clb(data):
    if(data & SW_PREV):
        print("SW_PREV")

def key_clb(data):
    if(data & KEY_PREV):
        print("KEY_PREV")


def sw_decode(messages):
    """ decoder for Radio Key messages """
    return messages - KEY_BASE

def key_decode(messages):
    """ decoder for Steering Wheel messages """
    return messages - SW_BASE

sw = OBDCommand("Steering Wheel",
               "Decode SW Commands",
               "ATE1",
               4,
               sw_decode,
               ECU.ALL,
               False)

key = OBDCommand("Steering Wheel",
               "Decode SW Commands",
               "ATE1",
               4,
               key_decode,
               ECU.ALL,
               False)

obd.logger.setLevel(obd.logging.DEBUG)

connection = obd.Async()

connection.supported_commands.add(sw)
connection.watch(sw, callback=sw_clb)

connection.supported_commands.add(key)
connection.watch(key, callback=key_clb)

connection.start()
