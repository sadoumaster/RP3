# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 22:51:04 2016

@author: Kikkawa
"""

import RPi.GPIO as GPIO
from time import sleep

led=23
switch=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN)
GPIO.output(led, GPIO.LOW)

try:
    while True:
        if GPIO.input(switch) == GPIO.HIGH:
            GPIO.output(led, GPIO.HIGH)
#            print('on')
        else:
            GPIO.output(led, GPIO.LOW)
#            print('off')
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()