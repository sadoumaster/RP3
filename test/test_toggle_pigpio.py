# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:46:30 2016

@author: user1
"""

import pigpio
from time import sleep

def my_callback(gpio, level=5, tick=200):
    global LedState, LED, switch
    if gpio ==switch:
        LedState=not LedState
        pi.write(LED, LedState)
        
LED, switch=21, 26
pi=pigpio.pi()
pi.set_mode(LED, pigpio.OUTPUT)
pi.set_mode(switch, pigpio.INPUT)
pi.write(LED, 0)
pi.set_pull_up_down(gpio=switch, pud=pigpio.PUD_DOWN)
pi.set_noise_filter(user_gpio=switch, steady=200000, active=0)
pi.callback(user_gpio=switch, edge=pigpio.RISING_EDGE, func=my_callback)

LedState=0

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

=======
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:46:30 2016

@author: user1
"""

import pigpio
from time import sleep

def my_callback(gpio, level=5, tick=200):
    global LedState, LED, switch
    if gpio ==switch:
        LedState=not LedState
        pi.write(LED, LedState)
        
LED, switch=21, 26
pi=pigpio.pi()
pi.set_mode(LED, pigpio.OUTPUT)
pi.set_mode(switch, pigpio.INPUT)
pi.write(LED, 0)
pi.set_pull_up_down(gpio=switch, pud=pigpio.PUD_DOWN)
#Level changes on the GPIO are ignored until a level which has been stable 
#for steady microseconds is detected. 
pi.set_noise_filter(user_gpio=switch, steady=200000, active=0)
pi.callback(user_gpio=switch, edge=pigpio.RISING_EDGE, func=my_callback)

LedState=0

try:
    while True:
        sleep(0.01)

except KeyboardInterrupt:
    pass

>>>>>>> 37526906407b643c4c9c5ea7cf8fbf5cd77d3377
pi.stop()