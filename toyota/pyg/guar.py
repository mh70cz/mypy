# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Fri Jun 21 17:42:55 2019 
"""

import pyautogui
import time
import random


#screenWidth, screenHeight = pyautogui.size()
#currentMouseX, currentMouseY = pyautogui.position()
#print(currentMouseX, currentMouseY)
#pyautogui.moveTo(currentMouseX + 100, currentMouseY + 150)


jmeno = "Gabriela"
prijmeni = "Garantujici"
rc = "8456215405"
datnar = "21.6.1984"
email = "gabriela.garantujici@garant.cz"

time.sleep(3)

#titul
pyautogui.typewrite("JUDr", interval=0.1)
pyautogui.press('tab')
pyautogui.press('tab')

#jmeno
pyautogui.typewrite(jmeno, interval=0.1)
pyautogui.press('tab')

#RC
pyautogui.typewrite(rc, interval=0.1)
pyautogui.press('tab')

#Prijmeni
pyautogui.typewrite(prijmeni, interval=0.1)
pyautogui.press('tab')

#datnar
pyautogui.typewrite(datnar, interval=0.1)
pyautogui.press('tab')

#titul pred
pyautogui.typewrite("MBA", interval=0.1)
pyautogui.press('tab')

# pohlavi
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')

#tel
pyautogui.typewrite("+420123456789", interval=0.1)
pyautogui.press('tab')

#email
pyautogui.typewrite(email, interval=0.1)
pyautogui.press('tab')

#typ 1. dokladu
pyautogui.press('down')
pyautogui.press('tab')

# predcisli bank. uctu
pyautogui.typewrite("35", interval=0.1)
pyautogui.press('tab')

# cislo prvniho dokladu
pyautogui.typewrite(str(random.randint(111111111,999999999)), interval=0.1)
pyautogui.press('tab')

#cislo uctu
pyautogui.typewrite(str(random.randint(111111111,999999999)), interval=0.1)
pyautogui.press('tab')

# platnost 1. dokladu do
random_future_date = str(random.randint(1,28)) + "." + str(random.randint(1,12))  + "." + str(random.randint(2021,2025))
pyautogui.typewrite(random_future_date, interval=0.1)

# kod banky
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('tab')

# typ 2. dokladu
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('tab')
# cislo 2. dokladu
pyautogui.typewrite(str(random.randint(111111111,999999999)), interval=0.1)
pyautogui.press('tab')


# cislo 2. dokladu
random_future_date = str(random.randint(1,28)) + "." + str(random.randint(1,12))  + "." + str(random.randint(2021,2025))
pyautogui.typewrite(random_future_date, interval=0.1)
pyautogui.press('tab')


