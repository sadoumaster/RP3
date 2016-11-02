# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:21:46 2016

@author: user1
led_blink program
"""

import RPi.GPIO as Gpio #Import raspberry pi library
import time #for waiting

Gpio.setmode(Gpio.BCM)
Gpio.setup(2, Gpio.OUT)
count=0

while count < 50 :
    Gpio.output(2, Gpio.HIGH)
    time.sleep(0.5)
    Gpio.output(2, Gpio.LOW)
    time.sleep(0.5)
    count += 1