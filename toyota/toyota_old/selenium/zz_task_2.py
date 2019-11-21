#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import random 

import start
import r_rc_ico

#
"""
browser, web_app = start.open_browser()
start.login(browser)

#http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/processDetail.aspx?id=7537
#http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/TaskEdit.aspx?id=46889
"""
def init(browser, web_app, task_id):
    web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
    web_task_edit = "Processing/TaskEdit.aspx?id="
    #task_id = "46889"  #46889  46891  46889
    browser.get(web_app + web_task_edit + task_id)
    
    sleep(2)
    subj_type_dd = browser.find_element_by_id("__SubjType")
    sleep(0.3)
    subj_type = subj_type_dd.get_attribute("value")
    
    
    if subj_type == "1":
        fill_spo(browser)        
    elif subj_type == "2":
        fill_fop(browser)        
    elif subj_type == "3":
        fill_po(browser)
        

def fill_spo(browser, data=None):
    
    sleep(0.4)
    if data is None:
        data = get_data()
        
    #  Doplňující údaje o vozidle    
    dopl_udaje_voz(browser, data)
    
       
    # Základní data pro identifikaci žadatele        
    sleep(0.3)
    subj_type_elem = browser.find_element_by_id("__SubjType")
    Select( subj_type_elem).select_by_value("1")        
    
    sleep(0.3)    
    sex, pin, dat_nar = r_rc_ico.rc_dat()
    pin_elem = browser.find_element_by_id("__PIN1")
    pin_elem.clear()
    sleep(0.1)
    pin_elem.send_keys(pin)
        
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)
    

    
def fill_fop(browser, data=None):
    
    sleep(0.4)
    
    if data is None:
        data = get_data()
    
    
    #  Doplňující údaje o vozidle    
    dopl_udaje_voz(browser, data)
    
    sleep(0.3)
    subj_type_elem = browser.find_element_by_id("__SubjType")
    Select( subj_type_elem).select_by_value("2")       
    
    sleep(0.3)    
    sex, pin, dat_nar = r_rc_ico.rc_dat()
    pin_elem = browser.find_element_by_id("__PIN2")
    pin_elem.clear()
    sleep(0.1)
    pin_elem.send_keys(pin)
    sleep(0.1)
          
    ico = r_rc_ico.r_ico()
    ico_f = browser.find_element_by_id("__RegistrationNumber2")
    ico_f.clear()
    sleep(0.1)
    ico_f.send_keys(ico)
    sleep(0.1)
    
    
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)
    

def fill_po(browser, data=None):   
           
    sleep(0.4)
    if data is None:
        data = get_data()
            
    #  Doplňující údaje o vozidle    
    dopl_udaje_voz(browser, data)

    sleep(0.3)
    subj_type_elem = browser.find_element_by_id("__SubjType")
    Select( subj_type_elem).select_by_value("3")

    sleep(0.3)
    ico_f = browser.find_element_by_id("__RegistrationNumber3")
    ico = r_rc_ico.r_ico()
    ico_f.clear()
    sleep(0.1)
    ico_f.send_keys(ico)
    sleep(0.1)
   
    
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)
    
    
    
def fill_numeric_fields (browser, vykazy):    
    for v in vykazy:
        field = browser.find_element_by_id(v[0])
        sleep(0.1)
        field.clear()
        sleep(0.1)
        field.send_keys(str(int(v[1])))
        sleep(0.1)
    

def prepocitat(browser):
    """for numeric (no leading 0 ) fields (konverted to int)"""
    b_prepocitat = browser.find_element_by_xpath('//button[contains(text(), "' + "PŘEPOČÍTAT" + '")]')
    sleep(1)
    b_prepocitat.click()

def dopl_udaje_voz(browser, data):
    """ Doplňující údaje o vozidle    """

    _section_doplnujici_udaje_lst = browser.find_elements_by_xpath("//div[contains(text(),'Doplňující údaje o vozidle')]")
    if (len(_section_doplnujici_udaje_lst) > 0 and 
        _section_doplnujici_udaje_lst[0].is_displayed()):
        _section_doplnujici_udaje_lst[0].click()
        
        vin_elem = browser.find_element_by_id("__VIN")
        vin_elem.clear()
        sleep(0.1) 
        vin_elem.send_keys(data["vehicle"]["VIN"])
        sleep(0.1)
        
        tpno_elem = browser.find_element_by_id("__RegistrationBookNo")
        tpno_elem.clear()
        sleep(0.1) 
        tpno_elem.send_keys(data["vehicle"]["RegistrationBookNo"])
        sleep(0.1)


        regno_elem = browser.find_element_by_id("__VehicleRegistrationMark")
        regno_elem.clear()
        sleep(0.1) 
        regno_elem.send_keys(data["vehicle"]["VehicleRegistrationMark"])
        sleep(0.1)

        mnfyear_elem = browser.find_element_by_id("__YearOfManufacture")
        mnfyear_elem.clear()
        sleep(0.1) 
        mnfyear_elem.send_keys(data["vehicle"]["YearOfManufacture"])
        sleep(0.1)      
        
        _section_doplnujici_udaje_lst[0].click()
        sleep(0.3)

def get_data():
    

    data = {
            "applicant":{},
            "contract":{},
            "vehicle":{
                    "VehicleStatus":"1", # nové 1 , ojeté 0
                    "VIN": "2T2BK1BA5CC150528",
                    "RegistrationBookNo":"TP27182",
                    "VehicleRegistrationMark":"6S61234",
                    "YearOfManufacture":"2018",
                    },
            }  
            
    return data
   

"""
for i in range(20):
    init(browser, web_app)
    sleep(1)
    browser.back()
    sleep(0.5)
    
"""