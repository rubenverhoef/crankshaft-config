#!/bin/bash

# do whatever you need to do here
# by default this does nothing

# PWM backlight init
gpio mode 26 pwm

# LINBus Buttons
sudo python /boot/crankshaft/custom/linbus.py &
