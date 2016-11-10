# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:05:54 2016

@author: user1
"""

import RP3.LED as LED
import time, math

with LED.LED(4) as Blueled:
    Blueled.blink(times=10)
    time.sleep(0.5)
    for i in range(101):
        Blueled.pwm(power = i)
        time.sleep(0.1)
    time.sleep(0.5)
    for i in range(-90, 271):
        degrees = math.pi()/i
        Blueled.pwm(power = (math.sin(degrees)+1)*100, time=0.05)
    print ('end')