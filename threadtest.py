# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:04:26 2017

@author: user1
"""

import threading
from time import sleep

class TestTh(threading.Thread):
    def __init__(self):
        super().__init__()
        self.stop_event=threading.Event()
        self.setDaemon(True)
        
    def stop(self):
        self.stop_event.set()
        
    def countup(self):
        self.count=0
        while True:
            print(self.count)
            sleep(0.5)
            self.count+=1
            
    def run(self):
        self.count=0
        while not self.stop_event.is_set():
            print(self.count)
            sleep(0.5)
            self.count+=1
        print('end')

th=TestTh()
th.start()
sleep(10)
th.stop()