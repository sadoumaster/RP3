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

#---setting for adc converter---
adc_pin0=0
SPICLK=11
SPIMOSI=10
SPIMISO=9
SPICS=8
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)
#-------

try:
    with LED_pigpio(25) as moter0, LED_pigpio(24) as moter1:
        moter0.pwm(0)
        moter1.pwm(0)
        while True:
            inputVal0=readadc(adc_pin0, SPICLK, SPIMOSI, SPIMISO, SPICS)
            if inputVal0>100 and inputVal0<2048:#101-2047
                moter1.pwm(0)
                duty=(2048-inputVal0)*70/2048
                moter0.pwm(duty)
            elif inputVal0>=2048 and inputVal0<4000:#2048-3999
                moter0.pwm(0)
                duty=(inputVal0-2048)*70/2048
                moter1.pwm(duty)
            sleep(0)
                

except KeyboardInterrupt:pass

GPIO.cleanup()