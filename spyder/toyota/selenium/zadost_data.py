# -*- coding: utf-8 -*-
"""

"""
id_zadost = "7556"
web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/" 
url = web_app + "processing/processData.aspx?id=" + id_zadost


browser.get(url)


contract_el = browser.find_element_by_xpath("//span[contains(text(), 'LCContract')]")
gparent_contract = contract_el.find_element_by_xpath("../..")
contract = gparent_contract.text[1:]

#print(contract)


vehicle_el = browser.find_element_by_xpath("//span[contains(text(), 'LCVehicle')]")
gparent_vehicle_el = vehicle_el.find_element_by_xpath("../..")
vehicle = gparent_vehicle_el.text[1:]
print(vehicle)


subject_app_els = browser.find_elements_by_xpath("//span[contains(text(), 'LCSubject')]")

for s in subject_app_els:
    s_parent = s.find_element_by_xpath("..")
    txts = [ x.text for x in s_parent.find_elements_by_xpath("./b")]
    #print (txts)
    if "applicant" in txts:
        s_gparent = s_parent.find_element_by_xpath("..")
        app_subject = s_gparent.text[1:]
    elif "coapplicant" in txts:
        s_gparent = s_parent.find_element_by_xpath("..")
        coapp_subject = s_gparent.text[1:]
    elif "employer" in txts:
        s_gparent = s_parent.find_element_by_xpath("..")
        employer_subject = s_gparent.text[1:]        

#gparent_subject_app_el = subject_app_el.find_element_by_xpath("../..")
#subject_app = gparent_subject_app_el.text[1:]
#print(subject_app)

# 'LCSubject name=\"applicant\"'