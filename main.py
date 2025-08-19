# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:40:25 2019

@author: stan lin
"""
from imagesearch import *
import time
import pyautogui
from pynput.keyboard import Key, Controller
keyboard = Controller()

####第一個遊戲所需圖片     *0.6464   or   /0.66
#image0="img/flag_start.png"
#image1="img/pancake.png"
#image2="img/drink.png"
#clockSet1=65#遊戲進行時間s

###第二個遊戲所需圖片
image3="img/disconnect1.png"
image4="img/cactus.png"
image5="img/fly1.png"
image6="img/fly2.png"
image7="img/restart.png"
clockSet2=600#遊戲進行時間s

timesample=0.1#取樣週期
precision=0.8 #精確度


## In[] 開始第一個遊戲

#time.sleep( 1 )
#pyautogui.click(262, 1055)#Chorme位置
#time.sleep( 0.1 )
#pyautogui.click(126, 17)#第一視窗
#pyautogui.click(88, 55) #refreshing
#time.sleep( 3 )
##
#pos = imagesearch(image0, precision)
#while pos[0] == -1:
#    print(image0+" not found, waiting")
#    time.sleep(timesample)
#    pos = imagesearch(image0, precision)
#print(image0+" found ", pos[0], pos[1])
#click_image(image0,pos,"left",1)
#pyautogui.moveTo(pos[0] +100 , pos[1] +100 ,1)
#
## In[] 進行第一個遊戲
#
#x1=812
#y1=653
#x2=1125
#y2=839
#tStart = time.time()#計時開始
#clock=0.0
#pos1 = imagesearch(image1, precision)
#pos2 = imagesearch(image2, precision)
#while clock<clockSet1:
#    clock=time.time()-tStart
#    pos1 = imagesearcharea(image1,x1,y1+55,x2,y2, precision)
#    pos2 = imagesearcharea(image2,x1+55,y1+30,x2,y2, precision)
#    if pos1[0] != -1 and pos2[0] == -1:
#        print(image1+" found ", pos1[0], pos1[1])
#        keyboard.press(Key.left)
#    elif pos2[0] != -1 and pos1[0] == -1:
#        print(image2+" found ", pos2[0], pos2[1])
#        keyboard.press(Key.right)  
#    elif pos2[0] == -1 and pos1[0] == -1:
#        keyboard.release(Key.right)
#        keyboard.release(Key.left) 
#print("over")
#keyboard.release(Key.right)
#keyboard.release(Key.left)
#
## In[] 開始第二個遊戲
# 
#time.sleep( 1 )
#pyautogui.click(334, 22)
#time.sleep( 0.1 )
#pyautogui.click(104, 59)
#
#pos = imagesearch(image3, 0.5)
#while pos[0] == -1:
#    print(image3+" not found, waiting")
#    time.sleep(timesample)
#    pos = imagesearch(image3, 0.5)
#print(image3+" found ", pos[0], pos[1])
##click_image(image3,pos,"left",1)
#keyboard.press(Key.space)
#pyautogui.moveTo( 1869 , 206 , 1 )
#keyboard.release(Key.space)

# In[] 進行第二個遊戲

x1=300#找仙人掌的範圍
y1=570
x2=580  #850
y2=762
tStart = time.time()#計時開始
clock=0.0
while clock<clockSet2:
    clock=time.time()-tStart
    pos1 = imagesearcharea(image4,x1,y1,x2,y2, precision)
#    pos2 = imagesearcharea(image5,x1,498,x2,498+100, precision)
#    pos3 = imagesearcharea(image5,x1-100,722-100,x2,722, precision)
#    pos4 = imagesearcharea(image6,x1,498,x2,498+100, precision)
#    pos5 = imagesearcharea(image6,x1-100,722-100,x2,722, precision)
    if pos1[0] != -1 :
        print(image4+" found ", pos1[0], pos1[1])
        #keyboard.release(Key.down)
        keyboard.press(Key.up)
        time.sleep(timesample)
        #keyboard.release(Key.up)  
#    elif pos2[0] != -1 or pos4[0] != -1:
#        print(image5+" found ", pos2[0], pos2[1])
#        keyboard.press(Key.up)
#        time.sleep(timesample)
#        keyboard.release(Key.up)
#    elif pos3[0] != -1 or pos5[0] != -1:
#        print(image5+" found ", pos3[0], pos3[1])
#        keyboard.press(Key.down)
#        time.sleep(timesample)
    else:
        keyboard.release(Key.up)
        #keyboard.press(Key.down)
        print("not found, waiting")
print("over")







