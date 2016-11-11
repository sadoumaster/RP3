# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 23:14:01 2016

1/f波を作成します。
"""
from math import pi,sin
def curve_1f_generator(rad=2*pi, resolution=1000): 
#1／f波をジェネレーター形式で返す。メモリーの節約
    def curve(rad, i):
        return 2**(-i)*sin((2**i)*rad)

    for j in range(1, (resolution+1)):
        fx=0
        x=rad/resolution*j
        for i in range(10):
    
            fx += curve(x, i)
        yield fx

def curve_1f_list(rad=2*pi, resolution=100): 
#1／f波をリストで返す、resolutionを大きくしすぎるとメモリーパンクします
    def curve(rad, i):
        return 2**(-i)*sin((2**i)*rad)
    fx_list=[]
    for j in range(1, (resolution+1)):
        fx=0
        x=rad/resolution*j
        for i in range(10):
    
            fx += curve(x, i)
        fx_list.append(fx)
    return fx_list