# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 19:17:43 2016

@author: user1
"""

import RPi.GPIO as GPIO
from time import sleep

def my_callback(channel):
    global LedState, LED, switch
    if channel ==switch:
        LedState = not LedState
        GPIO.output(LED, LedState)

LED, switch=21, 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#toggleイベントを呼び出す機能
#RISINGイベントでcallbackで指定した関数が呼ばれる。
GPIO.add_event_detect(switch, GPIO.RISING, 
                      callback=my_callback, bouncetime=200)

LedState=GPIO.LOW

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

GPIO.cleanup()