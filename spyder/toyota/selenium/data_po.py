#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import xml.etree.ElementTree as ET
import datetime
import random
import os
import r_names
import r_rc_ico

def get_data(data_file=None, ico=None):
    if data_file is None:
        data_file = "data_po.xml"        
        data = parse_data(data_file)
        randomize(data, ico)
    else:
        data = parse_data(data_file)
    post_process(data)
    
    
    return data

def parse_data(data_file):
    data = {
        "applicant": None,
        "applicant_address": None,
        "representative": None,
        "representativeAddress": None,
        "representative1": None,
        "representative1Address": None,
        "representative2": None,
        "representative2Address": None,        
        "guarantor": None,
        "guarantor_address": None,
        "guarantor_employer": None,
        "vehicle": None,
        "contract": None,
            }

    path = os.path.join("data", data_file) 
    tree = ET.parse(path)
    root = tree.getroot()
    
    for key in data:
        top_elem = root.find("./" + key)
        if top_elem is not None:
            data[key] = {}
            for node in top_elem:
                value = node.text
                data[key][node.tag] = value

    return data

def randomize(data,  ico=None):
    
    person_keys = ["TitleBefore", "Name", "Surname", "TitleAfter", "Email"]    
       
    #representatives
    representative_gender = random.choice(["M", "Z"])
    person = r_names.rnd_person(gender=representative_gender, guarantor=True)
    for key in person_keys:
        data["representative"][key] = person[key]
        
    #representatives1
    representative1_gender = random.choice(["M", "Z"])
    person = r_names.rnd_person(gender=representative1_gender, guarantor=True)
    for key in person_keys:
        data["representative1"][key] = person[key]

    #representatives2
    representative2_gender = random.choice(["M", "Z"])
    person = r_names.rnd_person(gender=representative2_gender, guarantor=True)
    for key in person_keys:
        data["representative2"][key] = person[key]
    
    
    #guarantor
    sex, pin, dat_nar = r_rc_ico.rc_dat()
    person = r_names.rnd_person(gender=sex, guarantor=True)
    for key in person_keys:
        data["guarantor"][key] = person[key]
    data["guarantor"]["Gender"] = sex
    data["guarantor"]["PIN"] = pin
    data["guarantor"]["DateOfBirth"] = dat_nar
    
    
    
    if ico is not None:
        data["applicant"]["TaxRegistrationNumber"] = "CZ" + str(ico)
    
    #ToDo dat nar, (rodné číslo ?)

def post_process(data):
    za60 = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%d.%m.%Y")
    
    data["vehicle"]["ExpectedDeliveryDate"] = za60


