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
waittime=0.5
GPIO.setup(LEDPIN, GPIO.OUT)
count=0

try:
    for i in range(0,20000,50):
        count = 0
        while count < 1:
            GPIO.output(LEDPIN, GPIO.HIGH)
            time.sleep(0.000001*i)
            GPIO.output(LEDPIN, GPIO.LOW)
            time.sleep(0.02-(0.000001*i))
            count += 1
        print(i)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()