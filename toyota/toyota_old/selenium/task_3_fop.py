#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from collections import namedtuple
import datetime

import data_fop
import task_3_guar_fo
# import start

Ekp = namedtuple("Ekp", "key, eid, name, etype, before, after") # element key + properties


def fill(browser, data=None, gender="M", pin=None):
    if data is None:
        data = data_fop.get_data(gender=gender, pin=pin)
    
    app_firma_elements = [
        Ekp("TradeName", "__TradeName", "","txt",0.1,0.1),
        Ekp("TaxRegistrationNumber", "__TaxRegistrationNumber", "","txt",0.1,0.1),
        Ekp("RegistrationSectionNoEntrepre", "__RegistrationSectionNoEntrepre", "","txt",0.1,0.1),
        Ekp("RegistrationOfficeEntrepre", "__RegistrationOfficeEntrepre", "","txt",0.1,0.1),
    ]
    fill_elems(browser, app_firma_elements, data["applicant"] )
    
    
    _section_udaje_zadatele = browser.find_element_by_xpath("//div[contains(text(),'Firma')]")
    _section_udaje_zadatele.click()
    sleep(0.3)
    
    # udaje zadatele
    app_udaje_elements = [
        Ekp("TitleBefore", "__TitleBefore", "","txt",0.1,0.1),
        Ekp("Name", "__Name", "","txt",0.1,0.1),
        Ekp("Surname", "__Surname", "","txt",0.1,0.1),
        Ekp("TitleAfter", "__TitleAfter", "","txt",0.1,0.1),
        Ekp("BankAccountNumber1", "__BankAccountNumber1", "","txt",0.1,0.1),
        Ekp("BankAccountNumber", "__BankAccountNumber", "","txt",0.1,0.1),
        Ekp("BankCode", "__BankCode", "","dd",0.1,0.1),
        Ekp("DocumentType", "__DocumentType", "","dd",0.1,0.1),
        Ekp("DocumentNumber", "__DocumentNumber", "","txt",0.1,0.1),
        Ekp("DocumentValidTo", "__DocumentValidTo", "","txt",0.1,0.1),
        Ekp("SecondDocumentType", "__SecondDocumentType", "","dd",0.1,0.1),
        Ekp("SecondDocumentNumber", "__SecondDocumentNumber", "","txt",0.1,0.1),
        Ekp("SecondDocumentValidTo", "__SecondDocumentValidTo", "","txt",0.1,0.1),
        Ekp("PhoneNumber", "__PhoneNumber", "","txt",0.1,0.1),
        Ekp("Email", "__Email", "","txt",0.1,0.1),
        Ekp("MaritalStatus", "__MaritalStatus", "","dd",0.1,0.1),
        Ekp("Gender", "__Gender", "","dd",0.1,0.1),
    ]
             
    fill_elems(browser, app_udaje_elements, data["applicant"] )
    
    _section_udaje_zadatele = browser.find_element_by_xpath("//div[contains(text(),'Údaje žadatele')]")
    _section_udaje_zadatele.click()
    sleep(0.3)
    
    # Applicant Address    
    sleep(0.3)    
                  
    app_address_elements_1 = [
        Ekp("HomeAddressStreet", "__HomeAddressStreet", "","txt",0.1,0.1),
        Ekp("HomeAddressCity", "__HomeAddressCity", "","txt",0.1,0.1),
        Ekp("HomeAddressZip", "__HomeAddressZip", "","txt",0.1,0.1),
        #Ekp("HomeAddressState", "__HomeAddressState", "","dd",0.1,0.1),
        ]
    fill_elems(browser,  app_address_elements_1, data["applicant_address"] )
    
    
    _section_udaje_zadatele = browser.find_element_by_xpath("//div[contains(text(),'Adresa')]")
    _section_udaje_zadatele.click()
    sleep(0.1)
        
    _address_same= browser.find_element_by_name("__AddressSame")
    if (_address_same.is_selected()):        
        _address_same.click()
        sleep(0.5)
          
        
    if not (_address_same.is_selected()):
        app_address_elements_2 = [
            Ekp("AddressServicesStreet", "__AddressServicesStreet", "","txt",0.1,0.1),
            Ekp("AddressServicesCity", "__AddressServicesCity", "","txt",0.1,0.1),
            Ekp("AddressServicesZip", "__AddressServicesZip", "","txt",0.1,0.1),
            Ekp("AddressServicesState", "__AddressServicesState", "","dd",0.1,0.1),
                ]
        fill_elems(browser, app_address_elements_2, data["applicant_address"])    
    
    _section_udaje_zadatele = browser.find_element_by_xpath("//div[contains(text(),'Adresa')]")
    _section_udaje_zadatele.click()
    sleep(0.1)
    
    #Bonita
    
    #Manžel/-ka žadatele
    sleep(0.3)
        
    _section_coapp = browser.find_element_by_xpath("//div[contains(text(),'Manžel/-ka žadatele')]")
    
    coapp_elements = [
        Ekp("TitleBefore", "__CoA_TitleBefore", "","txt",0.1,0.1),
        Ekp("Name", "__CoA_Name", "","txt",0.1,0.1),
        Ekp("Surname", "__CoA_Surname", "","txt",0.1,0.1),
        Ekp("TitleAfter", "__CoA_TitleAfter", "","txt",0.1,0.1),
        #Ekp("Foreigner", "__CoA_Foreigner", "","cb",0.1,0.1),
        Ekp("DateOfBirth", "__CoA_DateOfBirth", "","txt",0.1,0.1),
        #Ekp("AverageMIAT", "__CoA_AverageMIAT", "","txt",0.1,0.1),         
            ]
    
    fill_elems(browser, coapp_elements, data["coapplicant"])
    sleep(0.2)
    _section_coapp.click()
    sleep(0.3)
    # Guarantor 
    # ano / ne - je uloženo v applicant
    app_elements = [Ekp("IsDebtor", "", "__IsDebtor", "radio", 0.1, 0.1),]
    fill_elems(browser, app_elements, data["applicant"])
    
    if data["applicant"]["IsDebtor"] == "1":
        sleep (0.3)
        task_3_guar_fo.fill(browser, data)
    
    
    #Poptávkový list
    sleep(0.4)
           
    vehicle_elements = [Ekp("ExpectedDeliveryDate", "__ExpectedDeliveryDate", "", "txt", 0.1, 0.1),]
    fill_elems(browser, vehicle_elements, data["vehicle"])
    
    
    contract_elements = [Ekp("RequestSign", "__RequestSign", "", "dd", 0.1, 0.1),]
    fill_elems(browser,  contract_elements, data["contract"])
    
    app_elements = [Ekp("NRKISign", "__NRKISign", "", "dd", 0.1, 0.1),]
    fill_elems(browser, app_elements, data["applicant"] )
    
    _section_poptavkovy_list = browser.find_element_by_xpath("//div[contains(text(),'Poptávkový list')]")
    _section_poptavkovy_list.click()
    
    #prilohy
    _prilohy_lst = browser.find_elements_by_xpath("//div[contains(text(), 'Přílohy')]")
    if len(_prilohy_lst) > 0:
    
        label_ns_lst = browser.find_elements_by_xpath(".//label[contains(text(), 'Nahrát Soubor')]")
        _first_time = True
        for label in label_ns_lst:
            op_btn = label.find_element_by_xpath("../input")
            op_btn.send_keys(r"c:\temp\wolf_small.jpg")
            vlozit_btn = label.find_element_by_xpath("../span/input")
            vlozit_btn.click()
            if _first_time:
                sleep(0.5)
                _first_time = False
            sleep(0.5)    
        
        Coapp_AttachmentNote = browser.find_element_by_id("__Coapp_AttachmentNote")
        Coapp_AttachmentNote.send_keys("uživatelská poznámka")        
        
        #_prilohy_lst[0].click()

    _section_poptavkovy_list.click()
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)

             
def fill_elems(browser, elements, values):
    for ekp in elements:
        key = ekp.key
        elem_id = ekp.eid
        elem_name = ekp.name
        if ekp.etype == "txt":
            elem = browser.find_element_by_id(elem_id)  #podle id
            elem.clear()
            sleep(ekp.before)
            elem.send_keys(values[key])
            sleep(ekp.after)            
        elif ekp.etype == "dd":
            elem = browser.find_element_by_id(elem_id) #podle id
            sleep(ekp.before)
            Select(elem).select_by_value(values[key])
            sleep(ekp.after)
        elif ekp.etype == "cb":
            pass
        elif ekp.etype == "radio":
            rbs = browser.find_elements_by_name(elem_name) #podle jména !!!
            for rb in rbs:
                rbval = rb.get_attribute("value")
                if rbval == values[key]:
                    rb.click()

    

"""
browser.back() 
browser.get("http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/taskEdit.aspx?id=46938") 
fill(browser)


"IsDebtor": "1"
"""
