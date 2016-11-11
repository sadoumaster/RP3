# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:05:54 2016

@author: user1
"""
import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import RP3.LED as LED
import time, math

def sin_curve_pwm():    
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

def blink_1f_pwm():
    from RP3.1_f import curve_1f_generator
    with LED.LED(4) as Blueled:
        while True:
            fluctuation = curve_1f_generator()#-1.5~1.5の数字
            try:
                while True:
                    Blueled.pwm(power = ((fluctuation.__next__()+1.5)/3*100), 
                                time=0.5)
            except StopIteration:
                continue
        
                