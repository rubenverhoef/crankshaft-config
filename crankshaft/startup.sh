#!/bin/bash

# do whatever you need to do here
# by default this does nothing

# PWM backlight init
gpio -g mode 12 pwm
gpio -g mode 4 in

# LINBus Buttons
sudo python /boot/crankshaft/custom/linbus.py &

# RearCam
while true
do
gpio -g wfi 4 both
TRIGGER=`gpio -g read 4`
if [ $TRIGGER -ne 1 ] ; then
    (cd /boot/crankshaft/custom/cam_overlay && ./cam_overlay.bin &)
elif [ $TRIGGER -ne 0 ] ; then
    killall cam_overlay.bin
fi
done
