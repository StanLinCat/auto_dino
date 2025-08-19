# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:08:12 2019

@author: stan lin
"""

#! python3
import pyautogui, sys
import time
from pynput.keyboard import Key, Listener

def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False


print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + '   Y:' + str(y).rjust(4)
        print(positionStr, end=' \n')
        print('\b' * len(positionStr), end='', flush=True)
        on_release=on_release
        time.sleep( 1 )
except KeyboardInterrupt:  
    print('\n')