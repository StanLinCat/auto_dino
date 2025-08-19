# -*- coding: utf-8 -*-
"""
 Created on Thu May 16 15:06:39 2019    

1!@author: stan lin3j030 0 
"""

from pynput.keyboard import Key, Listener

def on_press1(key):
    print('{0} pressed'.format(key))  

def on_release1(key):     
    print('{0} release'.format(key))        
    if key == Key.esc:
        # Stop listener
        return False
    
def on_release(key):
    global keyCapture
    keyCapture = key
    A.append(keyCapture) 
    if key == Key.esc:
        # Stop listener
        return False

    # print(keyCapture)
# Collect events until released
A=[]
with Listener(on_press=None,on_release=on_release) as listener:
    listener.join()


#    
print(A)



##            dddd    dddddddddddd4444444dddddddddsvdf cat   i am awesome stan is good   ewrqfdscfef        123456789123456789heloo my name is stan lin


