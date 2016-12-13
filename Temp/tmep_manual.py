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
    def safe_tempUP():
        pass

    def safe_tempDOWN():
        pass
    
    def near_tempUP():
        pass
    
    def near_tempDOWN():
        pass

    def over_tempUP():
        pass

    def over_tempDOWN():
        pass

    
    def too_over_tempUP():
        pass

    def too_over_tempDOWN():
        pass

    
    def off():
        R.off()
        G.off()
        B.off()
    
    def main():
        now_temp=0
        if len(sys.argv) <2:
            print('usage: {} Target_Temperature'.format(sys.argv[0]))
            sys.exit(0)
        target = float(sys.argv[1])
        now_temp_archive=0
        while True:
            now_temp=read_temp()
            diff_temp=target-now_temp
            if now_temp_archive < now_temp:                    
                if diff_temp > 2.5:
                    safe_tempUP()
                elif -2.5 <=diff_temp <= 2.5:
                    near_tempUP()
                elif -7.5 <=diff_temp < -2.5:
                    over_tempUP()
                else:
                    too_over_tempUP()
                    
            else:                    
                if diff_temp > 2.5:
                    safe_tempDOWN()
                elif -2.5 <=diff_temp <= 2.5:
                    near_tempDOWN()
                elif -7.5 <=diff_temp < -2.5:
                    over_tempDOWN()
                else:
                    too_over_tempDOWN()
            now_temp_archive=now_temp
            sleep(5)
    
    if __name__=='__main__':
        try:
            main()
        except KeyboardInterrupt:
            pass
                