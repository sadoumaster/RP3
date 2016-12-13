# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:23:05 2016

@author: user1
"""
import RPi.GPIO as GPIO
from time import sleep, time
def send_null():
    GPIO.output(data_pin, GPIO.HIGH)
    sleep(0.5*(10**-6))#0.35us
    GPIO.output(data_pin, GPIO.LOW)
    sleep(2.0*(10**-6))#1.36us

def send_1():
    GPIO.output(data_pin, GPIO.HIGH)
    sleep(1.2*(10**-6))
    GPIO.output(data_pin, GPIO.LOW)
    sleep(1.3*(10**-6))

def reset():
    GPIO.output(data_pin, GPIO.LOW)
    sleep(0.00005)

def make_data(R=0, G=0, B=0):
    bit_data=0x100
    bit_data|=R
    bit_data<<=8
    bit_data|=G
    bit_data<<=8
    bit_data|=B
    return bit_data
    
def send_bit(R=0, G=0, B=0):
    #色でbit_dataを変える。
#    if   color=='R': bit_data=R_led
#    elif color=='G': bit_data=G_led
#    elif color=='B': bit_data=B_led
#    elif color==0: bit_data=0
#    #bit_dataが0−255になければ、０か２５５にする。
#    if bit_data < 0: bit_data=0
#    elif bit_data >255: bit_data=255
    bit_data=make_data(R, G, B)
    for i in range(24):
        if bit_data & 0x800000:#16**6
            send_1()
        else:
            send_null()
        bit_data <<= 1

def on():
    send_bit(R_led, G_led, B_led)

def off():
    send_bit(0, 0, 0)

#0-255
R_led=255
G_led=0
B_led=0

data_pin=10

GPIO.setmode(GPIO.BCM)
GPIO.setup(data_pin, GPIO.OUT)

try:
    while True:
#    off()
#    print('off')

#        on()
        reset()
#    print('on')

#    off()
#    sleep(1)
#    for i in range(255):
#        R_led, G_led, B_led=i, 0, 0
#        on()
#        reset()
#        sleep(0.02)
#    for i in range(255):
#        R_led, G_led, B_led=0, i, 0
#        on()
#        reset()
#        sleep(0.02)
#    for i in range(255):
#        R_led, G_led, B_led=0, 0, i
#        on()
#        reset()
#        sleep(0.02)
#    for i in range(255):
#        R_led=i
#        for j in range(255):
#            G_led=j
#            for k in range(255):
#                B_led=k
#                on()
#                reset()
#                sleep(0.0001)
        off()

except KeyboardInterrupt:pass
finally:GPIO.cleanup()