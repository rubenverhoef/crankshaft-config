### Hardware ###
# The hardware pins can be completly disabled with the global flag.

# Global Flag (enables / disables gpio usage excluding device connected
# trigger gpio and ignition based shutdown!)
ENABLE_GPIO=0

# Possible used gpio's by hifiberry dac's depending on model:
# For more info visit the hifiberry homepage! To prevent from bugs don't use them!
#
# GPIO 4,5,6,16,18,19,20,21,27,28,29,30,31

# Generally used GPIO's
# Used for HAT modules - Never use it!
# GPIO 27,28

# GPIO Setup
DEV_PIN=0
INVERT_PIN=0
X11_PIN=0

# Device connected gpio (device connected 1 / else 0)
# Note: this gpio depends NOT on ENABLE_GPIO!!!
# To disable set to 0
ANDROID_PIN=0

# GPIO Trigger for Rearcam
# GPIO wich triggers enabling Rearcam Mode of RPICam
# To disable set to 0
REARCAM_PIN=0

### Maintenance / Initial Setup ###
# Start Crankshaft in dev mode to get network, shell and ssh access
# openauto won't be started automatically
DEV_MODE=0
# Start openauto in dev mode if enabled
DEV_MODE_APP=1

### Debugging ###
# Start Crankshaft in debug mode to get network, shell and ssh access
# System will do a normal start in ro mode
DEBUG_MODE=0

### OpenAuto ###
# Start OpenAuto in X11 or EGL
# By default, EGL, but if you can't get it to work, do X11
START_X11=0

### Screen ###
# Brightness related stuff
# brightness file (default for rpi display: /sys/class/backlight/rpi_backlight/brightness)
BRIGHTNESS_FILE=/sys/class/backlight/rpi_backlight/brightness

# brightness values
BR_MIN=0
BR_MAX=1023
BR_STEP=103

# Custom brightness control
# Note: this command is called after every brightness change - can slow down for example the brightness
# slider depending on execution speed - the process is called with "&" so call is not waiting for exit!
# Sample call which will be executed on request: "CUSTOM_BRIGHTNESS_COMMAND brightnessvalue &"
#
# Note: To allow backup and restore your command must be located on /boot/crankshaft/custom/
# otherwise it will not be transfered during updates!
#
# To disable leave empty
CUSTOM_BRIGHTNESS_COMMAND=/boot/crankshaft/custom/brightness_command

# Flip the screen 180°
FLIP_SCREEN=0

# Try to identify and setup display during boot
# don't use - only prepared for further releases!
DISPLAY_AUTO_DETECT=0

### Audio ###
# If stored vol is lower than this set to this value
STARTUP_VOL_MIN=100
# If stored vol is greater than this limit to this value
STARTUP_VOL_MAX=100

###  Power Mgmt Related Stuff ###
# Timeout display after disconnect or after boot without connected device
DISCONNECTION_SCREEN_POWEROFF_SECS=120
# Disable Timer
DISCONNECTION_SCREEN_POWEROFF_DISABLE=1

# Timeout shutdown after disconnect or after boot without connected device
#
# Note: on first boot timeout is set to 300 seconds - after first start
# this value is used
DISCONNECTION_POWEROFF_MINS=60
# Disable Timer
DISCONNECTION_POWEROFF_DISABLE=1

### Wifi Setup ###
# Your country code like EN,DE,FR,UK etc.
WIFI_COUNTRY=NL

# Wifi client mode - Only used in dev mode
# If your SSID or password contains special chars or spaces make sure using quotation marks ="SSID" / ="password"
WIFI_SSID="OnePlus 3T Ruben"
WIFI_PSK="1+3TRuben"

# Hotspot (if enabled the wifi client is disabled and a hotspot is opened)
# If your SSID or password contains special chars or spaces make sure using quotation marks ="SSID" / ="password"
ENABLE_HOTSPOT=1
HOTSPOT_PSK="FordRuben"

### RPi Camera Module ###
# Overlay settings
RPICAM_X=100
RPICAM_Y=52
RPICAM_WIDTH=590
RPICAM_HEIGTH=366
RPICAM_HFLIP=0
RPICAM_VFLIP=0
RPICAM_ROTATION=0

# RTC Related Settings ###
# Enables day/night switch by rtc - don't change manually!
# Use command 'crankshaft rtc xxx' in shell!
RTC_DAYNIGHT=1

# Day / Night (only working with rtc enabled) - don't change manually!
# Use command 'crankshaft timers daynight xx xx' in shell!
RTC_DAY_START=8
RTC_NIGHT_START=17

# Ignition Based Shutdown
# This pin must be low to keep system running. If high for > IGNITION-DELAY (seconds)
# system will do a shutdown
# Note: this gpio depends NOT on ENABLE_GPIO!!!
# To disable set to 0
IGNITION_PIN=13
# Time to wait until shutting down (seconds)
IGNITION_DELAY=30

# Enable experimental bluetooth stuff
# don't use - only prepared for further releases!
ENABLE_BLUETOOTH=1
# Allow to autopair devices
ENABLE_PAIRABLE=1
# Use external adapter not builtin
EXTERNAL_BLUETOOTH=0

# Skip usb flash and usb detect for debug mode and dev mode - This overrides ALLOW_USB_FLASH!
# CSSTORAGE will still be searched for and mounted.
SKIP_USB_DETECT=1

# System updates
ALLOW_USB_FLASH=1
