#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from time import sleep


def open_browser():
    browser = webdriver.Chrome()
    web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
    browser.get(web_app)
    return browser, web_app

def login(browser):
    try:
        usr = browser.find_element_by_id('txtUsername')
        pwd = browser.find_element_by_id('txtPassword')
        log_in = browser.find_element_by_id('btnLogin')
        
        usr_val = "cis\\m.houska"
        pwd_val = "heslo"
        
        sleep(0.2)
        usr.send_keys(usr_val)
        pwd.send_keys(pwd_val)
        sleep(0.2)
        log_in.click()
        print("tried to log in")
    except:
        print("problem with login or already logged in")
    

