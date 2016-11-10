# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:21:46 2016

@author: user1
led_blink program
"""

import RPi.GPIO as GPIO #Import raspberry pi library
import time #for waiting
GPIO.setmode(GPIO.BCM)
LEDPIN=4
waittime=0.2
GPIO.setup(LEDPIN, GPIO.OUT)
count=0

try:
    while count < 10 :
        GPIO.output(LEDPIN, GPIO.HIGH)
        time.sleep(waittime)
        GPIO.output(LEDPIN, GPIO.LOW)
        time.sleep(waittime)
        count += 1
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
