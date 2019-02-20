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

import data_spo
# import start

Ekp = namedtuple("Ekp", "key, etype, before, after") # element key + properties


def get_data(browser):
    gender_e = browser.find_element_by_id("__Gender")
    gender = gender_e.get_property("value")
    if (gender == "M"):
        values = data_spo.spo_m()
    elif (gender == "Z"):
         values = data_spo.spo_z()
    return values

values = get_data(browser)
app_values, app_address_values, emp_values, coapp_values, guar_values, vehicle_values, contract_values = values

def fill(browser):
    
    app_elements = {'TitleBefore': '__TitleBefore', 'Name': '__Name', 'Surname': '__Surname', 'TitleAfter': '__TitleAfter', 'MaritalStatus': '__MaritalStatus', 'Foreigner': '__Foreigner', 'DateOfBirth': '__DateOfBirth', 'PIN': '__PIN', 'Gender': '__Gender', 'Citizenship': '__Citizenship', 'BankAccountNumber1': '__BankAccountNumber1', 'BankAccountNumber': '__BankAccountNumber', 'BankCode': '__BankCode', 'DocumentType': '__DocumentType', 'DocumentNumber': '__DocumentNumber', 'DocumentValidTo': '__DocumentValidTo', 'SecondDocumentType': '__SecondDocumentType', 'SecondDocumentNumber': '__SecondDocumentNumber', 'SecondDocumentValidTo': '__SecondDocumentValidTo', 'PhoneNumber': '__PhoneNumber', 'Email': '__Email', "NRKISign":"__NRKISign"}
    
    app = [
    Ekp("TitleBefore", "txt", 0.1, 0.1),
    Ekp("Name", "txt", 0.1, 0.1),
    Ekp("Surname", "txt", 0.1, 0.1),
    Ekp("TitleAfter", "txt", 0.1, 0.1),
    Ekp("BankAccountNumber1", "txt", 0.1, 0.1),
    Ekp("BankAccountNumber", "txt", 0.1, 0.1),
    Ekp("BankCode", "dd", 0.1, 0.2),
    Ekp("DocumentType", "dd", 0.1, 0.2),
    Ekp("DocumentNumber", "txt", 0.1, 0.1),
    Ekp("DocumentValidTo", "txt", 0.1, 0.1),
    Ekp("SecondDocumentType", "dd", 0.1, 0.2),
    Ekp("SecondDocumentNumber", "txt", 0.1, 0.1),
    Ekp("SecondDocumentValidTo", "txt", 0.1, 0.1),
    Ekp("PhoneNumber", "txt", 0.1, 0.1),
    Ekp("Email", "txt", 0.1, 0.1),
    Ekp("MaritalStatus", "dd", 0.1, 0.2),
    Ekp("Gender", "dd", 0.1, 0.2),
    ]
             
    fill_elems(browser, app, app_elements, app_values )

    _section_udaje_zadatele = browser.find_element_by_xpath("//div[contains(text(),'Údaje žadatele')]")
    _section_udaje_zadatele.click()
       
    # Applicant Address    
    sleep(0.3)    
        
    app_address_elements =  {'HomeAddressStreet': '__HomeAddressStreet', 'HomeAddressCity': '__HomeAddressCity', 'HomeAddressZip': '__HomeAddressZip', 'HomeAddressState': '__HomeAddressState', 'AddressSame': None, 'AddressServicesStreet': '__AddressServicesStreet', 'AddressServicesCity': '__AddressServicesCity', 'AddressServicesZip': '__AddressServicesZip', 'AddressServicesState': '__AddressServicesState'}  
      
    app_address_1 = [
        Ekp("HomeAddressStreet", "txt", 0.1, 0.1),
        Ekp("HomeAddressCity", "txt", 0.1, 0.1),
        Ekp("HomeAddressZip", "txt", 0.1, 0.1),
        #Ekp("HomeAddressState", "dd", 0.2, 0.1),
        ]
    fill_elems(browser, app_address_1,  app_address_elements, app_address_values )

        
    _address_same= browser.find_element_by_name("__AddressSame")
    if (_address_same.is_selected()):        
        _address_same.click()
        sleep(0.5)
    #někdy se prostě na první pokus neotevře i přes sleep(2) proč ???
    if (_address_same.is_selected()):        
        sleep(0.4)
        print("druhý pokus otevřít koresp. adresu")
        _address_same.click()
        sleep(0.5)        
        
    if not (_address_same.is_selected()):
        app_address_2 = [
            Ekp("AddressServicesStreet", "txt", 0.1, 0.1),
            Ekp("AddressServicesCity", "txt", 0.1, 0.1),
            Ekp("AddressServicesZip", "txt", 0.1, 0.1),
            Ekp("AddressServicesState", "dd", 0.2, 0.1),
                ]
        fill_elems(browser, app_address_2, app_address_elements, app_address_values)    
    
        
    #Zdroj příjmů žadatele
    emp_elements = {'RegistrationNumber': '__RegistrationNumber', 'ProbationPeriod': '__ProbationPeriod', 'EmploymentIndefinitePeriod': '__EmploymentIndefinitePeriod', 'NoticePeriod': '__NoticePeriod', 'WorkPhoneNumber': '__WorkPhoneNumber', 'Foreigner': '__Emp_Foreigner', 'EmploymentIndefinitePeriodUntil': '__EmploymentIndefinitePeriodUntil'}
            
    emp = [
        Ekp("RegistrationNumber", "txt", 0.1, 0.1),
        Ekp("ProbationPeriod", "radio", 0.1, 0.1),
        Ekp("EmploymentIndefinitePeriod", "radio", 0.1, 0.2),
        Ekp("NoticePeriod", "radio", 0.1, 0.1),
        Ekp("WorkPhoneNumber", "txt", 0.1, 0.1),
        #Ekp("Foreigner", "cb", 0.1, 0.1),
        #Ekp("EmploymentIndefinitePeriodUntil", "txt", 0.1, 0.1),
            ]
    if emp_values["EmploymentIndefinitePeriod"] == "0": # pp na dobu určitou
        emp.append(Ekp("EmploymentIndefinitePeriodUntil", "txt", 0.1, 0.1))
        
    fill_elems(browser, emp, emp_elements, emp_values)
    
    _section_zdoj_prijmu = browser.find_element_by_xpath("//div[contains(text(),'Zdroj příjmů žadatele')]")
    _section_zdoj_prijmu.click()
    
    #Manžel/-ka žadatele
    sleep(0.3)
    
    
    coapp_elements = {'TitleBefore': '__CoA_TitleBefore', 'Name': '__CoA_Name', 'Surname': '__CoA_Surname', 'TitleAfter': '__CoA_TitleAfter', 'Foreigner': '__CoA_Foreigner', 'DateOfBirth': '__CoA_DateOfBirth', 'AverageMIAT': '__CoA_AverageMIAT', 'AddressServicesStreet': '__CoA_HomeAddressStreet', 'AddressServicesCity': '__CoA_HomeAddressCity', 'AddressServicesZip': '__CoA_HomeAddressZip', 'AddressServicesState': '__CoA_HomeAddressState'}
    
    _section_coapp = browser.find_element_by_xpath("//div[contains(text(),'Manžel/-ka žadatele')]")

    coapp = [
        Ekp("TitleBefore", "txt", 0.1, 0.1),
        Ekp("Name", "txt", 0.1, 0.1),
        Ekp("Surname", "txt", 0.1, 0.1),
        Ekp("TitleAfter", "txt", 0.1, 0.1),
        #Ekp("Foreigner", "cb", 0.1, 0.1),
        Ekp("DateOfBirth", "txt", 0.1, 0.1),
        #Ekp("AverageMIAT", "txt", 0.1, 0.1),          
            ]

    fill_elems(browser, coapp, coapp_elements, coapp_values)
    sleep(0.2)
    _section_coapp.click()
    
    #adresa spolužadatele
    sleep(0.5)
    _stejna_adr_zad = browser.find_element_by_xpath("//span[contains(text(),'Stejná jako u žadatele')]")
    _par = _stejna_adr_zad.find_element_by_xpath("..")
    _address_same = _par.find_element_by_name("__AddressSame")
    if (_address_same.is_selected()):        
        _address_same.click()
        sleep(0.5)
    if (_address_same.is_selected()):
        print("druhý pokus otevřít adresu t.b. spolužadatele")        
        _address_same.click()
        sleep(0.5)    
    
    if not (_address_same.is_selected()):
        coapp = [
        Ekp("AddressServicesStreet", "txt", 0.1, 0.1),
        Ekp("AddressServicesCity", "txt", 0.1, 0.1),
        Ekp("AddressServicesZip", "txt", 0.1, 0.1),
        Ekp("AddressServicesState", "dd", 0.1, 0.1),            
            ]
            
        fill_elems(browser, coapp, coapp_elements, coapp_values)
        sleep(0.1)
        _section_coapp.click()
    
    
    #Poptávkový list
    sleep(0.4)
       
    vehicle_elements = {"ExpectedDeliveryDate":"__ExpectedDeliveryDate"}
    
    vehicle = [Ekp("ExpectedDeliveryDate", "txt", 0.1, 0.1),]
    fill_elems(browser, vehicle, vehicle_elements, vehicle_values)
    
    
    contract_elements = {"RequestSign":"__RequestSign"}
    
    contract = [Ekp("RequestSign", "dd", 0.1, 0.1),]
    fill_elems(browser, contract, contract_elements, contract_values)
    
    app = [Ekp("NRKISign", "dd", 0.1, 0.1),]
    fill_elems(browser, app, app_elements, app_values )

    _section_poptavkovy_list = browser.find_element_by_xpath("//div[contains(text(),'Poptávkový list')]")
    _section_poptavkovy_list.click()
             
def fill_elems(browser, ekps, elements, values):
    for ekp in ekps:
        key = ekp.key
        elem_id = elements[key]
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
            rbs = browser.find_elements_by_name(elem_id) #podle jména !!!
            for rb in rbs:
                rbval = rb.get_attribute("value")
                if rbval == values[key]:
                    rb.click()



"""
browser.back() 
browser.get("http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/taskEdit.aspx?id=46938") 
fill(browser)

"""
