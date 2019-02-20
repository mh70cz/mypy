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

#import data_spo
# import start

Ekp = namedtuple("Ekp", "key, etype, before, after") # element key + properties

app_values = {'TitleBefore': 'ing.', 'Name': 'Pavel', 'Surname': 'Ploc', 'TitleAfter': 'MBA', 'MaritalStatus': '1', 'Foreigner': '0', 'DateOfBirth': '26.1.1979', 'PIN': '7951266884', 'Gender': 'M', 'Citizenship': 'CZ', 'BankAccountNumber1': '31', 'BankAccountNumber': '314159', 'BankCode': '0100', 'DocumentType': '0', 'DocumentNumber': 'OP913746', 'DocumentValidTo': '13.3.2025', 'SecondDocumentType': '6', 'SecondDocumentNumber': 'RP853257', 'SecondDocumentValidTo': '14.12.2027', 'PhoneNumber': '+420398827620', 'Email': 'josef.novak@elposta.cz', "NRKISign":"1"}
app_address_values = {'HomeAddressStreet': 'Koněvova 242', 'HomeAddressCity': 'Praha 3', 'HomeAddressZip': '13000', 'HomeAddressState': 'CZ', 'AddressSame': '0', 'AddressServicesStreet': 'Park Str. 37', 'AddressServicesCity': 'Köln Chorweiler', 'AddressServicesZip': '50765', 'AddressServicesState': 'DE'}
emp_values = {'RegistrationNumber': '04134940', 'ProbationPeriod': '0', 'EmploymentIndefinitePeriod': '0', 'NoticePeriod': '0', 'WorkPhoneNumber': '+420731555999', 'Foreigner': '0', 'EmploymentIndefinitePeriodUntil': '21.11.2020'}
coapp_values = {'TitleBefore': 'ing', 'Name': 'Jana', 'Surname': 'Nováková', 'TitleAfter': 'PhD', 'Foreigner': '0', 'DateOfBirth': '1.1.1970', 'AverageMIAT': '22656', 'AddressServicesStreet': 'Augsburger Strasse 44', 'AddressServicesCity': 'Wershofen', 'AddressServicesZip': '53520', 'AddressServicesState': 'DE'}
za60 = datetime.datetime.now() + datetime.timedelta(days=60).strftime("%d.%m.%Y")
vehicle_values = {"ExpectedDeliveryDate":za60}
contract_values = {"RequestSign":"1"}

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

       
    # Applicant Address    
    sleep(0.2)    
        
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

#txt dd radio checkbox
#app_date_non_conditional_key = [
#        "DateOfBirth", "DocumentValidTo", "SecondDocumentValidTo"
#        ]    
#
#for key in app_date_non_conditional_key:
#    dat_id = app.fields[key]
#    dat = browser.find_element_by_id(dat_id)
#    sleep(0.1)
    

