# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 12:23:05 2016

@author: user1
"""
import RPi.GPIO as GPIO
from time import sleep

def send_null():
    GPIO.output(data_pin, GPIO.HIGH)
    sleep(0.00000035)#0.35us
    GPIO.output(data_pin, GPIO.LOW)
    sleep(0.00000136)#1.36us

def send_1():
    GPIO.output(data_pin, GPIO.HIGH)
    sleep(0.00000136)
    GPIO.output(data_pin, GPIO.LOW)
    sleep(0.00000035)

def reset():
    GPIO.output(data_pin, GPIO.LOW)
    sleep(0.00005)

def send_bit(color):
    #色でbit_dataを変える。
    if   color=='R': bit_data=R_led
    elif color=='G': bit_data=G_led
    elif color=='B': bit_data=B_led
    elif color==0: bit_data=0
    #bit_dataが0−255になければ、０か２５５にする。
    if bit_data < 0: bit_data=0
    elif bit_data >255: bit_data=255
    for i in range(8):
        if bit_data & 0x80:
            send_1()
        else:
            send_null()
        bit_data <<= 1

def on():
    map(send_bit, ('R', 'G', 'B'))

def off():
    map(send_bit, (0, 0, 0))

#0-255
R_led=123
G_led=123
B_led=123

data_pin=23

GPIO.setmode(GPIO.BCM)
GPIO.setup(data_pin, GPIO.OUT)

try:
    on()
    sleep(5)
    off()
    sleep(1)
    for i in range(255):
        R_led, G_led, B_led=i, 0, 0
        on()
        reset()
        sleep(0.02)
    for i in range(255):
        R_led, G_led, B_led=0, i, 0
        on()
        reset()
        sleep(0.02)
    for i in range(255):
        R_led, G_led, B_led=0, 0, i
        on()
        reset()
        sleep(0.02)
    off()
except KeyboardInterrupt:
    GPIO.cleanup()