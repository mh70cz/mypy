# -*- coding: utf-8 -*-
"""

"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


envs = {
       "cz_test_CI": {
               "web_app": "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/",
               "usr": "cis\\m.houska",
               "pwd": "heslo",
                 },
       "cz_live": {
               "web_app": "https://www.tfsonline.sc/ToyotaDcM/",
               "usr": "tfscz.cisadm.Houska",
               "pwd": "",  # see KeyPass CI
                 },
       "sk_live": {
               "web_app": "https://www.tfsonline.sk/ToyotaDcMSK/",
               "usr": "tfssk.cisadm.Houska",
               "pwd": "",  # see KeyPass CI
               },               
       }
env = envs["sk_live"]
    

def open_browser(env):
    browser = webdriver.Chrome()
    # web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
    # web_app = "https://www.tfsonline.sk/ToyotaDcMSK/"
    web_app = env["web_app"]
    browser.get(web_app)
    return browser, web_app

def login(browser, env):
    
    usr_val = env["usr"]
    pwd_val = env["pwd"]
    
    try:
        usr = browser.find_element_by_id('txtUsername')
        pwd = browser.find_element_by_id('txtPassword')
        log_in = browser.find_element_by_id('btnLogin')
        
        #usr_val = "cis\\m.houska"
        #pwd_val = "heslo"
                
        sleep(0.2)
        usr.send_keys(usr_val)
        if not (pwd_val == ""):
            pwd.send_keys(pwd_val)
            sleep(0.2)
            log_in.click()
        print("tried to log in")
    except:
        pass



"""
browser, web_app = open_browser(env)
login(browser, env)

id_zadost = "85134"   # SK Live
id_zadost = "7556"    # CZ test_CI

data = read_data(browser, web_app, id_zadost)

"""        
def read_data(browser, web_app, id_zadost):
    url = web_app + "processing/processData.aspx?id=" + id_zadost
    browser.get(url)
    
    app = None
    app_address = None
    coapp = None
    employer = None
    employer_address = None   #??
    contract = None
    vehicle = None
    
    contract_el = browser.find_element_by_xpath("//span[contains(text(), 'LCContract')]")
    gparent_contract = contract_el.find_element_by_xpath("../..")
    contract = gparent_contract.text[1:]
    
    #print(contract)
    
    
    vehicle_el = browser.find_element_by_xpath("//span[contains(text(), 'LCVehicle')]")
    gparent_vehicle_el = vehicle_el.find_element_by_xpath("../..")
    vehicle = gparent_vehicle_el.text[1:]
    #print(vehicle)
    
    
    subject_app_els = browser.find_elements_by_xpath("//span[contains(text(), 'LCSubject')]")
    
    for s in subject_app_els:
        s_parent = s.find_element_by_xpath("..")
        txts = [ x.text for x in s_parent.find_elements_by_xpath("./b")]
        #print (txts)
        if "applicant" in txts:
            s_gparent = s_parent.find_element_by_xpath("..")
            app = s_gparent.text[1:]
        elif "coapplicant" in txts:
            s_gparent = s_parent.find_element_by_xpath("..")
            coapp = s_gparent.text[1:]
        elif "employer" in txts:
            s_gparent = s_parent.find_element_by_xpath("..")
            employer = s_gparent.text[1:]        
            
    address_app_els = browser.find_elements_by_xpath("//span[contains(text(), 'LCAddress')]")        
    for s in address_app_els:
        s_parent = s.find_element_by_xpath("..")
        txts = [ x.text for x in s_parent.find_elements_by_xpath("./b")]
        #print (txts)
        if "applicantAddress" in txts:
            s_gparent = s_parent.find_element_by_xpath("..")
            app_address = s_gparent.text[1:]


    data = {
        "app": app,
        "app_address": app_address,
        "coapp": coapp,
        "employer": employer,
        "employer_address": employer_address,
        "contract": contract,
        "vehicle": vehicle,        
            }
    return data


#gparent_subject_app_el = subject_app_el.find_element_by_xpath("../..")
#subject_app = gparent_subject_app_el.text[1:]
#print(subject_app)

# 'LCSubject name=\"applicant\"'