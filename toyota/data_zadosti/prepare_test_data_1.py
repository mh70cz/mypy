# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Dec 16 20:54:02 2019 
"""

import pandas as pd
import xml.etree.ElementTree as ET
from pathlib import Path


src_fld = Path("c:/DataZadosti")
path = src_fld / "zadost_stopTask_190326.xml"

xlsx_path = Path("c:/Users/m.houska/Documents/_CIS/Toyota/CZ/IndividualniKalkulace_2019/tvorba_nabidky/field_list.xlsx")

# zadost_stopTask_190326.xml
# zadost_stopTask_190507.xml
# zadost_3obr_190791.xml
# zadost_akceptace_190623.xml
# zadost_stopTask_190786.xml

"""
%clear

print("\n")
ET.dump(offer_out)
print("\n")
"""

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
calculs_conn = root.find("./LCConnectors/Connector1ACD/result/response/Messages/Message/Response/Calculations")
calcul_conn_0_itms = calculs_conn[0].items()

req_id = root.find("./LCVariables/ProcessId").text
subj_type = root.find("LCSubject[@name='applicant']/SubjType").text
op_type = contract.find("OpType").text
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


vehicle_mode_label_dict = {"1":"osobní", "3":"Užitkové", }
vehicle_mode_elem = ET.Element("VehicleModeLabel")
vehicle_mode_elem.text = vehicle_mode_label_dict[vehicle_mode]
vehicle.append(vehicle_mode_elem )


vehicle_status_label_dict = {"0":"nové", "1":"ojeté", }
vehicle_status_elem = ET.Element("VehicleStatusLabel")
vehicle_status_elem.text = vehicle_status_label_dict[vehicle_status]
vehicle.append(vehicle_status_elem )



# applicant_out = ET.Element("Applicant")
# vehicle_out = ET.Element("Vehicle")
# contract_out = ET.Element('Contract')



calculs_out = ET.Element("Calculations")
calculs_out.text = "\n"

comment = ET.Comment(f" Preulozene attributy   ")
comment.tail = "\n"
calculs_out.append(comment)

# nacteni atributu elementu Calculations
calculs_attrib = calculs.attrib
calcul_conn_0_itms = calculs_conn[0].items()
calcul_out_add_atrib = {key:value for (key,value) in calcul_conn_0_itms if key in ["ResidualValue", "ResidualValueWithVAT", "ResidualValuePCT"]}
calculs_attrib.update(calcul_out_add_atrib)

# preulozeni atributu elementu Calculations do sub/elementu
for elem_name, value in calculs_attrib.items():
        inner_calculs_elem = ET.Element(elem_name)
        inner_calculs_elem.text = value
        inner_calculs_elem.tail = "\n"
        calculs_out.append(inner_calculs_elem)

comment = ET.Comment(f" END Preulozene attributy   ")
comment.tail = "\n\n"
calculs_out.append(comment)



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
comment = ET.Comment('  END Contract ')
comment.tail = "\n\n"        
offer_out.append(comment)        


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

# calculs_out.attrib = calculs.attrib
# calculs_out.attrib.update(calcul_out_add_atrib)

offer_out.append(calculs_out)



"""

%clear

print(f"<!-- req_id: {req_id}  | subj_type: {subj_type }  | {calculs_out.attrib} -->")


print(f"<!-- Applicat  -->")
ET.dump(applicant_out)
print(f"<!-- END Applicat  -->\n")

print(f"<!-- Vehicle  -->")
ET.dump(vehicle_out)
print(f"<!-- END Vehicle  -->\n")

print(f"<!-- Contract  -->")
ET.dump(contract_out)
print(f"<!-- END Contract  -->\n")

ET.dump(calculs_out)



SurrenderValueVAT="442497" LastAdvancedInstalmentPercent="41.55" RedemptionPrice="392077" 

Calculation Version="20171030" 
id="9968FAE3EFB42110E0530100007FFA83" 
OfferDate="2019-12-11" User="DOL" OfficeCode="DPL" VehicleUsage="0" 
VehicleStatus="0" VehicleCategory="0" InstalmentType="1" InstalmentTypeFinancial="1" 
InstalmentTypeInsurance="1" SubjectTypeCode="CT__RAV__NG19_T000854U6__" 
Price="755716" PriceWithVAT="914416" PriceForInsurance="755715.7" 
CampaignCode="KAMPAN_PRO_FO_RENT_V_19_070" ContractLengthMax="48" 
FinancialProductCode="FO_RENT_V" FinancialProductName="Rent (vozidlo)" 
FinancialTypeCode="RNT" FinancialTypeName="Rent" InterestRate="5.49" 
InstalmentCalculationType="1" InstalmentServiceCount="0" 
InstalmentServiceType="BEG" AdvancePaymentAsAmount="0" 
AdvancePaymentPercent="0" AdvancePaymentAmount="0" 
AdvancePaymentWithVAT="0" AdvancePaymentTypeCode="MIM.SPL." 
InstalmentCount="48" FinancedAmount="757516" ContractLength="48" 
FeeValueAsAmount="0" FeeValue="0" FeeValueWithVAT="0" FeeValuePCT="0" 
ResidualValueAsAmount="1" 
ResidualValue="365700" 
ResidualValueWithVAT="442497" 
ResidualValuePCT="41.55" ResidualValueTypeCode="Z" 
CustomerFinancedPart="0" BonusDealerStdAsAmount="0" 
BonusDealerStdPCT="1" BonusDealerStdAmount="7557.16" 
DeadDate="2023-11-30" PenaltyRate="9" 
GeneralTermsCode="OOVPOD-15/09-CZ" 
Hide="false" Selected="false" CalcCode="ADV:PCT0;HP;" >


MRTMileAgeSum





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

calculs_out.attrib = calculs.attrib






for calc in calculs:
    inner_calc_elem = ET.Element("Calculation")
    
    attribs = calc.attrib
    for e_tag, e_data_type in field_list:
        elem_value = attribs.get(e_tag, None)
        if elem_value is not None:
            # data_type = elem.attrib
            print (e_tag + " " + str(e_data_type) + " " + str(elem_value) )
            if e_data_type in ["decimal", "int"] and elem_value is None:
                continue
            inner_elem = ET.Element(e_tag)
            inner_elem.text = elem_value
            inner_elem.tail = "\n"
            inner_calc_elem.append(inner_elem)
    calculs_out.append(inner_calc_elem)     





"""