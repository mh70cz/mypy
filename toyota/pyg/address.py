# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Fri Jun 21 19:11:28 2019 
"""


import pyautogui
import time
import random

street = "Rucitelu 2"
city = "Horni Rucitelov"
zip_ = "23456"

time.sleep(3)

#ulice
pyautogui.typewrite(street, interval=0.1)
pyautogui.press('tab')

# mesto
pyautogui.typewrite(city, interval=0.1)
pyautogui.press('tab')


#psc
pyautogui.typewrite(zip_, interval=0.1)
pyautogui.press('tab')

