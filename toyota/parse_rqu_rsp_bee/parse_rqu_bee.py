# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 19:38:07 2019 
"""

import xml.etree.ElementTree as ET
from pathlib import Path


path = Path("C:/tmp/rqu_BEE_Live_po")
path = path / "178248_IN__636975927369383673.xml"

# 178068_IN__636968843102397373
# 178248_IN__636975927369383673 -nrki delikvence

ns = {"cls":"uri:creditinfosolutions/cls",
      "nrki":"nrki_ToDo",
      'urp': 'https://ws.urplus.sk',
      'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03'}

def get_root(path):
    with open(path, encoding="utf-16le") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def get_applicant(root):
    applicant_elem = root.find(".//cls:Applicant", ns)
    if applicant_elem is None:
        print("chybi applicant")
        return None
    return applicant_elem

def get_applicant_subj_type(subj_elem):
    sub_type = ""
    sub_type_elem = subj_elem.find(".//cls:SubjType", ns)
    if sub_type_elem is not None:
        sub_type = sub_type_elem.text
        #print (subj_type_elem)
    return sub_type
        

"""
root =  get_root(path)
applicant_elem = get_applicant(root)
applicant_subj_type = get_applicant_subj_type(applicant_elem)
"""



subj_elem = applicant_elem


applicant_nrki = subj_elem.find(".//cls:ConnectorNrki", ns)
#cr_rep = find(".//CR_REP", ns)
customer_data = subj_elem.find(".//CustomerData", ns)
contract_data = subj_elem.find(".//ContractData", ns)
cbscore = contract_data.find("CBScore", ns)


cbscore_error_code, cbscore_error_desc = "", ""
cbscore_error = cbscore.find("ScoreError", ns)
if cbscore_error is not None:
    cbscore_error_code = cbscore_error.find("Code", ns).text
    cbscore_error_desc = cbscore_error.find("Description", ns).text
    

cbscore_range = ""
cbscore_detail = cbscore.find("ScoreDetails", ns)
if cbscore_detail is not None:
    cbscore_range = cbscore_detail.find("CBSCoreRange", ns).text
    




    


def get_vat_other_stat_facts(subj):
    
    ico = ""
    ico_elems = subj.findall(".//gr:Ico", ns)
    if ico_elems:
        ico = ico_elems[0].text
    
    vatid = ""
    vatid_elems = subj.findall(".//gr:VATID", ns)
    if vatid_elems:
        vatid = vatid_elems[0].text
    
        
    #statutory_list = []
    num_statutories = 0
    statutory_list_elem = subj.find(".//gr:StatutoryList", ns)
    if statutory_list_elem is not None:
        statutories = statutory_list_elem.findall(".//gr:Statutory", ns)
        num_statutories = len(statutories)
    
    other_stat_facts = ""
    other_stat_facts_elems = subj.findall(".//gr:OtherStatutoryFacts", ns)
    if other_stat_facts_elems:
        other_stat_facts = other_stat_facts_elems[0].text

    out = {"ico": ico,
           "vatid": vatid, 
           "num_statutories": num_statutories,
           "other_stat_facts": other_stat_facts,
           }        
    return (out)

"""
StatutoryList
OtherStatutoryFacts

"""