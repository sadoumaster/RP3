# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 11:46:59 2016

@author: Kikkawa
"""
import pigpio, time

pi = pigpio.pi()
LED=4

pi.set_mode(LED, pigpio.OUTPUT)

print(pi.get_mode(LED))
pi.write(LED,1)
time.sleep(2)
pi.write(LED,0)
time.sleep(2)
pi.set_PWM_dutycycle(LED, 64)
time.sleep(2)
pi.set_PWM_range(LED, 100)
for i in range(100):
    pi.set_PWM_dutycycle(LED, i)
    time.sleep(0.01)
time.sleep(2)
print(pi.get_PWM_real_range(LED))
pi.write(LED, 0)