# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:50:39 2016

@author: user1
"""

import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import datetime
from time import sleep
import RP3.LED_pigpio.LED_pigpio as LED
import pigpio

now=datetime.datetime.now()

def get_target_time():
    #ledを付け始める日時を決める。０時以降に設定した場合は当日。前なら翌日に。５時半
    if 0<=now.hour<=5:#設定した時間が０時以降ならその日の５時半
        target_time=datetime.datetime(now.year, now.month, now.day, 5, 30)
    else:#設定した時間が０時以前なら翌日の５時半
        target_time=datetime.datetime(now.year, now.month, now.day, 5, 30)+datetime.timedelta(days=1)
    return target_time

def get_time_difference():
    #あと何秒で指定時刻になるか計算
    now=datetime.datetime.now()
    target_time=get_target_time()
    time_difference=target_time-now
    return int(time_difference.total_seconds())

def led_on():
    #LEDを３０分かけて徐々に付けて、１時間つけっぱなし、５分かけて徐々に消える。
    with LED(led_pin) as led:
        led.on_off_smooth(on_off='on', circle_sec=1800)
        led.on()
        sleep(3600)
        led.on_off_smooth(on_off='off', circle_sec=300)

led_pin=20
switch_pin=21

pi=pigpio.pi()
pi.set_mode(switch_pin, pigpio.INPUT)
pi.set_pull_up_down(gpio=switch_pin, pud=pigpio.PUD_DOWN)

#LEDの電源を切る
with LED(led_pin) as led:
    led.off()

time_difference=get_time_difference()
sleep(time_difference)
interval=int(30*60/100) #３０分＊６０秒　を１００で割る=18秒

with LED(led_pin) as led:
    for power in range(1, 101):
        led.pwm(power)

        for i in range(interval*2):
            if pi.read(switch_pin, 1):
                
            sleep(0.5)
    
    led.on()
