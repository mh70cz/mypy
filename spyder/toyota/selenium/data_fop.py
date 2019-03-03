#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
import xml.etree.ElementTree as ET
import datetime
import random
import os
import r_names

def get_data(data_file=None, gender = "M"):
    if data_file is None:
        if gender.lower()  in ["m", "male"]:
            gender = "M"
            data_file = "data_fop_m.xml"
        elif gender.lower() in ["f", "female", "z"]:
            gender = "Z" # dle číselníku TFS
            data_file = "data_fop_z.xml"
        else:
            raise ValueError("unsupported gender")
        
        data = parse_data(data_file)
        randomize(data, gender)
    else:
        data = parse_data(data_file)
    post_process(data)
    
    
    return data

def parse_data(data_file):
    data = {
        "applicant": None,
        "applicant_address": None,
        "employer": None,
        "coapplicant": None,
        "coapplicant_address": None,
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

def randomize(data, gender="M"):
    
   
    person_keys = ["TitleBefore", "Name", "Surname", "TitleAfter", "Email"]
    
    person_pair = r_names.rnd_person_pair(guarantor=False)
    if gender == "M":
        for key in person_keys:
            data["applicant"][key] = person_pair["male"][key]
            data["coapplicant"][key] = person_pair["female"][key]
    elif gender == "Z":
        for key in person_keys:
            data["applicant"][key] = person_pair["female"][key]
            data["coapplicant"][key] = person_pair["male"][key]        

    #guarantor
    guarantor_gender = random.choice(["M", "Z"])
    person = r_names.rnd_person(gender=guarantor_gender, guarantor=True)
    for key in person_keys:
        data["guarantor"][key] = person[key]
    
    #ToDo dat nar, (rodné číslo ?)

def post_process(data):
    za60 = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%d.%m.%Y")
    
    data["vehicle"]["ExpectedDeliveryDate"] = za60


