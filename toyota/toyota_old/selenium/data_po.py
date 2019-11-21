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

def get_data(data_file=None, ico=None, guarantor="po"):
    if data_file is None:
        if guarantor == "po":
            data_file = "data_po_g_po.xml"
        else:         
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
        "guarantorRepresentative": None,
        "guarantorRepresentativeAddress": None,
        "guarantorRepresentative1": None,
        "guarantorRepresentative1Address": None,
        "guarantorRepresentative2": None,
        "guarantorRepresentative2Address": None,          
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

    # subject (element: string, guarantor: boolean, representative: boolean)
    subjects = [
     ('representative', False, True),
     ('representative1', False, True),
     ('representative2', False, True),
     #("guarantor", True, False),
     ('guarantorRepresentative', True, True),
     ('guarantorRepresentative1', True, True),
     ('guarantorRepresentative2', True, True),
     ]
    
    for s in subjects:
        sex, pin, dat_nar = r_rc_ico.rc_dat()
        person = r_names.rnd_person(gender=sex, guarantor=s[1], representative=s[2])
        for key in person_keys:
            data[s[0]][key] = person[key]
        data[s[0]]["PIN"] = pin
        data[s[0]]["DateOfBirth"] = dat_nar    
       
#    #representatives
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), representative=True)
#    for key in person_keys:
#        data["representative"][key] = person[key]
#        
#    #representatives1
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), representative=True)
#    for key in person_keys:
#        data["representative1"][key] = person[key]
#
#    #representatives2
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), representative=True)
#    for key in person_keys:
#        data["representative2"][key] = person[key]
#    
#    
#    #guarantor
#    sex, pin, dat_nar = r_rc_ico.rc_dat()
#    person = r_names.rnd_person(gender=sex, guarantor=True)
#    for key in person_keys:
#        data["guarantor"][key] = person[key]
#    data["guarantor"]["Gender"] = sex
#    data["guarantor"]["PIN"] = pin
#    data["guarantor"]["DateOfBirth"] = dat_nar
#    
#    #guarantor representative
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), guarantor=True, representative=True)
#    for key in person_keys:
#        data["guarantorRepresentative"][key] = person[key]
#        
#    #guarantor representative 1
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), guarantor=True, representative=True)
#    for key in person_keys:
#        data["guarantorRepresentative1"][key] = person[key]
#
#    #guarantor representative 2
#    person = r_names.rnd_person(gender=random.choice(["M", "Z"]), guarantor=True, representative=True)
#    for key in person_keys:
#        data["guarantorRepresentative2"][key] = person[key]    
#    
    if ico is not None:
        data["applicant"]["TaxRegistrationNumber"] = "CZ" + str(ico)
    

def post_process(data):
    za60 = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%d.%m.%Y")
    
    data["vehicle"]["ExpectedDeliveryDate"] = za60


