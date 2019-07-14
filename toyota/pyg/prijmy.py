# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Fri Jun 21 21:36:14 2019 
"""

import pyautogui
import time
import random



time.sleep(3)


#prijmy

# mzda
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
time.sleep(0.1)

pyautogui.press('tab')
#
#
random_salary = str(random.randint(45000,85000))
time.sleep(0.5)
pyautogui.typewrite(random_salary, interval=0.1)
pyautogui.press('tab')

# jiny prijem
pyautogui.typewrite("Pronajem", interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite("8000", interval=0.1)
pyautogui.press('tab')

# bydleni
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')

# mate uver
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')
pyautogui.typewrite("200", interval=0.1)
pyautogui.press('tab')

# pocet osob
pyautogui.typewrite("5", interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite("1", interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite("1", interval=0.1)
pyautogui.press('tab')
pyautogui.typewrite("1", interval=0.1)
pyautogui.press('tab')
