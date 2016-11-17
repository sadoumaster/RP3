# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:05:54 2016

@author: user1
"""
import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import RP3.LED.LED as LED
import time, math

def sin_curve_pwm(times=1, circle_sec=2, resolution=None):
    with LED.LED(4) as Blueled:
#        for j in range(times):
#            for i in range(-90, 270, 2):
#                degrees = 2 * math.pi/360 * i
#                interval = circle_sec / 180
#                Blueled.pwm(power = (math.sin(degrees)+1)*100/2, sec=interval)
        if resolution == None: # decide resolution by circle_sec
            if circle_sec <= 2: resolution = 10
            if circle_sec >  2: resolution = math.ceil(circle_sec * 10)
        for j in range(times):
            for i in range(resolution):
                degrees = 2 * math.pi/resolution * i
                interval = circle_sec / resolution
                Blueled.pwm(power = (math.sin(degrees-(math.pi/2))+1)*100/2, 
                            sec = interval)

        print ('end')

def blink_1f_pwm(interval_sec=0.01, resolution=500):
    from RP3.curve1f import curve_1f_generator
    with LED.LED(4) as Blueled:
        while True:
            fluctuation = curve_1f_generator(resolution=resolution)#-1.5~1.5の数字
            try:
                while True:
                    a=fluctuation.__next__()
                    #print((a+1.5)/3*100)
                    Blueled.pwm(power = ((a+1.5)/3*100), 
                                sec=interval_sec)
            except StopIteration:
                continue
if __name__ == '__main__':
    sin_curve_pwm(2,2,10)
    time.sleep(0.5)
    sin_curve_pwm(2,2,20)
    time.sleep(0.5)
    sin_curve_pwm(2,2,30)
    time.sleep(0.5)
    sin_curve_pwm(2,2,40)
    blink_1f_pwm()