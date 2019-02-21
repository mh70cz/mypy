# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 12:36:35 2019

@author: mh70
"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from collections import namedtuple
import datetime

import data_guar_fo

Ekp = namedtuple("Ekp", "key, eid, name, etype, before, after") # element key + properties

def fill(browser):
    values = data_guar_fo.guar_values
    
    guar_fo_elements = [
        Ekp("SubjType", "__Deb_SubjType","", "dd", 0.1, 0.1 ),
        Ekp("TitleBefore", "__Deb_TitleBefore","", "txt", 0.1, 0.1 ),
        Ekp("Name", "__Deb_Name","", "txt", 0.1, 0.1 ),
        Ekp("Surname", "__Deb_Surname","", "txt", 0.1, 0.1 ),
        Ekp("TitleAfter", "__Deb_TitleAfter","", "txt", 0.1, 0.1 ),
        Ekp("PhoneNumber", "__Deb_PhoneNumber","", "txt", 0.1, 0.1 ),
        Ekp("Email", "__Deb_Email","", "txt", 0.1, 0.1 ),
        Ekp("BankAccountNumber1", "__Deb_BankAccountNumber1","", "txt", 0.1, 0.1 ),
        Ekp("BankAccountNumber", "__Deb_BankAccountNumber","", "txt", 0.1, 0.1 ),
        Ekp("BankCode", "__Deb_BankCode","", "dd", 0.1, 0.1 ),
        Ekp("Foreigner", "__Deb_Foreigner","", "cb", 0.1, 0.1 ), # ToDo
        Ekp("PIN", "__Deb_PIN","", "txt", 0.1, 0.1 ),
        Ekp("DateOfBirth", "__Deb_DateOfBirth","", "txt", 0.1, 0.1 ),
        Ekp("Gender", "__Deb_Gender","", "dd", 0.1, 0.1 ),
        Ekp("Citizenship", "__Deb_Citizenship","", "dd", 0.1, 0.1 ), 
        Ekp("DocumentType", "__Deb_DocumentType","", "dd", 0.1, 0.1 ),
        Ekp("DocumentNumber", "__Deb_DocumentNumber","", "txt", 0.1, 0.1 ),
        Ekp("DocumentValidTo", "__Deb_DocumentValidTo","", "txt", 0.1, 0.1 ),
        Ekp("SecondDocumentType", "__Deb_SecondDocumentType","", "dd", 0.1, 0.1 ),
        Ekp("SecondDocumentNumber", "__Deb_SecondDocumentNumber","", "txt", 0.1, 0.1 ),
        Ekp("SecondDocumentValidTo", "__Deb_SecondDocumentValidTo","", "txt", 0.1, 0.1 ),      
            ]
    
    fill_elems(browser, guar_fo_elements, values)
    
    _section_guar_udaje = browser.find_element_by_xpath("//div[contains(text(),'Údaje o ručiteli')]")
    _section_guar_udaje.click()
    sleep(0.3)
    
    guar_address_values = data_guar_fo.guar_address_values
    
    guar_address_elements = [
            Ekp('HomeAddressStreet', '__Deb_HomeAddressStreet', "", "txt", 0.1, 0.1),
            Ekp('HomeAddressCity', '__Deb_HomeAddressCity', "", "txt", 0.1, 0.1),
            Ekp('HomeAddressZip', '__Deb_HomeAddressZip', "", "txt", 0.1, 0.1),
            #Ekp('HomeAddressState', '__Deb_HomeAddressState', "", "txt", 0.1, 0.1),
            #Ekp('AddressSame', '__Deb_AddressSame', "", "cb", 0.1, 0.1),   
            ]    
        
    fill_elems(browser, guar_address_elements, guar_address_values)
    
    # otevři koresp. adresu    
    _section_guar_add = browser.find_element_by_xpath("//div[contains(text(),'Adresa ručitele')]")
    _section_guar_add.click()    
    _address_same= browser.find_element_by_name("__Deb_AddressSame")
    if (_address_same.is_selected()):        
        _address_same.click()
        sleep(0.3)
        
    guar_address_elements = [
            Ekp('AddressServicesStreet', '__Deb_AddressServicesStreet', "", "txt", 0.1, 0.1),
            Ekp('AddressServicesCity', '__Deb_AddressServicesCity', "", "txt", 0.1, 0.1),
            Ekp('AddressServicesZip', '__Deb_AddressServicesZip', "", "txt", 0.1, 0.1),
            Ekp('AddressServicesState', '__Deb_AddressServicesState', "", "dd", 0.1, 0.1),     
            ]            
    
    fill_elems(browser, guar_address_elements, guar_address_values)
    
    _section_guar_add.click()  
    # Zaměstnání ručitele
    sleep(0.3)
    _section_guar_emp = browser.find_element_by_xpath("//div[contains(text(),'Zaměstnání ručitele')]")
    _section_guar_emp.click()
    
    guar_employer_values = data_guar_fo.guar_employer_values
    guar_employer_elements = [
            Ekp('EmployerType', '__Deb_SourceOfIncome',"","dd", 0.1, 0.1),
            Ekp('WorkPhoneNumber', '__Deb_WorkPhoneNumber',"","txt", 0.1, 0.1),
            Ekp('RegistrationNumber', '__DebEmp_RegistrationNumber',"","txt", 0.1, 0.1),
            #Ekp('Foreigner', '__Emp_Foreigner',"","dd", 0.1, 0.1),
            Ekp('ProbationPeriod', '',"__Deb_ProbationPeriod","cb", 0.1, 0.1),
            Ekp('NoticePeriod', '',"__Deb_NoticePeriod","cb", 0.1, 0.1),
            Ekp('EmploymentIndefinitePeriod', '',"__Deb_EmploymentIndefinitePeriod","cb", 0.1, 0.1),
            Ekp('EmploymentIndefinitePeriodUntil', '__Deb_EmploymentIndefinitePeriodUntil', "","txt", 0.1, 0.1),            
            ]
    fill_elems(browser, guar_employer_elements, guar_employer_values)
    
    _section_guar_emp.click()
    
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
_guar_elements = {'SubjType': '__Deb_SubjType', 'TitleBefore': '__Deb_TitleBefore', 'Name': '__Deb_Name', 'Surname': '__Deb_Surname', 'TitleAfter': '__Deb_TitleAfter', 'PhoneNumber': '__Deb_PhoneNumber', 'Email': '__Deb_Email', 'BankAccountNumber1': '__Deb_BankAccountNumber1', 'BankAccountNumber': '__Deb_BankAccountNumber', 'BankCode': '__Deb_BankCode', 'Foreigner': '__Deb_Foreigner', 'PIN': '__Deb_PIN', 'DateOfBirth': '__Deb_DateOfBirth', 'Gender': '__Deb_Gender', 'Citizenship': '__Deb_Citizenship', 'DocumentType': '__Deb_DocumentType', 'DocumentNumber': '__Deb_DocumentNumber', 'DocumentValidTo': '__Deb_DocumentValidTo', 'SecondDocumentType': '__Deb_SecondDocumentType', 'SecondDocumentNumber': '__Deb_SecondDocumentNumber', 'SecondDocumentValidTo': '__Deb_SecondDocumentValidTo'}

for e in _guar_elements:
    print(f'Ekp("{e}", "{_guar_elements[e]}","", "txt", 0.1, 0.1 ),')
"""  