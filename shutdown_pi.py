#!/usr/bin/python
# Simple script for shutting down the raspberry Pi at the press of a button.
# by Inderpreet Singh

import RPi.GPIO as GPIO
import time
import os
import subprocess

# Use the Broadcom SOC Pin numbers
# Setup the Pin with Internal pullups enabled and PIN in reading mode.
GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Our function on what to do when the button is pressed
def Shutdown(channel):
    os.system("pkill --oldest  chromium")
    os.system("sleep 3")
    os.system("sudo reboot")
#    subprocess.Popen("wmctrl -c chromium; sleep 5; sudo reboot")
#    subprocess.call("(wmctrl -c chromium && sleep 5 && sudo shutdown)")

# Add our function to execute when the button pressed event happens
GPIO.add_event_detect(3, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)

# Now wait!
while 1:
    time.sleep(1)