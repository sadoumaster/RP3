#!/usr/bin/env python
import sys
sys.path.append('/home/pi/Documents/PythonProjects/RP3/LED/rpi_ws281x/python/')
import time
import math
from neopixel import *

# LED strip configuration:
LED_COUNT      = 1
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# return Color(G, R, B)
def colorScaleBCGYR(value):
    tmp_val = math.cos( 4.0 * math.pi * value)
    col_val = int((-tmp_val / 2 + 0.5) * 255)
    if   (value >= (4.0 / 4.0)):
        color = Color ( 0, 255, 0 )
    elif (value >= (3.0 / 4.0)):
        color = Color ( col_val, 255, 0 )
    elif (value >= (2.0 / 4.0)):
        color = Color ( 255, col_val, 0 )
    elif (value >= (1.0 / 4.0)):
        color = Color ( 255, 0, col_val )
    elif (value >= (0.0 / 4.0)):
        color = Color ( col_val, 0, 255 )
    else:
        color = Color ( 0, 0, 255 )
    return color

def showLed(color):
    # without these 3 lines, pixel color is not correctly set. ???
    strip.setPixelColor(0, Color(0, 0, 0))
    strip.show()
    time.sleep(0.005)

    strip.setPixelColor(0, color)
    strip.show()

# Main program logic follows:
if __name__ == '__main__':
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    for i in range(256):
        strip.setPixelColor(0, Color(0, 0, i))
        strip.show()
        time.sleep(0.05)
    time.sleep(1)
#    print ('Press Ctrl-C to quit.')
#    for i in range(0, 61):
#        showLed(colorScaleBCGYR(i / 60.0))
#        time.sleep(0.1)
    strip.setPixelColor(0, Color(0, 0, 0))
    strip.show()