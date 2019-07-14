# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Fri Jun 21 20:50:27 2019 
"""

import pyautogui
import time
import random
import rnd_ico


time.sleep(3)

# 
pyautogui.press('down')

pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

ico = rnd_ico.rnd_ico("PO")
pyautogui.typewrite(ico, interval=0.1)
pyautogui.press('tab')
pyautogui.press('tab')

#tel
pyautogui.typewrite("+420123456789", interval=0.1)
pyautogui.press('tab')

# pracovni pomer do
random_future_date = str(random.randint(1,28)) + "." + str(random.randint(1,12))  + "." + str(random.randint(2021,2025))
pyautogui.typewrite(random_future_date, interval=0.1)
pyautogui.press('tab')


#prohlaseni
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
