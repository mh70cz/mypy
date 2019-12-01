# -*- coding: utf-8 -*-
"""
uprava requestu pro testovani pocet representatives
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import os


srcpath = Path("C:/BEE_batch/ma_stat")

process_sro = False
if process_sro:
    dstpath = Path("C:/BEE_batch/in_stat_sro")
    file = "189231_master_sro.xml"
    comp_cond = 'row["legal_form_cd"] == "112"'
    
else:
    dstpath = Path("C:/BEE_batch/in_stat_nonsro")
    file = "178557_master_as.xml"
    comp_cond = 'row["legal_form_cd"] != "112"'    
    
    
ns = {"cls":"uri:creditinfosolutions/cls",
      "nrki":"nrki_ToDo",
      'urp': 'https://ws.urplus.sk',
      'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03',
      "types": "http://isirws.cca.cz/types/"}

# prida do elemnetu attrib xmlns="uri:creditinfosolutions/cls" , neni pouzit prefix cls:
ET.register_namespace('',"uri:creditinfosolutions/cls")
# pouzije prefix cls:
#ET.register_namespace('cls',"uri:creditinfosolutions/cls")

ET.register_namespace('nrki',"nrki_ToDo")
ET.register_namespace("types", "http://isirws.cca.cz/types/")
ET.register_namespace("urp", "https://ws.urplus.sk")
ET.register_namespace("cee", "urn:crif-cribiscz-ExekuceGet:2013-01-10")
ET.register_namespace("gr", "urn:crif-cribiscz-GetGlobalReport:2013-05-03")
# 


def get_root(path):
    with open(path, encoding="utf-8") as fp:  
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def get_applicant(root):
    applicant_elem = root.find(".//cls:Applicant", ns)
    if applicant_elem is None:
        print("chybi applicant")
        return None
    return applicant_elem

def get_representative(root):
    representative_elem = root.find(".//cls:Representative", ns)
    if representative_elem is None:
        print("chybi representative")
        return None
    return representative_elem



path = srcpath / file


root = get_root(path)
representative = get_representative(root)
applicant = get_applicant(root)

representative_type_elem = ET.Element("{uri:creditinfosolutions/cls}RepresentativeType")
representative_type_elem.text="1"
representative_type_elem.tail = "\n"+6*" "
representative.insert(1, representative_type_elem)

other_statutory_facts_elem = applicant.find(".//gr:OtherStatutoryFacts", ns)

for idx, row in df2.head(n=600).iterrows():
    
    if row["num_statutories"] != 1 and eval(comp_cond) :
        #print(idx, row["other_stat_facts"])
        new_osf = row["other_stat_facts"]
        file = row["src_file"]

        other_statutory_facts_elem.text = new_osf
        
        path_out = dstpath / file
        print(path_out)
        out_tree = ET.ElementTree(root) # vytvor novy tree 
        out_tree.write(path_out, encoding="utf-8")                

"""



"""    