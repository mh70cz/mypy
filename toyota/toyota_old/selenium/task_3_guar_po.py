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


Ekp = namedtuple("Ekp", "key, eid, name, etype, before, after") # element key + properties


def fill(browser, data):

    guar_fo_elements = [
        Ekp("SubjType", "__Deb_SubjType","", "dd", 0.1, 0.3 ),
        Ekp("RegistrationNumber", "__Deb_RegistrationNumber", "","txt",0.1, 0.1),
        Ekp("TradeName", "__Deb3_TradeName", "","txt",0.2, 0.1),
        Ekp("TaxRegistrationNumber", "__Deb3_TaxRegistrationNumber", "","txt",0.1,0.1),
        Ekp("RegistrationOfficeType", "__Deb3_RegistrationOfficeType", "","txt",0.1,0.1),
        Ekp("RegistrationOfficeName", "__Deb3_RegistrationOfficeName", "","txt",0.1,0.1),
        Ekp("RegistrationSectionFileNo", "__Deb3_RegistrationSectionFileNo", "","txt",0.1,0.1),                
        Ekp("BankAccountNumber1", "__Deb3_BankAccountNumber1", "","txt",0.1,0.1),
        Ekp("BankAccountNumber", "__Deb3_BankAccountNumber", "","txt",0.1,0.1),
        Ekp("BankCode", "__Deb3_BankCode", "","dd",0.1,0.1),
        Ekp("PhoneNumber", "__Deb3_PhoneNumber", "","txt",0.1,0.1),
        Ekp("Email", "__Deb3_Email", "","txt",0.1,0.1),
    ]
             
    fill_elems(browser, guar_fo_elements, data["guarantor"] )

    _section_guar_udaje = browser.find_element_by_xpath("//div[contains(text(),'Ručitel - firma')]")
    _section_guar_udaje.click()


    # Guarantor Address    
    sleep(0.3)    
                  
    guar_address_elements_1 = [
        Ekp("HomeAddressStreet", "__Deb3_HomeAddressStreet", "","txt",0.1,0.1),
        Ekp("HomeAddressCity", "__Deb3_HomeAddressCity", "","txt",0.1,0.1),
        Ekp("HomeAddressZip", "__Deb3_HomeAddressZip", "","txt",0.1,0.1),
        #Ekp("HomeAddressState", "__Deb3_HomeAddressState", "","dd",0.1,0.1),
        ]
    fill_elems(browser,  guar_address_elements_1, data["guarantor_address"] )

    _section_adresa = browser.find_element_by_xpath("//div[contains(text(),'Adresa ručitele')]")
    _section_adresa.click()
        
    _address_same= browser.find_element_by_name("__Deb3_AddressSame")
    if (_address_same.is_selected()):        
        _address_same.click()
        sleep(0.5)
   
        
    if not (_address_same.is_selected()):
        guar_address_elements_2 = [
            Ekp("AddressServicesStreet", "__Deb3_AddressServicesStreet", "","txt",0.1,0.1),
            Ekp("AddressServicesCity", "__Deb3_AddressServicesCity", "","txt",0.1,0.1),
            Ekp("AddressServicesZip", "__Deb3_AddressServicesZip", "","txt",0.1,0.1),
            #Ekp("AddressServicesState", "__Deb3_AddressServicesState", "","dd",0.1,0.1),
                ]
        fill_elems(browser, guar_address_elements_2, data["guarantor_address"])    
        _section_adresa.click()
    
    # způsob zastupování
    sleep(0.3)
    app_zz_elements = [Ekp("RepresentativeMethod", "__Deb3_RepresentativeMethod", "", "dd", 0.1, 0.1),]
    fill_elems(browser, app_zz_elements, data["guarantor"] )

    _section_zz_lst = browser.find_elements_by_xpath("//div[contains(text(),'Způsob zastupování')]")
    _section_zz_lst[1].click()    #totožný název s oprávněnými osobami žadatele


    # Oprávněná osoba 1
    sleep(0.3)    
    _section_rep_lab_lst = browser.find_elements_by_xpath("//div[contains(text(),'Oprávněná osoba 1')]")
    _section_rep_lab = _section_rep_lab_lst[1]
    
    section = _section_rep_lab.find_element_by_xpath("..")
    rep_data = data["guarantorRepresentative"]
    fill_representative(section, rep_data)
    
    rep_data = data["guarantorRepresentativeAddress"]
    fill_repAddress(section, rep_data)
    
    _section_rep_lab.click()
    
    # Oprávněná osoba 2  
    sleep(0.3)    
    _section_rep1_lab_lst = browser.find_elements_by_xpath("//div[contains(text(),'Oprávněná osoba 2')]")
    _section_rep1_lab = _section_rep1_lab_lst[1]
    
    section = _section_rep1_lab.find_element_by_xpath("..")
    rep_data = data["guarantorRepresentative1"]
    fill_representative(section, rep_data)
    
    rep_data = data["guarantorRepresentative1Address"]
    fill_repAddress(section, rep_data)
    
    _section_rep1_lab.click()    
    
    # Oprávněná osoba 2  
    sleep(0.3)    
    _section_rep2_lab_lst = browser.find_elements_by_xpath("//div[contains(text(),'Oprávněná osoba 3')]")
    _section_rep2_lab = _section_rep2_lab_lst[1]
    
    section = _section_rep2_lab.find_element_by_xpath("..")
    rep_data = data["guarantorRepresentative2"]
    fill_representative(section, rep_data)
    
    rep_data = data["guarantorRepresentative2Address"]
    fill_repAddress(section, rep_data)
    
    _section_rep2_lab.click()   
    
    
    #bonita ručitele
    sleep(0.3)
    if data["guarantor"]["TrReportsInFull"] == "1":
        guar_bonita_elements = [
            Ekp("TrReportsInFull", "__Deb3_TrReportsInFull","", "dd", 0.1, 0.3 ),
            Ekp("TotalAssets", "__Deb3_TotalAssetsRow", "","txt",0.1,0.1),
            Ekp("EquityCapital", "__Deb3_EquityCapitalRow", "","txt",0.1,0.1),
            Ekp("TrProfitForAccountingPeriod", "__Deb3_TrProfitForAccountingPeriodRow", "","txt",0.1,0.1),
            Ekp("TrNetTurnoverForAccountingPeriod", "__Deb3_TrNetTurnoverForAccountingPeriod3Row", "","txt",0.1,0.1),
        ]
    elif data["guarantor"]["TrReportsInFull"] == "0":
        guar_bonita_elements = [
            Ekp("TrReportsInFull", "__Deb3_TrReportsInFull","", "dd", 0.1, 0.3 ),
            Ekp("TotalAssets", "__Deb3_TotalAssets", "","txt",0.1,0.1),
            Ekp("EquityCapital", "__Deb3_EquityCapital", "","txt",0.1,0.1),
            Ekp("TrProfitForAccountingPeriod", "__Deb3_TrProfitForAccountingPeriod1", "","txt",0.1,0.1),
            Ekp("TrNetTurnoverForAccountingPeriod", "__Deb3_TrNetTurnoverForAccountingPeriod2", "","txt",0.1,0.1),
        ]
        
    fill_elems(browser, guar_bonita_elements, data["guarantor"] )

    _section_guar_bonita = browser.find_element_by_xpath("//div[contains(text(),'Bonita ručitele')]")
    _section_guar_bonita.click()    
    

