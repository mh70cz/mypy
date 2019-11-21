#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
import random


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
    

"""
<a href="Processing/processStart.aspx?definitionID={AB260856-E6EA-42D4-998C-175099591E9A}" target="mainFrame" class="AspNet-Menu-Link">
								<img src="App_Themes/Toyota/images/icons/ico_app_new.png" alt="Nová žádost – financování" class="Menu-ico">Nová žádost – financování
							</a>

http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/Processing/processList.aspx
"""

def fillscreen(browser, web_app, data=None, subj_type="SPO", prod_type="FC"):
    nova_zadost_url = "Processing/processStart.aspx?definitionID={AB260856-E6EA-42D4-998C-175099591E9A}"
    browser.get(web_app + nova_zadost_url)
    sleep(3)
    
    
    #subj_type = "PO"  # SPO, FOP, PO
    #prod_type = "FC"   # FC - úvěr , FO - operativní leasing
    
    if data is None:
        data = get_data(subj_type, prod_type)
    
    label_fc = browser.find_element_by_xpath('//span[contains(text(), "' + "úvěr" + '")]')
    label_fo = browser.find_element_by_xpath('//span[contains(text(), "' + "operativní leasing" + '")]')
    
    if prod_type == "FC":
        label_fc.click()        
    elif prod_type == "FO":
        label_fo.click()

    
    label_nove = browser.find_element_by_xpath('//span[contains(text(), "' + "nové" + '")]')
    label_ojete = browser.find_element_by_xpath('//span[contains(text(), "' + "ojeté" + '")]')
    
    if data["vehicle"]["VehicleStatus"] == "1":
        label_nove.click()        
    elif data["vehicle"]["VehicleStatus"] == "0":
        label_ojete.click()
    
    label_osobni = browser.find_element_by_xpath('//span[contains(text(), "' + "osobní" + '")]')
    label_uzitkove = browser.find_element_by_xpath('//span[contains(text(), "' + "užitkové" + '")]')
    
    if data["vehicle"]["VehicleMode"] == "1":
        label_osobni.click()        
    elif data["vehicle"]["VehicleMode"] == "3":
        label_uzitkove.click()    
    
    #vyrobce = browser.find_element_by_id("__VehicleMaker")
    #Select(vyrobce).select_by_value("L") #Lexus
    
    sleep(0.2)
    model_type = browser.find_element_by_id("__VehicleModelType")
    sleep(0.2)
    Select(model_type).select_by_value(data["vehicle"]["VehicleModelType"])
    
    sleep(0.2)
    model = browser.find_element_by_id("__VehicleModel")
    sleep(0.2)
    Select(model).select_by_value(data["vehicle"]["VehicleModel"])
    
    sleep(0.2)
    equipment = browser.find_element_by_id("__EquipmentLevel")
    sleep(0.2)
    Select(equipment).select_by_value(data["vehicle"]["EquipmentLevel"])
    
    
    if data["vehicle"]["VehicleStatus"] == "0":
        cylinder_volume = browser.find_element_by_id("__CylinderVolume")
        if cylinder_volume.is_enabled():
            cylinder_volume.send_keys(data["vehicle"]["CylinderVolume"])

        usage_start_date = browser.find_element_by_id("__UsageStartDate")
        usage_start_date.send_keys(data["vehicle"]["UsageStartDate"])

        covered_km = browser.find_element_by_id("__CoveredKilometres")
        covered_km.send_keys(data["vehicle"]["CoveredKilometres"])        
        
    
    sleep(0.2)
    subj_type_dd = browser.find_element_by_id("__SubjType")
    vehicle_operation = browser.find_element_by_id("__VehicleOperation")
    vat_r_buttons = browser.find_elements_by_name("__VATPayer")
    if subj_type == "SPO":
        Select(subj_type_dd).select_by_value("1")
    elif subj_type == "FOP":
        Select(subj_type_dd).select_by_value("2")
        sleep(0.2)
        Select(vehicle_operation).select_by_value("1")
        vat_r_buttons[0].click() #platce DPH ano
        
    elif subj_type == "PO":
        Select(subj_type_dd).select_by_value("3")
        sleep(0.2)
        Select(vehicle_operation).select_by_value("1")
        vat_r_buttons[0].click() #platce DPH ano
    
    #cena doplňků
    accessories_price = browser.find_element_by_id("__AccessoriesPrice")
    accessories_price.send_keys(data["vehicle"]["AccessoriesPriceVAT"])
    
    # sleva s dph
    sleep(0.1)
    discount_price = browser.find_element_by_id("__DiscountPrice")
    discount_price.send_keys(data["vehicle"]["DiscountPrice"])
    
    
    
    sleep(0.2)
    dealer = browser.find_element_by_id("__TFSCDealer")
    sleep(0.2)
    Select(dealer).select_by_value(data["contract"]["TFSCDealer"])
    
    sleep(0.4)
    campaign = browser.find_element_by_id("__CampaignCode")
    sleep(0.8) #opravdu tolik
    Select(campaign).select_by_value(data["contract"]["CampaignCode"]) 
    
    
    sleep(0.4)
    pocet_mesicu = browser.find_element_by_id("__NoOfInstalmentsMax")
    sleep(0.4)
    Select(pocet_mesicu).select_by_index(1)
    
    
    if prod_type=="FO":
        sleep(0.4)
        rocni_najezd = browser.find_element_by_id("__StepMileAgePerYear")
        Select(rocni_najezd).select_by_index(1)
    
    sleep(0.2)
    pojisteni = ["__InsuranceCoName", "__MTPLInsuranceLimits", "__InsuranceCoNameMotor", "__MotorInsuranceParticipation"]
    for p in pojisteni:
        Select(browser.find_element_by_id(p)).select_by_index(1)
        sleep(0.4)
     
    doplnkove_pojisteni = [
            ("__MotorSIWindscreenInsurance", "__MotorSIWindscreenLimit"),
            ("__MotorSILuggageInsurance", "__MotorSILuggageLimit"),
            ("__MotorSIVehicleRentInsurance", "__MotorSIVehicleRentDays"),
            ("__MotorAPISeatInsurance", "__MotorAPISeatAmount"),
            ("__MotorSIPlusInsurance", "__MotorSIPlusType")
            ]    
    
    for p in doplnkove_pojisteni:
        cb = browser.find_element_by_id(p[0])
        cb.click()
        sleep(0.2)
        Select(browser.find_element_by_id(p[1])).select_by_index(1)
    Select(browser.find_element_by_id("__MotorAPIMultiple")).select_by_index(1)
    
    
    sleep(0.2)
    if prod_type == "FC":
        prod_type_text = "úvěr"
    elif prod_type == "FO":
        prod_type_text = "operL"
    else:
        prod_type_text = ""
    
    
