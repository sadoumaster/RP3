# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:21:46 2016

@author: user1
led_blink program
"""

import RPi.GPIO as GPIO #Import raspberry pi library
import time #for waiting
GPIO.setmode(GPIO.BCM)

#LEDの点灯パターンを記したclass。LED(num) numにGPIO PINを指定。
#with as 構文使用可能。ex. with LED(4) as redLED :
class LED():
    def __init__(self, GPIO_PIN_No):
        self.GPIO_PIN = GPIO_PIN_No
        GPIO.setup(self.GPIO_PIN, GPIO.OUT)
        print ('set % PIN for LED'.format(self.GPIO_PIN))
    
    def blink(self, duration = 0.5, interval = 0.5 ,times = 5):
        for i in range(times):
            GPIO.output(self.GPIO_PIN, GPIO.HIGH)
            time.sleep(duration)
            GPIO.output(self.GPIO_PIN, GPIO.LOW)
            time.sleep(interval)

    def pwm(self, power = 100, time = 0.1, Hz = 50):
        if (power < 0) & (power > 100):
            print('Input power between 1 and 100')
            pass
        if Hz < 1 :
            print('input Hz bigger than 1')
            pass
        if time < 0 :
            print('input time bigger than 0')
            pass
        interval = 1 / Hz
        ontime = interval * power / 100
        offtime = interval - ontime
        for i in range(time * Hz):
            GPIO.output(self.GPIO_PIN, GPIO.HIGH)
            time.sleep(ontime)
            GPIO.output(self.GPIO_PIN, GPIO.LOW)
            time.sleep(offtime)

    def __enter__(self):
        print ("start")
        return self
        
    def __exit__(self, type, value, traceback):
        GPIO.cleanup()
        print('Cleanup GPIO PINs')

if __name__ == '__main__' :
    print('This is a module for using Led.')