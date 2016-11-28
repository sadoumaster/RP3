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
    if   color=='R': bit_data=R_led
    elif color=='G': bit_data=G_led
    elif color=='B': bit_data=B_led
    elif color==0: bit_data=0
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
except KeyboardInterrupt:
    GPIO.cleanup()