# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 00:21:46 2016

@author: user1
led_blink program
"""

import pigpio
from time import sleep #for waiting
import math
#GPIO.setmode(GPIO.BCM)

#LEDの点灯パターンを記したclass。LED(num) numにGPIO PINを指定。
#with as 構文使用可能。ex. with LED(4) as redLED :
class LED_pigpio():
    def __init__(self, GPIO_PIN_No):
        self.GPIO_PIN = GPIO_PIN_No
        self.pi=pigpio.pi()#初期化処理。
        self.pi.set_mode(self.GPIO_PIN, pigpio.OUTPUT)
        print ('set GPIO{} for LED'.format(self.GPIO_PIN))
    
    def on(self):  self.pwm(power=100)
    
    def off(self): self.pwm(power=0)
    
    def blink(self, duration=0.5, interval=0.5 ,times=5, power=100):
        for i in range(times):
            self.on(power)
            sleep(duration)
            self.off()
            sleep(interval)

    def pwm(self, power=100):#0<＝power<＝100
        if 0<power<=100:
            self.power=math.ceil(255/100*power)
            self.pi.set_PWM_dutycycle(self.GPIO_PIN, self.power)
        elif power>100: self.pi.set_PWM_dutycycle(self.GPIO_PIN, 255)
        elif power<=0:   self.pi.set_PWM_dutycycle(self.GPIO_PIN, 0)
            
    def on_off_smooth(self, on_off='on', circle_sec=0.5):
        if on_off=='on':
            self.sin_curve_pwm(on_off='on', circle_sec=circle_sec)
        elif on_off=='off':
            self.sin_curve_pwm(on_off='off', circle_sec=circle_sec)
        else:
            print('func on_off_smooth needs \'on\' or \'off\'')
            pass

    def sin_curve_pwm(self, circle_sec=2, on_off=None, resolution=None):
        pattern_on = ('on', 'ON', 'On', True, 1, '1')
        pattern_off = ('off', 'OFF', 'Off', False, 0, '0')
        if resolution == None: # decide resolution by circle_sec
            resolution = math.ceil(circle_sec*30)
        for i in range(1, resolution+1): #0-100-0
            if on_off == None:
                degrees = 2 * math.pi/resolution * i
                interval = circle_sec / resolution
                self.pwm(power = (math.sin(degrees-(math.pi/2))+1)*100/2)
                sleep(interval)
            elif on_off in pattern_on: #when on
                degrees = math.pi/resolution * i
                interval = circle_sec / resolution
                self.pwm(power = (math.sin(degrees-(math.pi/2))+1)*100/2)
                sleep(interval)
            elif on_off in pattern_off: #when off
                degrees = math.pi/resolution * i
                interval = circle_sec / resolution
                self.pwm(power = (math.sin(degrees+(math.pi/2))+1)*100/2)
                print(i)
                sleep(interval)
            else:
                print('''on_off can read
                pattern_on = (\'on\', \'ON\', \'On\', True, 1, \'1\'),
                pattern_off = (\'off\', \'OFF\', \'Off\', False, 0, \'0\')''')
                break

    def blink_1f_pwm(self, circle_sec=5, resolution=None):
        from RP3.curve1f import curve_1f_generator
        if resolution==None: resolution=circle_sec*30
        interval=circle_sec/resolution
        fluctuation = curve_1f_generator(resolution=resolution)#-1.5~1.5の数字
        try:
            while True:
                a=fluctuation.__next__()
                #print((a+1.5)/3*100)
                self.pwm(power = ((a+1.5)/3*100))
                sleep(interval)
        except StopIteration:
            pass

    def __enter__(self):
        print ("start")
        return self
        
    def __exit__(self, type, value, traceback):
        self.pi.stop()
        print('Cleanup GPIO{}'.format(self.GPIO_PIN))

if __name__ == '__main__' :
    print('This is a module for using Led.')