#    if data["vehicle"]["VehicleStatus"] == "1":
#        vehicle_status_text = "nové"
#    elif  data["vehicle"]["VehicleStatus"] == "0":
#        vehicle_status_text = "ojeté"
#    else:
#        vehicle_status_text = ""
        
    if data["vehicle"]["VehicleMode"] == "1":
        vehicle_mode_text = "osobní"
    elif  data["vehicle"]["VehicleMode"] == "3":
        vehicle_mode_text = "užitkové"
    else:
        vehicle_mode_text = ""        
        
        
    id_zadosti = browser.find_element_by_id("__IdentificationRequest")
    
    my_charset="1234567890abcdefghjkmnprtuvwxyz"
    rnd_string = ''.join(random.choice(my_charset) for _ in range(8))
    id_zadosti.send_keys(f"{prod_type_text}; {vehicle_mode_text}; {rnd_string}")
    

def get_data(subj_type, prod_type):
            
    data = {
            "applicant":{},
            "contract":{},
            "vehicle":{
                    "VehicleStatus":"1", # nové 1 , ojeté 0
                    "VehicleMode": "1", # osobní 1, užitkové 3
                    },
            }     
            
    if prod_type == "FC":
        data["contract"]["OpType"] = "FC"
        data["contract"]["TFSCDealer"] = "1373"
        data["contract"]["CampaignCode"] = "KAMPAN_PRO_FC_GENIO_V_15_018"
        data["contract"]["NoOfInstalmentsMax"] = "72"
        
        
        data["vehicle"]["VehicleModelType"] = "AUHTS"
        data["vehicle"]["VehicleModel"] = "000636"
        data["vehicle"]["EquipmentLevel"] = "CT__AUHTSMC15_T0006363L__"
        data["vehicle"]["VehicleOperation"] = "1"
        data["vehicle"]["AccessoriesPriceVAT"] = "7500"
        data["vehicle"]["DiscountPrice"] = "1586"
        
    elif prod_type == "FO":
        data["contract"]["OpType"] = "FO"
        data["contract"]["TFSCDealer"] = "1373"
        data["contract"]["CampaignCode"] = "KAMPAN_PRO_FO_RENT_V_15_064"
        data["contract"]["NoOfInstalmentsMax"] = "72"        
        
        data["vehicle"]["VehicleModelType"] = "AUR"
        data["vehicle"]["VehicleModel"] = "000621"
        data["vehicle"]["EquipmentLevel"] = "CT__AUR__MC15_T000621JH__"
        data["vehicle"]["VehicleOperation"] = "1"
        data["vehicle"]["AccessoriesPriceVAT"] = "7500"
        data["vehicle"]["DiscountPrice"] = "1586"        
    
    if subj_type == "SPO":
        data["applicant"]["SubjType"] = "1"
        data["applicant"]["VATPayer"] = "0"
    elif subj_type == "FOP":
        data["applicant"]["SubjType"] = "2"
        data["applicant"]["VATPayer"] = "1"
    elif subj_type == "PO":
        data["applicant"]["SubjType"] = "3"
        data["applicant"]["VATPayer"] = "1"
        
        
    if data["vehicle"]["VehicleStatus"] == "0":
        data["vehicle"]["UsageStartDate"] = "21.12.2018"
        data["vehicle"]["CylinderVolume"] = "1794"
        data["vehicle"]["CoveredKilometres"] = "5999"
        
        data["contract"]["CampaignCode"] = "KAMPAN_PRO_FC_KREDIT_V_15_031"
        
        
        #__UsageStartDate, __CylinderVolume, __CoveredKilometres
        
    return data


                  
