# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 23:13:32 2016

@author: Kikkawa
"""

import sys
sys.path.append('/home/pi/Documents/PythonProjects')
from RP3.LED.LED_pigpio import LED_pigpio as LED
from time import sleep
import RPi.GPIO as GPIO
import threading

R,G,B=16,21,20

def color(Rp, Gp, Bp):
    #yellow(100,100,0)
    with LED(R) as RLED, LED(G) as GLED, LED(B) as BLED:
        RLED.pwm(Rp)
        GLED.pwm(Gp)
        BLED.pwm(Bp)

try:
    color(0,0,0)
    color(25,100,100)

except KeyboardInterrupt: pass