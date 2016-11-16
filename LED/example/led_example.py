# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:05:54 2016

@author: user1
"""
import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import RP3.LED.LED as LED
import time, math

def sin_curve_pwm(times=1 ,circle_sec=10):    
    with LED.LED(4) as Blueled:
        for j in range(times):
            for i in range(-90, 271):
                degrees = 2 * math.pi/360 * i
                Blueled.pwm(power = (math.sin(degrees)+1)*100/2, sec=0.05)

        print ('end')

def blink_1f_pwm():
    from RP3.curve1f import curve_1f_generator
    with LED.LED(4) as Blueled:
        while True:
            fluctuation = curve_1f_generator(resolution=500)#-1.5~1.5の数字
            try:
                while True:
                    a=fluctuation.__next__()
                    #print((a+1.5)/3*100)
                    Blueled.pwm(power = ((a+1.5)/3*100), 
                                sec=0.01)
            except StopIteration:
                continue
if __name__ == '__main__':
    sin_curve_pwm(2)
    blink_1f_pwm()