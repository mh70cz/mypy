#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome()
web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
browser.get(web_app)

def login():
    try:
        usr = browser.find_element_by_id('txtUsername')
        pwd = browser.find_element_by_id('txtPassword')
        log_in = browser.find_element_by_id('btnLogin')
        
        usr_val = "cis\\m.houska"
        pwd_val = "heslo"
        
        time.sleep(0.2)
        usr.send_keys(usr_val)
        pwd.send_keys(pwd_val)
        time.sleep(0.2)
        log_in.click()
        print("tried to log in")
    except:
        print("problem with login or already logged in")
    

    

"""
<a href="Processing/processStart.aspx?definitionID={AB260856-E6EA-42D4-998C-175099591E9A}" target="mainFrame" class="AspNet-Menu-Link">
								<img src="App_Themes/Toyota/images/icons/ico_app_new.png" alt="Nová žádost – financování" class="Menu-ico">Nová žádost – financování
							</a>

http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/processList.aspx
"""

def fillscreen():
    nova_zadost_url = "Processing/processStart.aspx?definitionID={AB260856-E6EA-42D4-998C-175099591E9A}"
    browser.get(web_app + nova_zadost_url)
    time.sleep(3)
    
    
    subj_type = "SPO"
    prod_type = "OL"
    
    
    
    label_fc = browser.find_element_by_xpath('//span[contains(text(), "' + "úvěr" + '")]')
    label_fo = browser.find_element_by_xpath('//span[contains(text(), "' + "operativní leasing" + '")]')
    
    #label_f0.click()
    
    label_nove = browser.find_element_by_xpath('//span[contains(text(), "' + "nové" + '")]')
    label_ojete = browser.find_element_by_xpath('//span[contains(text(), "' + "ojeté" + '")]')
    
    
    #vyrobce = browser.find_element_by_id("__VehicleMaker")
    #Select(vyrobce).select_by_value("L") #Lexus
    
    time.sleep(0.2)
    model_type = browser.find_element_by_id("__VehicleModelType")
    Select(model_type).select_by_value("AUHTS")
    
    time.sleep(0.2)
    model = browser.find_element_by_id("__VehicleModel")
    Select(model).select_by_value("000636")
    
    time.sleep(0.2)
    equipment = browser.find_element_by_id("__EquipmentLevel")
    Select(equipment).select_by_value("CT__AUHTSMC15_T0006363L__")
    
    time.sleep(0.2)
    subj_type = browser.find_element_by_id("__SubjType")
    Select(subj_type).select_by_value("1")
    
    time.sleep(0.2)
    dealer = browser.find_element_by_id("__TFSCDealer")
    Select(dealer).select_by_value("1373")
    
    time.sleep(0.2)
    campaign = browser.find_element_by_id("__CampaignCode")
    time.sleep(0.5)
    #Select(campaign).select_by_value("KAMPAN_PRO_FO_RENT_V_15_064") #FO
    Select(campaign).select_by_value("KAMPAN_PRO_FC_VARIO_V_15_X02") #FC
    
    
    time.sleep(0.2)
    pocet_mesicu = browser.find_element_by_id("__NoOfInstalmentsMax")
    Select(pocet_mesicu).select_by_index(1)
    
    time.sleep(0.2)
    rocni_najezd = browser.find_element_by_id("__StepMileAgePerYear")
    Select(rocni_najezd).select_by_index(1)
    
    pojisteni = ["__InsuranceCoName", "__MTPLInsuranceLimits", "__InsuranceCoNameMotor", "__MotorInsuranceParticipation"]
    for p in pojisteni:
        time.sleep(0.2)
        Select(browser.find_element_by_id(p)).select_by_index(1)
        
    
    time.sleep(0.2)
    id_zadosti = browser.find_element_by_id("__IdentificationRequest")
    id_zadosti.send_keys(f"mh {prod_type} ; tsts ; nové")

#
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from pathlib import Path
#import csv
#import datetime
#import os
#import time
#import sys
#
#
#opts = Options()
#opts.set_headless(False)
#
#
#'''
#When Page Loading takes too much time and you need to stop downloading 
#additional subresources (images, css, js etc) you can change 
#the  pageLoadStrategy through the webdriver.
#'''
#caps = DesiredCapabilities().FIREFOX
#caps["pageLoadStrategy"] = "eager"  #  interactive
## caps["pageLoadStrategy"] = "normal"  #  complete
## caps["pageLoadStrategy"] = "none"   #  undefined
#    
#browser = Firefox(options=opts, capabilities=caps)
#browser.implicitly_wait(2) # seconds
## An implicit wait tells WebDriver to poll the DOM 
## for a certain amount of time when trying to find 
## any element (or elements) not immediately available. 
## The default setting is 0. Once set, 
## the implicit wait is set for the life of the WebDriver object.
#
#
#def get_password():
#    home =  str(Path.home())
#    pwd_file = home + '/Documents/local_info/selenium_appmulti_prev.txt'
#    pwd_val = ''
#    try:
#        with open(pwd_file, "r", encoding = "utf8") as f:
#            pwd_val = f.readline()
#    except Exception as e:
#        print(e)
#        print('try insert password manually:')
#        pwd_val = input("Password: ")
#    return pwd_val
#
#
#def gc_log_in(url, usr_val='cis.admin', pwd_val=''):
#    if pwd_val == "":
#        pwd_val = get_password()
#    print('try to log in')        
#    browser.get(url)
#    usr = browser.find_element_by_id('Username')
#    pwd = browser.find_element_by_id('Password')
#    log_in = browser.find_element_by_class_name('btn-primary')
#    usr.send_keys(usr_val)
#    pwd.send_keys(pwd_val)
#    log_in.click()
#    
#    try:
#        ddtoggles = browser.find_elements_by_class_name('dropdown-toggle')
#        for ddt in ddtoggles:
#            # print('ddt: ' + str(ddt.text))
#            if 'cis' in ddt.text and 'admin' in ddt.text:
#                print("logged OK")
#                return True
#        print('not logged')
#        return False
#    except Exception as e:
#        print(e)
#        return False
#
#init_url = 'http://appmultipreview/idmken'
#
#subject_id = '14161673902'
#strategy_type = 'Companies' #contains text
#strategy_name = 'Atlas' #contains text
#
#browser.get(init_url)
#if 'sign-in' in browser.current_url:
#    if gc_log_in(init_url):
#        pass
#    else:
#        sys.exit('not able to log , exiting')
#
#
## url is remmaped by webserver e.g. https://cishd-mc-pre01.cis.local/.......        
#current_url = browser.current_url 
#url_pre = current_url[:current_url.rfind("/")]
#
#browser.get(url_pre + '/NewQuery')
#time.sleep(1)
##strategy type
#links = browser.find_elements_by_tag_name('a')
#for link in links:
#    if strategy_type in link.text:
#        link.click()
#time.sleep(1)
##strategy name
#elems = browser.find_elements_by_tag_name('td')
#for e in elems:
#    if strategy_name in e.text:
#        e.click()
#
#id = browser.find_element_by_id("Cb5SearchParameters.RegistrationNumber-1")
#id.send_keys(subject_id)
#consent = browser.find_element_by_id("Consent-1") # consent checkbox
#if consent.is_selected() == False:
#    consent.click()
#browser.find_element_by_id("submit-query-btn").click()
#time.sleep(1)
## open report
#tds = browser.find_elements_by_tag_name("td")
#for td in tds:
#    if subject_id in td.text:
#        td.click()
#        break
#    
#    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