#browser, web_app = open_browser()
#login()
#fillscreen(browser, web_app)    

"""
browser, web_app = open_browser()
login(browser)

fillscreen(browser, web_app)


fillscreen(browser, web_app, subj_type = "SPO", prod_type = "FO")
fillscreen(browser, web_app, subj_type = "FOP", prod_type = "FO")
fillscreen(browser, web_app, subj_type = "PO", prod_type = "FO")






for subj_type in ["SPO", "FOP", "PO"]:
    for prod_type in ["FC", "FO"]:
        fillscreen(browser, web_app, 
                   subj_type = subj_type, prod_type = prod_type)
        sleep(2)
        browser.back()
        sleep(1)
        
"""

#    "VehicleMaker":"T",
#    "VehicleModelType":"AUHTS",
#    "VehicleModel":"000636",
#    "EquipmentLevel": "CT__AUHTSMC15_T0006363L__",
#    "VehicleOperation":"1",
#    "AccessoriesPriceVAT":"7500",
#    "DiscountPrice":"1586",
#    "TFSCDealer":"1373",
#    "NoOfInstalmentsMax":"72",
#    
#    
#    "InsuranceCoName": "",
#    "MTPLInsuranceLimit":"",
#    "InsuranceCoNameMotor":"",
#    
#    'MotorSIWindscreenInsurance': '1',
#    'MotorSILuggageInsurance': '1',
#    'MotorSIVehicleRentInsurance': '1',
#    'MotorAPISeatInsurance': '1',
#    'MotorSIPlusInsurance': '1',
#    "MotorAPIMultiple":"1",  
#    
#    'MotorSIWindscreenLimit': '1',
#    'MotorSILuggageLimit': '1',
#    'MotorSIVehicleRentDays': '1',
#    'MotorAPISeatAmount': '1',
#    'MotorSIPlusType': '1',
                    
