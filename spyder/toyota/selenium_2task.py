#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time


#
#browser = webdriver.Chrome()
#web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
#browser.get(web_app)




time.sleep(0.2)
Select(browser.find_element_by_id("__EmployerType")).select_by_value("1")
time.sleep(0.2)
Select(browser.find_element_by_id("__MainIncomeType")).select_by_value("0")
browser.find_element_by_id("__AverageMIAT").send_keys("45000")

browser.find_element_by_id("__OtherIncomeType").send_keys("Pronájem nemovitosti")
time.sleep(0.2)
browser.find_element_by_id("__OtherIncomeAmount").send_keys("3450")

  

time.sleep(0.2)
Select(browser.find_element_by_id("__TypeOfHousing")).select_by_value("1")

time.sleep(0.2)
Select(browser.find_element_by_id("__IsLiabilities")).select_by_value("1")
time.sleep(0.2)
browser.find_element_by_id("__Liabilities").send_keys("512")

    


Select(browser.find_element_by_id("__Spoluzadatel")).select_by_value("1")
time.sleep(0.2)

browser.find_element_by_id("__CoAverageMIAT").send_keys("34000")


browser.find_element_by_id("__HouseholdNumberPersons").send_keys("5")

deti = ["__NumberDependentPersons",
        "__NumberDependentPersons1",
        "__NumberDependentPersons2",
                      ]
for d in deti:
    browser.find_element_by_id(d).send_keys("1")




browser.find_element_by_id("__DateOfBirth").send_keys("15.3.1970")
#time.sleep(0.2)
#browser.find_element_by_id("__DateOfBirth").send_keys(Keys.ENTER)
#browser.find_element_by_id("__DateOfBirth").send_keys(Keys.ENTER)

browser.find_element_by_id("__PIN").send_keys("7003150044")

Select(browser.find_element_by_id("__Gender")).select_by_value("M")


b_prepocitat = browser.find_element_by_xpath('//button[contains(text(), "' + "PŘEPOČÍTAT" + '")]')
time.sleep(1)
b_prepocitat.click()
