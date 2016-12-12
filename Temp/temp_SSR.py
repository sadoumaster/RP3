# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:43:34 2016

@author: user1
"""

import sys, datetime
sys.path.append('/home/pi/Documents/PythonProjects')
from RP3.Temp_DS18B20 import read_temp
from time import sleep
import RPi.GPIO as GPIO

SSR_pin=20

def output(power):
    if power > 1:
        power = 1
    on = power * 10
    off = (1 - power) * 10
    if on > 0:
        GPIO.output(SSR_pin,GPIO.HIGH)
        sleep(on)
    if off > 0:
        GPIO.output(SSR_pin,GPIO.LOW)
        sleep(off)

def p(temp, target, kp):
    d = target - temp
    if d < 0:
        return 0
    power = d / target * kp
    return power

def i(prev, now, target, ki):
    if prev == 0:
        return 0
    d1 = target - now
    d2 = target - prev
    if d1 < 0:
        return 0
    if d2 < 0:
        d2 = 0
    return (d1 + d2) * 10 / 2 * ki


def main():
    if len(sys.argv) < 2:
        print('usafge: {} TARGET_TEMPERTURE'.format(sys.argv[0]))
        sys.exit(0)
    target = float(sys.argv[1])
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SSR_pin, GPIO.OUT)
    prev_temp=0
    t=0
    while True:
        now_temp = read_temp()
        pg = p(temp, target, 2.7)
        ig = i(prev_temp, now_temp, target, 0.005)
        power = pg + ig
        if power > 0:
            power += 0.13
        prev_temp = now_temp
        print ('{}sec, {}℃, {}\%'.forma(t, prev_temp, power*100))
        sys.stdout.flush()
        output(power)
        t += 10

if __name__ == "__main__":
    main()