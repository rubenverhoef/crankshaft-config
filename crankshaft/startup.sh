#!/bin/bash

# do whatever you need to do here
# by default this does nothing

# PWM backlight init
sudo /usr/bin/gpio -g mode 12 pwm

# LINBus Buttons
sudo python /boot/crankshaft/custom/linbus.py &

# RearCam
sudo /usr/bin/gpio -g mode 4 in
sudo /usr/bin/gpio -g mode 4 up
while true; do
    REARCAM_GPIO=`gpio -g read 4`
    if [ $REARCAM_GPIO -ne 1 ] ; then
        (cd /boot/crankshaft/custom/rear_cam && ./rear_cam &)
    else
        killall rear_cam
    fi
    sleep 1
done
