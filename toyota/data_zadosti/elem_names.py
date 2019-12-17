# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Dec  9 16:29:36 2019 
"""

import xml.etree.ElementTree as ET
from pathlib import Path


src_fld_path = Path("C:/DataZadosti")
path = src_fld_path / "zadost_1obr_7588.xml"


"""
7588 SPO, uver, nove, osobni
7589 SPO, operL, nove, osobni
7590 SPO, uver, ojete, osobni
7591 FOP, uver, nove, osobni
7592 FOP, operL, nove, osobni
7593 FOP, uver, ojete, uzitkove

"""

def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

root =  get_root(path)
contract = root.find("./LCContract")
variables = root.find("./LCVariables")
vehicle = root.find("./LCVehicle")
applicant = root.find("./LCSubject[@name='applicant']")

contract_elem_names = []
variables_elem_names = []
vehicle_elem_names = []
applicant_elem_names = []


for e in contract:
    contract_elem_names.append(e.tag)

for e in variables:
    variables_elem_names.append(e.tag)
    
for e in vehicle:
    vehicle_elem_names.append(e.tag)

for e in applicant:
    applicant_elem_names.append(e.tag)    
    












"""
root =  get_root(path)





zadosti = ["zadost_1obr_7588.xml", "zadost_1obr_7589.xml", "zadost_1obr_7590.xml", "zadost_1obr_7591.xml", "zadost_1obr_7592.xml", "zadost_1obr_7593.xml", ]


for z in zadosti:
    root =  get_root(path)
    contract = root.find("./LCContract")
    variables = root.find("./LCVariables")
    vehicle = root.find("./LCVehicle")
    applicant = root.find("./LCSubject[@name='applicant']")
    
    print ("\n" + z + "\n")
    
    print ("contract: " + str(len(contract)))
    print ("variables: " + str(len(variables)))
    print ("vehicle: " + str(len(vehicle)))
    print ("applicant: " + str(len(applicant)))

"""