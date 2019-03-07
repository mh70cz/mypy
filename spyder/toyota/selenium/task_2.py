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
        

def fill_spo(browser):
    
    sleep(0.2)
    employer_dd = browser.find_element_by_id("__EmployerType")
    sleep(0.1)
    Select(employer_dd).select_by_value("1")
    
    sleep(0.1)
    main_inc_dd = browser.find_element_by_id("__MainIncomeType")
    sleep(0.1)
    Select(main_inc_dd).select_by_value("0")
    
    avg_miat_f = browser.find_element_by_id("__AverageMIAT")
    avg_miat_f.send_keys(str(random.randint(18_000, 50_000)))
    
    other_inc_type_f = browser.find_element_by_id("__OtherIncomeType")
    other_inc_type_f.send_keys("Pronájem nemovitosti")
    sleep(0.2)
    other_inc_f = browser.find_element_by_id("__OtherIncomeAmount")
    other_inc_f.send_keys(str(random.randint(2_000, 7_000)))
    
      
    
    sleep(0.2)
    housing_type_dd = browser.find_element_by_id("__TypeOfHousing")
    housing_type_val = random.choice(["1", "2", "3"]) 
    # 1 -nájem, 2 - u rodičů, 3 - vlastní
    Select(housing_type_dd).select_by_value(housing_type_val)
    
    sleep(0.2)
    Select(browser.find_element_by_id("__IsLiabilities")).select_by_value("1")
    sleep(0.2)
    monthly_inst_f = browser.find_element_by_id("__Liabilities")
    monthly_inst_f.send_keys(str(random.randint(400, 9_000)))
    
        
    Select(browser.find_element_by_id("__Spoluzadatel")).select_by_value("1")
    sleep(0.2)
    
    coapp_avg_miat_f = browser.find_element_by_id("__CoAverageMIAT")
    coapp_avg_miat_f.send_keys(str(random.randint(15_000, 39_000)))
    
    
    browser.find_element_by_id("__HouseholdNumberPersons").send_keys("5")
    
    deti = ["__NumberDependentPersons",
            "__NumberDependentPersons1",
            "__NumberDependentPersons2",
                          ]
    for d in deti:
        browser.find_element_by_id(d).send_keys("1")
    
    sex, pin, dat_nar = r_rc_ico.rc_dat()
    
    dat_nar_f = browser.find_element_by_id("__DateOfBirth")
    dat_nar_f.send_keys(dat_nar)
    sleep(0.2)

    
    pin_f = browser.find_element_by_id("__PIN")
    pin_f.send_keys(pin)
    
    sleep(0.1)
    sex_dd = browser.find_element_by_id("__Gender")
    sleep(0.1)
    Select(sex_dd).select_by_value(sex)
    
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)
    
    prepocitat(browser)
    
def fill_fop(browser):
    
    sleep(0.4)
    
    # Uplatňuji výdaje procentem z příjmu
    # per_of_inc = 1  # 1- ano 2-ne
    per_of_inc = random.choice([1,2])
    per_of_inc_dd = browser.find_element_by_id("__TrPercentageOfIncome")
    Select(per_of_inc_dd).select_by_index(per_of_inc) # 1- ano 2-ne

    r_money = random.randint(400_000, 9_000_000) #v jednotkách Kč
    prijmy = [
        ("__TrReceivedFromAllEmployers", r_money),
        ("__TrTaxBaseLineTotals", r_money * 1.5),
        ("__IncomeByAct", r_money * 1.9),
        ("__TrTaxAfterApplyingDiscount", r_money / 3),
            ]
    
    sleep(0.1)
    fill_numeric_fields(browser, prijmy)
    
    co_applicant = browser.find_element_by_id("__Spoluzadatel2")
    Select(co_applicant).select_by_value("1")
    sleep(0.2)
    
    prijem_coapp_f = browser.find_element_by_id("__CoAverageMIAT2")
    prijem_coapp_f.send_keys(str(random.randint(10_000, 45_000)))
    
    sex, pin, dat_nar = r_rc_ico.rc_dat()
    ico = r_rc_ico.r_ico()
    
    sleep(0.2)
    identif_app = [("__PIN", pin),]
    fill_numeric_fields(browser, identif_app)
        
    dat_nar_f = browser.find_element_by_id("__DateOfBirth")
    sleep(0.1)
    dat_nar_f.send_keys(dat_nar)  
    sleep(0.2)
    
    
    sleep(0.1)
    sex_dd = browser.find_element_by_id("__Gender")
    sleep(0.1)
    Select(sex_dd).select_by_value(sex)
    sleep(0.2)
    ico_f = browser.find_element_by_id("__RegistrationNumber")
    ico_f.send_keys(ico)
    sleep(0.2)
    
    prepocitat(browser)
    
    _body = browser.find_element_by_css_selector('body')
    _body.send_keys(Keys.PAGE_DOWN)
    
    return sex, pin
    

def fill_po(browser, full_statements = True):   
    # full_statements = True| False  __TrReportsInFull výkazy v plném rozsahu 
    
    sleep(0.4)
    
    r_money = random.randint(8_000, 99_000) #v tisících Kč - tisících!
    vykazy_plne_ano = [
            ("__TotalAssetsRow", r_money),
            ("__TrProfitForAccountingPeriodRow", r_money * 0.6, 0),
            ("__EquityCapitalRow", r_money * 0.9),
            ("__TrNetTurnoverForAccountingPeriod3Row", r_money * 5),
            ]
    vykazy_plne_ne = [
            ("__TotalAssets", r_money * 1.2),
            ("__TrProfitForAccountingPeriod1", r_money * 0.8),
            ("__EquityCapital", r_money * 1.1),
            ("__TrNetTurnoverForAccountingPeriod2", r_money * 6),
            ]
    
    vykazy_dd = browser.find_element_by_id("__TrReportsInFull")
    sleep(0.3)
    if full_statements:
        Select(vykazy_dd).select_by_index(0) # 0 - Ano, 1 - Ne
        fill_numeric_fields(browser, vykazy_plne_ano)    
    else:
        Select(vykazy_dd).select_by_index(1) # 0 - Ano, 1 - Ne
        fill_numeric_fields(browser, vykazy_plne_ne)    
        

    ico_f = browser.find_element_by_id("__RegistrationNumber3")
    ico = r_rc_ico.r_ico()
    ico_f.clear()
    sleep(0.1)
    ico_f.send_keys(ico)
    sleep(0.1)
   
    prepocitat(browser)
    
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

"""
for i in range(20):
    init(browser, web_app)
    sleep(1)
    browser.back()
    sleep(0.5)
    
"""