#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ToDo - odstranit randomize_old
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
            data_file = "data_spo_m.xml"
        elif gender.lower() in ["f", "female", "z"]:
            gender = "Z" # dle číselníku TFS
            data_file = "data_spo_z.xml"
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

def randomize_old(data, gender="M"):
    
    person_keys = ["TitleBefore", "Name", "Surname", "TitleAfter"]
    person = rnd_person(gender)
    for key in person_keys:
        data["applicant"][key] = person[key]
    
    #coapplicant
    if gender == "M":
        person = rnd_person("Z")
    else:
        person = rnd_person("M")        
    for key in person_keys:
        data["coapplicant"][key] = person[key]

    #guarantor
    guarantor_gender = random.choice(["M", "Z"])
    person = rnd_person(guarantor_gender)
    for key in person_keys:
        data["guarantor"][key] = person[key]
    
    #ToDo dat nar, (rodné číslo ?)

def post_process(data):
    za60 = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime("%d.%m.%Y")
    
    data["vehicle"]["ExpectedDeliveryDate"] = za60


def rnd_person(gender="M"):
    
    #http://prirucka.ujc.cas.cz/?ref=700&id=701
    
    m_jmena = [
         ('Jan', 'Císař'),
         ('Valdemar', 'Matura'),
         ('Libor', 'Šrubař'),
         ('Ferdinand', 'Bažant'),
         ('Vincenc', 'Pala'),
         ('Marek', 'Urbanec'),
         ('Ctibor', 'Hanák'),
         ('Vlastislav', 'Soldán'),
         ('Mikuláš', 'Zámečník'),
         ('Ctirad', 'Hodek'),
         ('Viktor', 'Krčmář'),
         ('Medard', 'Kalič')
             ]

    z_jmena = [
         ('Veronika', 'Holá'),
         ('Diana', 'Škopová'),
         ('Marika', 'Sudová'),
         ('Valérie', 'Hloušková'),
         ('Hedvika', 'Frolíková'),
         ('Marina', 'Kobrová'),
         ('Pavlína', 'Horňáková'),
         ('Bohdana', 'Papoušková'),
         ('Marcela', 'Sloupová'),
         ('Vlasta', 'Šplíchalová'),
         ('Božena', 'Martinovská'),
         ('Milada', 'Špinková'),
         ('Olga', 'Chytilová'),
         ('Diana', 'Štiková'),
         ('Iveta', 'Pavlovská')
        ]
           
    titles_before = [
            'Bc.',
            'BcA.',
            'Ing.',
            'Ing. arch.',
            'MUDr.',
            'MDDr.',
            'MVDr.',
            'MgA.',
            'Mgr.',
            'JUDr.',
            'RNDr.',
            'PharmDr.',
            'ThDr.',
            "",
                 ]
    titles_after = [
            "PhD",
            'PhDr.',
            "CSc",
            "DrSc",
            "MBA",
            "",            
            ]
    if gender =="M":
        jmeno = random.choice(m_jmena)
    else:
        jmeno = random.choice(z_jmena)
    
    
    person = {
            "TitleBefore": random.choice(titles_before),
            "Name": jmeno[0],
            "Surname": jmeno[1],
            "TitleAfter": random.choice(titles_after)
            }
    
    return person

"""
    return (
        app_values,
        app_address_values,
        emp_values,
        coapp_values,
        guar_values,
        guar_address_values,
        vehicle_values,
        contract_values,
    )
"""

"""
app_values = {'TitleBefore': 'ing.', 'Name': 'Pavel', 'Surname': 'Ploc', 'TitleAfter': 'MBA', 'MaritalStatus': '1', 'Foreigner': '0', 'DateOfBirth': '26.1.1979', 'PIN': '7951266884', 'Gender': 'M', 'Citizenship': 'CZ', 'BankAccountNumber1': '31', 'BankAccountNumber': '314159', 'BankCode': '0100', 'DocumentType': '0', 'DocumentNumber': 'OP913746', 'DocumentValidTo': '13.3.2025', 'SecondDocumentType': '6', 'SecondDocumentNumber': 'RP853257', 'SecondDocumentValidTo': '14.12.2027', 'PhoneNumber': '+420398827620', 'Email': 'josef.novak@elposta.cz', "NRKISign":"1"}
app_address_values = {'HomeAddressStreet': 'Koněvova 242', 'HomeAddressCity': 'Praha 3', 'HomeAddressZip': '13000', 'HomeAddressState': 'CZ', 'AddressSame': '0', 'AddressServicesStreet': 'Park Str. 37', 'AddressServicesCity': 'Köln Chorweiler', 'AddressServicesZip': '50765', 'AddressServicesState': 'DE'}
emp_values = {'RegistrationNumber': '04134940', 'ProbationPeriod': '0', 'EmploymentIndefinitePeriod': '0', 'NoticePeriod': '0', 'WorkPhoneNumber': '+420731555999', 'Foreigner': '0', 'EmploymentIndefinitePeriodUntil': '21.11.2020'}
coapp_values = {'TitleBefore': 'ing', 'Name': 'Jana', 'Surname': 'Nováková', 'TitleAfter': 'PhD', 'Foreigner': '0', 'DateOfBirth': '1.1.1970', 'AverageMIAT': '22656', 'AddressServicesStreet': 'Augsburger Strasse 44', 'AddressServicesCity': 'Wershofen', 'AddressServicesZip': '53520', 'AddressServicesState': 'DE'}
za60 = datetime.datetime.now() + datetime.timedelta(days=60).strftime("%d.%m.%Y")
vehicle_values = {"ExpectedDeliveryDate":za60}
contract_values = {"RequestSign":"1"}
"""