def fill_old(browser, data):
    
    
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
    
    fill_elems(browser, guar_fo_elements, data["guarantor"])
    
    _section_guar_udaje = browser.find_element_by_xpath("//div[contains(text(),'Údaje o ručiteli')]")
    _section_guar_udaje.click()
    sleep(0.3)
    
    guar_address_elements = [
            Ekp('HomeAddressStreet', '__Deb_HomeAddressStreet', "", "txt", 0.1, 0.1),
            Ekp('HomeAddressCity', '__Deb_HomeAddressCity', "", "txt", 0.1, 0.1),
            Ekp('HomeAddressZip', '__Deb_HomeAddressZip', "", "txt", 0.1, 0.1),
            #Ekp('HomeAddressState', '__Deb_HomeAddressState', "", "txt", 0.1, 0.1),
            #Ekp('AddressSame', '__Deb_AddressSame', "", "cb", 0.1, 0.1),   
            ]    
        
    fill_elems(browser, guar_address_elements, data["guarantor_address"])
    
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
    
    fill_elems(browser, guar_address_elements, data["guarantor_address"])
    
    _section_guar_add.click()  
    # Zaměstnání ručitele
    sleep(0.3)
    _section_guar_emp = browser.find_element_by_xpath("//div[contains(text(),'Zaměstnání ručitele')]")
    _section_guar_emp.click()

    guar_employer_elements = [
            Ekp('EmployerType', '__Deb_SourceOfIncome',"","dd", 0.1, 0.1),
            Ekp('WorkPhoneNumber', '__Deb_WorkPhoneNumber',"","txt", 0.1, 0.1),
            Ekp('RegistrationNumber', '__DebEmp_RegistrationNumber',"","txt", 0.1, 0.1),
            #Ekp('Foreigner', '__Emp_Foreigner',"","dd", 0.1, 0.1),
            Ekp('ProbationPeriod', '',"__Deb_ProbationPeriod","cb", 0.1, 0.1),
            Ekp('NoticePeriod', '',"__Deb_NoticePeriod","cb", 0.1, 0.1),
            Ekp('EmploymentIndefinitePeriod', '',"__Deb_EmploymentIndefinitePeriod","cb", 0.1, 0.2),
            Ekp('EmploymentIndefinitePeriodUntil', '__Deb_EmploymentIndefinitePeriodUntil', "","txt", 0.1, 0.1), #ToDo podmíněné pole           
            ]
    fill_elems(browser, guar_employer_elements, data["guarantor_employer"])
    
    _section_guar_emp.click()
    
    # Bonit ručitle
    sleep(0.3)
    _section_guar_bonita = browser.find_element_by_xpath("//div[contains(text(),'Bonita ručitele')]")
    _section_guar_bonita.click()
    
    guar_elements = [
            Ekp("MainIncomeType", "__Deb_MainIncomeType", "", "dd", 0.1, 0.2),
            #Ekp("IncomeType", "__Deb_IncomeType", "",  "txt", 0.1, 0.1), #Pokud MainIncomeType == Jiné
            Ekp("AverageMIAT", "__Deb_AverageMIAT", "",  "txt", 0.1, 0.1),
            Ekp("OtherIncomeType", "__Deb_OtherIncomeType", "",  "txt", 0.1, 0.2),
            Ekp("OtherIncomeAmount", "__Deb_OtherIncomeAmount", "",  "txt", 0.1, 0.1),
            Ekp("TypeOfHousing", "__Deb_TypeOfHousing", "",  "dd", 0.1, 0.1),
            #Ekp("TrReceivedFromAllEmployers", "__Deb_TrReceivedFromAllEmployersFO", "",  "txt", 0.1, 0.1), #OSVC
            #Ekp("TrTaxBaseLineTotals", "__Deb_TrTaxBaseLineTotalsFO", "",  "txt", 0.1, 0.1), #OSVC
            #Ekp("TrTaxAfterApplyingDiscount", "__Deb_TrTaxAfterApplyingDiscountFO", "",  "txt", 0.1, 0.1), #OSVC
            Ekp("IsLiabilities", "__Deb_IsLiabilities", "",  "dd", 0.1, 0.2),
            Ekp("Liabilities", "__Deb_Liabilities", "",  "txt", 0.1, 0.1),
            Ekp("HouseholdNumberPersons", "__Deb_HouseholdNumberPersons", "",  "txt", 0.1, 0.1),
            Ekp("NumberDependentPersons", "__Deb_NumberDependentPersons", "",  "txt", 0.1, 0.1),
            Ekp("NumberDependentPersons1", "__Deb_NumberDependentPersons1", "",  "txt", 0.1, 0.1),
            Ekp("NumberDependentPersons2", "__Deb_NumberDependentPersons2", "",  "txt", 0.1, 0.1),
            Ekp("IsExecutionAgainst", "", "__Deb_IsExecutionAgainst",  "radio", 0.1, 0.1),
            Ekp("IsInsolvencyAgainst", "", "__Deb_IsInsolvencyAgainst",  "radio", 0.1, 0.1),
            Ekp("IsPoliticallyExposedPerson", "", "__Deb_IsPoliticallyExposedPerson",  "radio", 0.1, 0.1),
            ]
    
    fill_elems(browser, guar_elements, data["guarantor"])
    
    _section_guar_bonita.click()
    

