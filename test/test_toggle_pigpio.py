# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:46:30 2016

@author: user1
"""

import pigpio
from time import sleep

def my_callback(channel):
    global LedState, LED, switch
    if channel ==switch:
        LedState=not LedState
        pi.write(LED, LedState)
        
LED, switch=25, 24
pi=pigpio.pi()
pi.set_mode(LED, OUTPUT)
pi.set_mode(switch, INPUT)
pi.write(LED, 0)
pi.set_pull_up_down(gpio=switch, pud=PUD_DOWN)
pi.callback(user_gpio=switch, edge=RISING_EDGE, func=my_callback)

LedState=0

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

pi.stop()