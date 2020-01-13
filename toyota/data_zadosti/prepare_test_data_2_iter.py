# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Dec 16 20:54:02 2019 
"""

import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path


src_fld = Path("c:/DataZadosti")


def read_xlsx_fields():
    xlsx_path = Path("c:/Users/m.houska/Documents/_CIS/Toyota/CZ/IndividualniKalkulace_2019/tvorba_nabidky/field_list.xlsx")
    df_applicant = pd.read_excel (xlsx_path, sheet_name="Applicant")
    df_applicant = df_applicant.sort_values(by=['Field'])
    
    df_vehicle = pd.read_excel (xlsx_path, sheet_name="Vehicle")
    df_vehicle = df_vehicle.sort_values(by=['Field'])
    
    df_contract = pd.read_excel (xlsx_path, sheet_name="Contract")
    df_contract = df_contract.sort_values(by=['Field'])
    
    df_calcul = pd.read_excel (xlsx_path, sheet_name="Calculation")
    df_calcul = df_calcul.sort_values(by=['Field'])

    return (df_applicant, df_vehicle, df_contract, df_calcul)

def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def parse_zadost(path, df_applicant, df_vehicle, df_contract, df_calcul):

    
    

    root = get_root(path)
    applicant = root.find("LCSubject[@name='applicant']")
    vehicle = root.find("LCVehicle")
    contract = root.find("LCContract[@name='contract']")
    calculs = root.find("./LCConnectors/Connector1ACD/result/Calculations")
    calculs_conn = root.find("./LCConnectors/Connector1ACD/result/response/Messages/Message/Response/Calculations")
    calcul_conn_0_itms = calculs_conn[0].items()
    
    req_id = root.find("./LCVariables/ProcessId").text
    subj_type = root.find("LCSubject[@name='applicant']/SubjType").text
    op_type = contract.find("OpType").text
    modality = contract.find("Modality").text
    vehicle_mode = vehicle.find("VehicleMode").text
    vehicle_status = vehicle.find("VehicleStatus").text
    
    
    
    
    subj_type_label_dict = {"1":"Spotřebitel", "2":"Fyzická osoba podnikatel", "3": "Právnická osoba"}
    stl_elem = ET.Element("SubjTypeLabel")
    stl_elem.text = subj_type_label_dict[subj_type]
    applicant.append(stl_elem)
    
    
    op_type_label_dict = {"FC":"Úvěr", "FO":"Operativní Leasing", }
    otl_elem = ET.Element("OpTypeLabel")
    otl_elem.text = op_type_label_dict[op_type]
    contract.append(otl_elem)
    
    modality_label_dict = {"1":"měsíční", "2":"čtvrtletní", }
    modality_elem = ET.Element("ModalityLabel")
    modality_elem.text = modality_label_dict[modality]
    contract.append(modality_elem )
    
    vehicle_mode_label_dict = {"1":"osobní", "3":"Užitkové", }
    vehicle_mode_elem = ET.Element("VehicleModeLabel")
    vehicle_mode_elem.text = vehicle_mode_label_dict[vehicle_mode]
    vehicle.append(vehicle_mode_elem )
    
    
    vehicle_status_label_dict = {"0":"nové", "1":"ojeté", }
    vehicle_status_elem = ET.Element("VehicleStatusLabel")
    vehicle_status_elem.text = vehicle_status_label_dict[vehicle_status]
    vehicle.append(vehicle_status_elem )
    
    

    
    calculs_out = ET.Element("Calculations")
    calculs_out.text = "\n"
    

    
    # nacteni atributu elementu Calculations
    calculs_attrib = calculs.attrib
    calcul_conn_0_itms = calculs_conn[0].items()
    calcul_out_add_atrib = {key:value for (key,value) in calcul_conn_0_itms if key in ["ResidualValue", "ResidualValueWithVAT", "ResidualValuePCT"]}
    calculs_attrib.update(calcul_out_add_atrib)
    

    
    
    offer_out = ET.Element('Offer')
    offer_out.text = "\n"
    
    
    comment = ET.Comment(f" req_id: {req_id}  | subj_type: {subj_type }  | {calculs_attrib}   ")
    comment.tail = "\n\n"
    offer_out.append(comment)
    
    
    comment = ET.Comment(' Applicant ')
    comment.tail = "\n"
    offer_out.append(comment)
    for e_tag in df_applicant["Field"].to_list():
        elem = applicant.find(e_tag)
        if elem is not None:
            #print (elem.tag)
            offer_out.append(elem)
    comment = ET.Comment('  END Applicant ')
    comment.tail = "\n\n"        
    offer_out.append(comment)        
    
    comment = ET.Comment('  Vehicle ')
    comment.tail = "\n"
    offer_out.append(comment)
    for e_tag in df_vehicle["Field"].to_list():
        elem = vehicle.find(e_tag)
        if elem is not None:
            #print (elem.tag)
            offer_out.append(elem)
    comment = ET.Comment('  END Vehicle ')
    comment.tail = "\n\n"        
    offer_out.append(comment)          
    
    comment = ET.Comment('  Contract ')
    comment.tail = "\n"
    offer_out.append(comment)
    for e_tag in df_contract["Field"].to_list():
        elem = contract.find(e_tag)
        if elem is not None:
            #print (elem.tag)
            offer_out.append(elem)
    
    #_ServicePack
    contract_service_pack = ET.Element("_ServicePack")
    contract_service_pack.text = "_fakeServicePack"
    offer_out.append(contract_service_pack)
            
    comment = ET.Comment('  END Contract ')
    comment.tail = "\n\n"        
    offer_out.append(comment)        
    
    
    # preulozeni VYBRANYCH atributu elementu z Calculations do elementu Offer
    comment = ET.Comment(f" Preulozene attributy  a odvozene hodnoty z  Calculations  ")
    comment.tail = "\n"
    offer_out.append(comment)
    
    elem_names = ["ProductCode", "SurrenderValueVAT", "LastAdvancedInstalmentPercent", "RedemptionPrice", "TableType",  "ResidualValue", "ResidualValueWithVAT", "ResidualValuePCT",  ]
    for elem_name in elem_names:
        value = calculs_attrib.get(elem_name, None)
        if value is None:
            continue
        inner_calculs_elem = ET.Element(elem_name)
        inner_calculs_elem.text = value
        inner_calculs_elem.tail = "\n"
        offer_out.append(inner_calculs_elem)
        
    # celkovy rocni najezd
    _MRTMileAgeSum = calculs.find("./Calculation[1]/MRTMileAgeSum")    
    if _MRTMileAgeSum is not None:            
        _MRTMileAgeSum_elem = ET.Element("MRTMileAgeSum")
        _MRTMileAgeSum_elem.text = _MRTMileAgeSum.text
        offer_out.append(_MRTMileAgeSum_elem)
        
        
    comment = ET.Comment(f" END Preulozene attributy  a odvozene hodnoty z  Calculations  ")
    comment.tail = "\n\n"
    offer_out.append(comment)
        
    #vybrana varianta
    selected_offer_number_elem = contract.find("./CalculatedOfferNumber")
    if selected_offer_number_elem is not None:
        selected_offer_number = selected_offer_number_elem.text
    else:
        raise ValueError("chybi CalculatedOfferNumber")
    
    
    field_list = list(zip(df_calcul["Field"].to_list(), df_calcul["DataType"].to_list()))
    for idx, calc in enumerate(calculs):
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
                
        #_CalcCheckBox
        _CalcCheckBox_elem = ET.Element("_CalcCheckBox")
        calculated_offer_number_elem = calc.find("./CalculatedOfferNumber")
        calculated_offer_number = calculated_offer_number_elem.text
        if selected_offer_number == calculated_offer_number:
            _CalcCheckBox_elem.text = "true"
        else:
            _CalcCheckBox_elem.text = "false"
        inner_calc_elem.append(_CalcCheckBox_elem)    
        
        
        #DP, DS, ZP, 
        for elem_name in ["_DP", "_DS", "_ZP"]:
            elem = ET.Element(elem_name)
            elem.text = elem_name + str(idx)
            inner_calc_elem.append(elem)
            
            
                
        calculs_out.append(inner_calc_elem)
            
    # calculs_out.attrib = calculs.attrib
    # calculs_out.attrib.update(calcul_out_add_atrib)
    
    offer_out.append(calculs_out)
    
    
    return offer_out

zadosti = ["zadost_stopTask_190326.xml", 
           "zadost_akceptace_189850.xml",
           "zadost_stopTask_190507.xml", 
           "zadost_3obr_190791.xml", 
           "zadost_akceptace_190623.xml", 
           "zadost_stopTask_190786.xml", ]

df_applicant, df_vehicle, df_contract, df_calcul = read_xlsx_fields()

out_str = ""
for zadost in zadosti:
    path = src_fld / zadost
    

    parsed_zadost = parse_zadost(path, df_applicant, df_vehicle, df_contract, df_calcul)
    
    xml_str = ET.tostring(parsed_zadost, encoding='unicode')
    
    out_str += "\n"
    out_str += xml_str 
    out_str += "\n"


