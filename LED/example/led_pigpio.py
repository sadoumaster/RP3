# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 23:05:21 2016

@author: Kikkawa
"""

import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import RP3.LED.LED_pigpio as LED
import time

with LED.LED_pigpio(21) as white:
    try:
        while True:
            white.blink_1f_pwm(2)
    except:white.off()