def fill_representative(section, rep_data):
    fill_elems_sdl_dd(section, '__Rep_RepresentativeType', rep_data["RepresentativeType"])
    fill_elems_sdl_txt(section, "__Rep_TitleBefore", rep_data["TitleBefore"])
    fill_elems_sdl_txt(section, "__Name", rep_data["Name"])
    fill_elems_sdl_txt(section, "__Rep_Surname", rep_data["Surname"])
    fill_elems_sdl_txt(section, "__Rep_TitleAfter", rep_data["TitleAfter"])    
    fill_elems_sdl_txt(section, "__Rep_PIN", rep_data["PIN"])     
    fill_elems_sdl_txt(section, "__Rep_DateOfBirth", rep_data["DateOfBirth"])
    fill_elems_sdl_dd(section, '__DocumentType', rep_data["DocumentType"])
    fill_elems_sdl_txt(section, "__DocumentNumber", rep_data["DocumentNumber"])
    fill_elems_sdl_txt(section, "__DocumentValidTo", rep_data["DocumentValidTo"])
    fill_elems_sdl_dd(section, '__SecondDocumentType', rep_data["SecondDocumentType"])
    fill_elems_sdl_txt(section, "__SecondDocumentNumber", rep_data["SecondDocumentNumber"])
    fill_elems_sdl_txt(section, "__SecondDocumentValidTo", rep_data["SecondDocumentValidTo"])    


