# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:36:07 2016

@author: user1
"""

import sys, datetime
sys.path.append('/home/pi/Documents/PythonProjects')
from RP3.Temp_DS18B20 import read_temp
from RP3.LED.LED_pigpio import LED_pigpio as LED
from time import sleep
import RPi.GPIO as GPIO

R, G, B=21, 22, 23
with LED(R) as R, LED(G) as G, LED(B) as B:
    def safe_temp():
        pass
    
    def near_temp():
        pass
    
    def over_temp():
        pass
    
    def too_over_temp():
        pass
    
    def off():
        R.off()
        G.off()
        B.off()
    
    def main():
        now_temp=0
        if len(sys.argv) <2:
            print('usafge: {} Target_Temperature'.format(sys.argv[0]))
            sys.exit(0)
        target = float(sys.argv[1])
        while True:
            now_temp=read_temp()
            diff_temp=target-now_temp
            if diff_temp > 2.5:
                safe_temp()
            elif -2.5 <=diff_temp <= 2.5:
                near_temp()
            elif -7.5 <=diff_temp < -2.5:
                over_temp()
            else:
                too_over_temp()
            sleep(5)
    
    if __name__=='__main__':
        try:
            main()
        except KeyboardInterrupt:
            pass
                