#
#"""
#browser, web_app = start.open_browser()
#start.login(browser)
#
##http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/processDetail.aspx?id=7537
##http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/TaskEdit.aspx?id=46889
#"""
#def init(browser, web_app, task_id):
#    web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
#    web_task_edit = "Processing/TaskEdit.aspx?id="
#    #task_id = "46889"  #46889  46891  46889
#    browser.get(web_app + web_task_edit + task_id)
#
#    sleep(2)
#    subj_type_dd = browser.find_element_by_id("__SubjType")
#    sleep(0.3)
#    subj_type = subj_type_dd.get_attribute("value")
#
#
#    if subj_type == "1":
#        fill_spo(browser)
#    elif subj_type == "2":
#        fill_fop(browser)
#    elif subj_type == "3":
#        fill_po(browser)
#
#
#def fill_spo(browser):
#
#    sleep(0.2)
#    employer_dd = browser.find_element_by_id("__EmployerType")
#    sleep(0.1)
#    Select(employer_dd).select_by_value("1")
#
#    sleep(0.1)
#    main_inc_dd = browser.find_element_by_id("__MainIncomeType")
#    sleep(0.1)
#    Select(main_inc_dd).select_by_value("0")
#
#    avg_miat_f = browser.find_element_by_id("__AverageMIAT")
#    avg_miat_f.send_keys(str(random.randint(18_000, 50_000)))
#
#    other_inc_type_f = browser.find_element_by_id("__OtherIncomeType")
#    other_inc_type_f.send_keys("Pronájem nemovitosti")
#    sleep(0.2)
#    other_inc_f = browser.find_element_by_id("__OtherIncomeAmount")
#    other_inc_f.send_keys(str(random.randint(2_000, 7_000)))
#
#
#
#    sleep(0.2)
#    housing_type_dd = browser.find_element_by_id("__TypeOfHousing")
#    housing_type_val = random.choice(["1", "2", "3"])
#    # 1 -nájem, 2 - u rodičů, 3 - vlastní
#    Select(housing_type_dd).select_by_value(housing_type_val)
#
#    sleep(0.2)
#    Select(browser.find_element_by_id("__IsLiabilities")).select_by_value("1")
#    sleep(0.2)
#    monthly_inst_f = browser.find_element_by_id("__Liabilities")
#    monthly_inst_f.send_keys(str(random.randint(400, 9_000)))
#
#
#    Select(browser.find_element_by_id("__Spoluzadatel")).select_by_value("1")
#    sleep(0.2)
#
#    coapp_avg_miat_f = browser.find_element_by_id("__CoAverageMIAT")
#    coapp_avg_miat_f.send_keys(str(random.randint(15_000, 39_000)))
#
#
#    browser.find_element_by_id("__HouseholdNumberPersons").send_keys("5")
#
#    deti = ["__NumberDependentPersons",
#            "__NumberDependentPersons1",
#            "__NumberDependentPersons2",
#                          ]
#    for d in deti:
#        browser.find_element_by_id(d).send_keys("1")
#
#    sex, pin, dat_nar = r_rc_ico.rc_dat()
#
#    dat_nar_f = browser.find_element_by_id("__DateOfBirth")
#    dat_nar_f.send_keys(dat_nar)
#    sleep(0.2)
#
#
#    pin_f = browser.find_element_by_id("__PIN")
#    pin_f.send_keys(pin)
#
#    sleep(0.1)
#    sex_dd = browser.find_element_by_id("__Gender")
#    sleep(0.1)
#    Select(sex_dd).select_by_value(sex)
#
#    prepocitat(browser)
#
#def fill_fop(browser):
#
#    sleep(0.4)
#
#    # Uplatňuji výdaje procentem z příjmu
#    # per_of_inc = 1  # 1- ano 2-ne
#    per_of_inc = random.choice([1,2])
#    per_of_inc_dd = browser.find_element_by_id("__TrPercentageOfIncome")
#    Select(per_of_inc_dd).select_by_index(per_of_inc) # 1- ano 2-ne
#
#    r_money = random.randint(400_000, 9_000_000) #v jednotkách Kč
#    prijmy = [
#        ("__TrReceivedFromAllEmployers", r_money),
#        ("__TrTaxBaseLineTotals", r_money * 1.5),
#        ("__IncomeByAct", r_money * 1.9),
#        ("__TrTaxAfterApplyingDiscount", r_money / 3),
#            ]
#
#    sleep(0.1)
#    fill_numeric_fields(browser, prijmy)
#
#    co_applicant = browser.find_element_by_id("__Spoluzadatel2")
#    Select(co_applicant).select_by_value("1")
#    sleep(0.2)
#
#    prijem_coapp_f = browser.find_element_by_id("__CoAverageMIAT2")
#    prijem_coapp_f.send_keys(str(random.randint(10_000, 45_000)))
#
#    sex, pin, dat_nar = r_rc_ico.rc_dat()
#    ico = r_rc_ico.r_ico()
#
#    sleep(0.2)
#    identif_app = [("__PIN", pin),]
#    fill_numeric_fields(browser, identif_app)
#
#    dat_nar_f = browser.find_element_by_id("__DateOfBirth")
#    sleep(0.1)
#    dat_nar_f.send_keys(dat_nar)
#    sleep(0.2)
#
#
#    sleep(0.1)
#    sex_dd = browser.find_element_by_id("__Gender")
#    sleep(0.1)
#    Select(sex_dd).select_by_value(sex)
#    sleep(0.2)
#    ico_f = browser.find_element_by_id("__RegistrationNumber")
#    ico_f.send_keys(ico)
#    sleep(0.2)
#
#    prepocitat(browser)
#
#
#
#
#def fill_po(browser):
#
#    #__TrReportsInFull výkazy v plném rozsahu
#    sleep(0.4)
#    vykazy_dd = browser.find_element_by_id("__TrReportsInFull")
#    Select(vykazy_dd).select_by_index(0) # 0 - Ano, 1 - Ne
#
#    r_money = random.randint(8_000, 99_000) #v tisících Kč - tisících!
#    vykazy_plne_ano = [
#            ("__TotalAssetsRow", r_money),
#            ("__TrProfitForAccountingPeriodRow", r_money * 0.6, 0),
#            ("__EquityCapitalRow", r_money * 0.9),
#            ("__TrNetTurnoverForAccountingPeriod3Row", r_money * 5),
#            ]
#    sleep(0.2)
#    fill_numeric_fields(browser, vykazy_plne_ano)
#
#    sleep(0.2)
#    Select(vykazy_dd).select_by_index(1) # 0 - Ano, 1 - Ne
#    vykazy_plne_ne = [
#            ("__TotalAssets", r_money * 1.2),
#            ("__TrProfitForAccountingPeriod1", r_money * 0.8),
#            ("__EquityCapital", r_money * 1.1),
#            ("__TrNetTurnoverForAccountingPeriod2", r_money * 6),
#            ]
#    sleep(0.2)
#    fill_numeric_fields(browser, vykazy_plne_ne)
#
#
#    ico_f = browser.find_element_by_id("__RegistrationNumber3")
#    ico = r_rc_ico.r_ico()
#    ico_f.send_keys(ico)
#
#    prepocitat(browser)
#
#
#
#def fill_numeric_fields (browser, vykazy):
#    for v in vykazy:
#        field = browser.find_element_by_id(v[0])
#        sleep(0.1)
#        field.clear()
#        sleep(0.1)
#        field.send_keys(str(int(v[1])))
#        sleep(0.1)
#
#
#def prepocitat(browser):
#    """for numeric (no leading 0 ) fields (konverted to int)"""
#    b_prepocitat = browser.find_element_by_xpath('//button[contains(text(), "' + "PŘEPOČÍTAT" + '")]')
#    sleep(1)
#    b_prepocitat.click()
#
#"""
#for i in range(20):
#    init(browser, web_app)
#    sleep(1)
#    browser.back()
#    sleep(0.5)
#
#"""