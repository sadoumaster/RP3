# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:05:54 2016

@author: user1
"""
import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import RP3.LED.LED as LED
import time, math

def sin_curve_pwm(circle_sec=2, on_off=None, resolution=None):
    pattern_on = ('on', 'ON', 'On', True, 1, '1')
    pattern_off = ('off', 'OFF', 'Off', False, 0, '0')
    with LED.LED(4) as Blueled:
        if resolution == None: # decide resolution by circle_sec
            resolution = math.ceil(circle_sec * 20)
        for i in range(resolution):
            if on_off == None:
                degrees = 2 * math.pi/resolution * i
                interval = circle_sec / resolution
                Blueled.pwm(power = (math.sin(degrees-(math.pi/2))+1)*100/2, 
                            sec = interval)
            elif on_off in pattern_on:
                degrees = math.pi/resolution * i
                interval = circle_sec / resolution
                Blueled.pwm(power = (math.sin(degrees-(math.pi/2))+1)*100/2, 
                            sec = interval)
            elif on_off in pattern_off:
                degrees = math.pi/resolution * i
                interval = circle_sec / resolution
                Blueled.pwm(power = (math.sin(degrees+(math.pi/2))+1)*100/2, 
                            sec = interval)
            else:
                print('''on_off can read
                pattern_on = (\'on\', \'ON\', \'On\', True, 1, \'1\'),
                pattern_off = (\'off\', \'OFF\', \'Off\', False, 0, \'0\')''')
                break
        print ('end')

def blink_1f_pwm(circle_sec=5, resolution=None):
    from RP3.curve1f import curve_1f_generator
    if resolution==None: resolution=circle_sec*20
    with LED.LED(4) as Blueled:
        fluctuation = curve_1f_generator(resolution=resolution)#-1.5~1.5の数字
        try:
            while True:
                a=fluctuation.__next__()
                #print((a+1.5)/3*100)
                Blueled.pwm(power = ((a+1.5)/3*100), 
                            sec=circle_sec/resolution)
        except StopIteration:
            pass
        
if __name__ == '__main__':
    while True:
        blink_1f_pwm(3)

#    for i in range(10):
#        switch=1
#        sin_curve_pwm(circle_sec=0.2, on_off=switch)
#        with LED.LED(4) as Blueled:
#            Blueled.blink(0.6,0,1)
#        switch= not switch
#        sin_curve_pwm(circle_sec=0.2, on_off=switch)
#    blink_1f_pwm()