def fill_repAddress(section, rep_data):
    fill_elems_sdl_txt(section, "__HomeAddressStreet", rep_data["HomeAddressStreet"])
    fill_elems_sdl_txt(section, "__HomeAddressCity", rep_data["HomeAddressCity"])
    fill_elems_sdl_txt(section, "__HomeAddressZip", rep_data["HomeAddressZip"])
    fill_elems_sdl_dd(section, '__HomeAddressState', rep_data["HomeAddressState"])    
    
    
def fill_elems_sdl_dd(section, data_label, value):
    elem = section.find_element_by_xpath(f".//select[@data-label='{data_label}']")
    sleep(0.1)
    Select(elem).select_by_value(value)
    sleep(0.1)
    
def fill_elems_sdl_txt(section, data_label, value):
    elem = section.find_element_by_xpath(f".//input[@data-label='{data_label}']")
    elem.clear()
    sleep(0.1)
    elem.send_keys(value)
    sleep(0.1)   


def fill_elems(browser, elements, values):
    for ekp in elements:
        key = ekp.key
        elem_id = ekp.eid
        elem_name = ekp.name
        if ekp.etype == "txt":
            elem = browser.find_element_by_id(elem_id)  #podle id
            elem.click()
            sleep(ekp.before)
            elem.clear()
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