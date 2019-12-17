# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Dec 16 20:54:02 2019 
"""

import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path


src_fld = Path("c:/DataZadosti")
path = src_fld / "zadost_stopTask_190786.xml"

xlsx_path = Path("c:/Users/m.houska/Documents/_CIS/Toyota/CZ/IndividualniKalkulace_2019/tvorba_nabidky/field_list.xlsx")

# zadost_stopTask_190507.xml
# zadost_3obr_190791.xml
# zadost_akceptace_190623.xml
# zadost_stopTask_190786.xml

df_applicant = pd.read_excel (xlsx_path, sheet_name="Applicant")
df_applicant = df_applicant.sort_values(by=['Field'])

df_vehicle = pd.read_excel (xlsx_path, sheet_name="Vehicle")
df_vehicle = df_vehicle.sort_values(by=['Field'])

df_contract = pd.read_excel (xlsx_path, sheet_name="Contract")
df_contract = df_contract.sort_values(by=['Field'])

df_calcul = pd.read_excel (xlsx_path, sheet_name="Calculation")
df_calcul = df_calcul.sort_values(by=['Field'])



def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root



root = get_root(path)
applicant = root.find("LCSubject[@name='applicant']")
vehicle = root.find("LCVehicle")
contract = root.find("LCContract[@name='contract']")
calculs = root.find("./LCConnectors/Connector1ACD/result/Calculations")

req_id = root.find("./LCVariables/ProcessId").text
subj_type = root.find("LCSubject[@name='applicant']/SubjType").text

applicant_out = ET.Element("Applicant")
vehicle_out = ET.Element("Vehicle")
contract_out = ET.Element('Contract')
calculs_out = ET.Element("Calculations")
calculs_out.attrib = calculs.attrib

for e_tag in df_applicant["Field"].to_list():
    elem = applicant.find(e_tag)
    if elem is not None:
        #print (elem.tag)
        applicant_out.append(elem)

for e_tag in df_vehicle["Field"].to_list():
    elem = vehicle.find(e_tag)
    if elem is not None:
        #print (elem.tag)
        vehicle_out.append(elem)

for e_tag in df_contract["Field"].to_list():
    elem = contract.find(e_tag)
    if elem is not None:
        #print (elem.tag)
        contract_out.append(elem)
        


field_list = list(zip(df_calcul["Field"].to_list(), df_calcul["DataType"].to_list()))

for calc in calculs:
    inner_calc_elem = ET.Element("Calculation")
    
    for e_tag, e_data_type in field_list:
        elem = calc.find(e_tag)
        if elem is not None:
            data_type = elem.attrib
            # print (elem.tag + " " + str(e_data_type))
            if e_data_type in ["decimal", "int"] and elem.text is None:
                continue
            inner_elem = ET.Element(elem.tag)
            inner_elem.text = elem.text
            inner_elem.tail = "\n"
            inner_calc_elem.append(inner_elem)
    calculs_out.append(inner_calc_elem)    



"""

print(f"<!-- req_id: {req_id}  | subj_type: {subj_type }  | {calculs_out.attrib} -->")

ET.dump(applicant_out)
ET.dump(vehicle_out)
ET.dump(contract_out)
ET.dump(calculs_out)


"""