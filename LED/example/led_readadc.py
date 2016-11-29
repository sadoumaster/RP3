# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:27:19 2016

@author: user1
"""

import sys
sys.path.append('/home/pi/Documents/PythonProjects')
from RP3.readadc.readadc import readadc
from RP3.LED.LED_pigpio import LED_pigpio
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
SPICLK=11
SPIMOSI=10
SPIMISO=9
SPICS=8
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

try:
    with LED_pigpio(24) as led:
        while True:
            inputVal0=readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
            led.pwm((1-inputVal0/4095)*100)
            sleep(0.01)

except KeyboardInterrupt:pass

GPIO.cleanup()