# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 21:31:35 2016

@author: Kikkawa
"""

import RPi.GPIO as GPIO
from time import sleep

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum>7 or adcnum<0:return -1
    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)
    
    commandout=adcnum
    commandout|=0x18
    commandout<<=3
    for i in range(5):
        if commandout & 0x80:   GPIO.output(mosipin, GPIO.HIGH)
        else:                   GPIO.output(mosipin, GPIO.LOW)
        commandout<<=1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout=0
    
    for i in range(13):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout<<=1
        if i>0 and GPIO.input(misopin)==GPIO.HIGH:adcout|=0x1
    GPIO.output(cspin, GPIO.HIGH)
    #0-4095
    return adcout#0-4095 0b111111111111 0xfff

if __name__=='__main__':
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
        while True:
            inputVal0=readadc(7, SPICLK, SPIMOSI, SPIMISO, SPICS)#0-4095
            print('{}kΩ'.format(inputVal0*2.442))#10000Ω/4095=2.442
            sleep(0.2)
    
    except KeyboardInterrupt:pass
    
    GPIO.cleanup()