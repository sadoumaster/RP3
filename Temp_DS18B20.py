# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 22:22:30 2016

@author: Toru

GPIO4にDS18B20を接続してプルアップ抵抗として、4.7k〜10kΩを電源3.3VとGPIO4に繫ぐ
read_temp() で温度取得。
"""
import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

# 生の温度データを取得する関数
def read_temp_raw():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    return lines

# 温度データのみを取り出して返す関数
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
#        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c#, temp_f


if __name__=='__main__':
    try:
        while True:
            print('{}℃'.format(read_temp()))
            time.sleep(5)
    except KeyboardInterrupt:
        pass