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
    def safe_tempUP():#blue
        on(0, 0, 25)
        sleep(10)

    def safe_tempDOWN():#blue blink
        blink(0, 0, 25)
    
    def near_tempUP():#green
        on(0, 25, 0)
        sleep(10)
    
    def near_tempDOWN():#green blink
        blink(0, 25, 0)

    def over_tempUP():#yellow
        on(25, 25, 0)
        sleep(10)

    def over_tempDOWN():#yellow blink
        blink(25, 25, 0)
    
    def too_over_tempUP():#red
        on(25, 0, 0)
        sleep(10)

    def too_over_tempDOWN():#red blink
        blink(25, 0, 0)

    def off():
        R.off()
        G.off()
        B.off()
    
    def on(Rp, Gp, Bp):
        R.pwm(Rp)
        G.pwm(Gp)
        B.pwm(Bp)
        
    def blink(Rp, Gp, Bp):#ついて消えてを1秒毎5回　全部で10秒
        for i in range(5):
            on(Rp, Gp, Bp)
            sleep(1)
            off()
            sleep(1)
        
    
    def main():
        now_temp=0
        if len(sys.argv) <2:#ターゲット温度を指定
            print('usage: {} Target_Temperature'.format(sys.argv[0]))
            sys.exit(0)
        target = float(sys.argv[1])
        now_temp_archive=0
        while True:
            now_temp=read_temp()
            diff_temp=target-now_temp
            if now_temp_archive < now_temp:#温度上昇中
                if diff_temp > 2.5:
                    safe_tempUP()
                elif -2.5 <=diff_temp <= 2.5:
                    near_tempUP()
                elif -7.5 <=diff_temp < -2.5:
                    over_tempUP()
                else:
                    too_over_tempUP()
                    
            else:                           #温度下降中
                if diff_temp > 2.5:
                    safe_tempDOWN()
                elif -2.5 <=diff_temp <= 2.5:
                    near_tempDOWN()
                elif -7.5 <=diff_temp < -2.5:
                    over_tempDOWN()
                else:
                    too_over_tempDOWN()
            now_temp_archive=now_temp
            sleep(0.001)
    
    if __name__=='__main__':
        try:
            main()
        except KeyboardInterrupt:
            off()
            pass
                