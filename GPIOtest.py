# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 22:03:48 2016

@author: Kikkawa
"""

import RPi.GPIO as GPIO
from time import sleep
GPIO_PIN=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)
GPIO.output(GPIO_PIN, GPIO.HIGH)

try:
    while True:sleep(0.01)

except KeyboardInterrupt: pass

finally:GPIO.cleanup()