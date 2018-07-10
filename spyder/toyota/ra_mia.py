# -*- coding: utf-8 -*-
"""

"""
import xml.etree.ElementTree as ET
import os

#fname = 'NRKI_6901209084.xml'
#fname = "NRKI_6959106286.xml"
#fname= "NRKI_7851047787.xml"
#fname="NRKI_7251068077_predZmenou.xml"
fname="NRKI_7807029912_poZmene.xml"


xmlpath = os.path.join(r'C:\Users\m.houska\Documents\_CIS\Toyota', fname)
tree = ET.parse(xmlpath)
root = tree.getroot()

fic = root.find(".//CustomerData/FoundCustomer/Customer/FIPersonalCode")

# root.findall(".//ContractData/Cards/CardDetail")
# root.findall(".//ContractData/Cards/CardDetail/CommonData/[OpPhase='EX']../ResidualAmount")

# ra_inst   Residual Amount            Installment operations
# ra_cc   Residual Amount            Card operations
# limit_cc  Credit limit               Card operations
# mai_inst  MonthlyInstallment Amount  Installment operations
# mai_cc    MonthlyInstallments Amount Card operations


def get_inst_cc_values():
    card_detail = root.findall(".//ContractData/Cards/CardDetail")
    inst_detail = root.findall(".//ContractData/Installments/InstDetail")
    
    ra_cc = 0
    mai_cc = 0
    limit_cc = 0
    for e in card_detail:
        if e.findall("./CommonData/[OpPhase='EX']"):
            ra_cc_e = e.find("./ResidualAmount").text
            mai_cc_e = e.find("./MonthlyInstalmentAmount").text
            limit_cc_e = e.find("./CreditLimit").text
            #print(e)
            #print (ra_cc_e, mai_cc_e, limit_cc_e)
            ra_cc += int(ra_cc_e or 0)
            mai_cc += int(mai_cc_e or 0)
            limit_cc += int(limit_cc_e or 0)
    #print(ra_cc, mai_cc, limit_cc)
    

    ra_inst = 0
    mai_inst = 0
    for e in inst_detail:
        if e.findall("./CommonData/[OpPhase='EX']"):
            ra_inst_e = e.find("./ResidualAmount").text
            mai_inst_e = e.find("./MonthlyInstalmentAmount").text
            #print(e)
            #print (ra_inst_e, mai_inst_e)
            ra_inst += int(ra_inst_e or 0)
            mai_inst += int(mai_inst_e or 0)
    #print(ra_inst, mai_inst)
    return(ra_cc, mai_cc, limit_cc, ra_inst, mai_inst)
 
def get_score_values():

    score_detail = root.find(".//ContractData/CBScore/ScoreDetails")
    if score_detail:
        score_raw = score_detail.find("./ScoreRaw").text
        cbs_core_range =  score_detail.find("./CBSCoreRange").text
        score_factor =  score_detail.findall(".//ScoreFactor")
        #sf_code = score_detail.findall(".//SFCode")
        #sf_description = score_detail.findall(".//SFDescription")
    else:
        score_raw = None
        cbs_core_range = None
        score_factor = None    
    score_error = root.find(".//ContractData/CBScore/ScoreError")
    
    
    #print(score_raw, cbs_core_range, sf_code, sf_description)
    return (score_raw, cbs_core_range, score_factor, score_error)
    

def residual_amout(ra_inst, ra_cc, limit_cc):
    residual_amount = ra_inst + ra_cc + 0.2 * (limit_cc - ra_cc)
    return residual_amount


def monthly_amount(mai_inst, mai_cc, limit_cc):
    _lim_cc = limit_cc *  0.03
    if mai_cc >= _lim_cc:
        return (mai_inst + mai_cc)
    else:
        return (mai_inst + _lim_cc)

ra_cc, mai_cc, limit_cc, ra_inst, mai_inst =  get_inst_cc_values()
score_raw, cbs_core_range, score_factor, score_error = get_score_values()


if score_error:    
    print(f"Score error Code       : {score_error[0].text}")
    print(f"Score error Description: {score_error[1].text}")   
else:    
    print(f"FIPersonalCode CRIF    : {fic.text if fic is not None else ''}")
    print(f"ScoreRaw               : {score_raw}")
    print(f"CBSCoreRange           : {cbs_core_range}")
    
    for sf in score_factor:
        print(f"SFCode                 : {sf[0].text}")
        print(f"SFDescription          : {sf[1].text}")  

print(f"Celková měsíční splátka: {monthly_amount(mai_inst, mai_cc, limit_cc)}")        
print(f"Zustatkova hodnota     : {residual_amout(ra_inst, ra_cc, limit_cc)}")

