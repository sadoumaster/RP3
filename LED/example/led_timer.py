# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 22:50:39 2016

@author: user1
"""

import sys
sys.path.append('/home/pi/Documents/PythonProjects')
import datetime, threading
from time import sleep
import RP3.LED_pigpio.LED_pigpio as LED
import pigpio

led_pin=20
switch_pin=21

def get_target_time():
    #ledを付け始める日時を決める。０時以降に設定した場合は当日。前なら翌日に。５時半
    now=datetime.datetime.now()
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

#def led_on():
#    #LEDを３０分かけて徐々に付けて、30分つけっぱなし、30分チカチカ、５分かけて徐々に消える。
#    with LED(led_pin) as led:
#        led.on_off_smooth(on_off='on', circle_sec=1800)
#        led.on()
#        sleep(1800)
#        led_state=1
#        blink(duration=1, interval=1 ,times=900, power=100)
#        led.on_off_smooth(on_off='off', circle_sec=300)
#
#def led_timer_thread(gpio, level=5, tick=200):
#    if gpio == switch_pin:
#        led_on()

class LedThread(threading.Thread):
    def __init__(self, pin):
        super().__init__()
        self.led_pin=pin
        self.led=LED(self.led_pin)
        self.led.off()
        self.stop_event=threading.Event()
        self.setDaemon(True)
    
    #Threadをとめるフラグを立てる
    def stop(self):
        self.stop_event.set()
        
    def led_callback(self, gpio, level=5, tick=200):
        if gpio ==switch_pin:
            self.stop()
    
    def run(self):
        #total 5700secs　stop_eventフラッグが立つと一気にoffまでいく。
        self.count=0
        #徐々に付けていく 1800secs
        while not self.stop_event.is_set() or self.count>1800:
            self.led.pwm(100/1800*self.count)
            self.count+=1
            sleep(1)
        self.count=0
        #LEDつけっぱなし30分 1800secs
        while not self.stop_event.is_set() or self.count>1800:
            self.led.on()
            self.count+=1
            sleep(1)
        self.count=0
        #LEDチカチカ 1800secs
        while not self.stop_event.is_set() or self.count>900:
            self.led.blink(duration=1, interval=1 ,times=1, power=100)#2秒
            self.count+=1
        self.count=0
        #徐々に消える 300secs
        while not self.stop_event.is_set() or self.count>300:
            self.led.pwm(100-(100/300*self.count))
            self.count+=1
            sleep(1)
        self.led.off()

if __name__ == '__main__':    
    try:
        #ピン初期化。スイッチをトグル操作とする。
        pi=pigpio.pi()
        pi.set_mode(switch_pin, pigpio.INPUT)
        pi.set_pull_up_down(gpio=switch_pin, pud=pigpio.PUD_DOWN)
        pi.set_noise_filter(user_gpio=switch_pin, steady=200000, active=0)

        while True:
             #thread定義。init処理でLED offになる。
            led_th=LedThread(led_pin)
            pi.callback(user_gpio=switch_pin, edge=pigpio.RISING_EDGE,
                        func=led_th.led_callback)
            difference_time=get_time_difference()
            sleep(difference_time) #指定時刻までまつ
            led_th.start() #時刻になれば開始
            for i in range(5700): #led threadが動いている間止まるようにする
                sleep(1)
                if led_th.stop_event.is_set():break #stop eventフラグ立てば止める。
            sleep(1800) #30分経った時点で次の日の目覚まし開始。
    
    except:
        led_th.led.off()
        pi.stop()
        led_th.led.pi.stop()
    
#led_thread=threading.Thread(target=led_on)
#led_thread.start()
#
#time_difference=get_time_difference()
#sleep(time_difference)
#interval=int(30*60/100) #３０分＊６０秒　を１００で割る=18秒
#
#with LED(led_pin) as led:
#    for power in range(1, 101):
#        led.pwm(power)
#
#        for i in range(interval*2):
#            if pi.read(switch_pin, 1):
#                
#            sleep(0.5)
#    
#    led.on()
