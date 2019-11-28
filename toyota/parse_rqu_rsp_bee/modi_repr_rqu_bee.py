# -*- coding: utf-8 -*-
"""
uprava requestu pro testovani pocet representatives
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import os


#srcpath = Path("C:/BEE_rqu/rqu_BEE_Live_spo")
#dstpath = Path("C:/BEE_batch/in_spo")

#srcpath = Path("C:/BEE_rqu/rqu_BEE_Live_fop")
#dstpath = Path("C:/BEE_batch/in_fop")

srcpath = Path("C:/BEE_batch/ma_stat")
dstpath = Path("C:/BEE_batch/in_stat")

file = "189231_IN__637098581329698681.xml"

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


print(path)
root = get_root(path)
representative = get_representative(root)
applicant = get_applicant(root)

representative_type_elem = ET.Element("{uri:creditinfosolutions/cls}RepresentativeType")
representative_type_elem.text="1"
representative_type_elem.tail = "\n"+6*" "
representative.insert(1, representative_type_elem)


new_osf = "bflmpsvz"

other_statutory_facts_elem = applicant.find(".//gr:OtherStatutoryFacts", ns)
other_statutory_facts_elem.text = new_osf

path_out = dstpath / file
out_tree = ET.ElementTree(root) # vytvor novy tree 
out_tree.write(path_out, encoding="utf-8")                



"""

OtherStatutoryFacts

files = []
for file in os.listdir(srcpath):
    if file.endswith(".xml"):
        files.append(file)

data = []
for file in files[-10:]:
    
    path = srcpath / file
    print(path)
    root = get_root(path)
    
    in_elem = root.find(".//cls:In", ns)
    
    # ET.register_namespace('',"uri:creditinfosolutions/cls") zajisti pridani 
    # xmlns="uri:creditinfosolutions/cls" attributu do elementu, nasleduji radek
    # by zpusobil duplicitni vyskyt tohoto attributu
    #in_elem.attrib["xmlns"] = "uri:creditinfosolutions/cls"
    
    
    # oprava 2 chybnych ns -- poresit s Petrem J.
    if in_elem is not None:
        cr_rep_elem = in_elem.find(".//CR_REP", ns)
        if cr_rep_elem is not None:
            cr_rep_elem.attrib["xmlns"] = "nrki_ToDo" 
            
        conn_isir_elem = in_elem.find(".//cls:ConnectorIsir", ns)
        if conn_isir_elem is not None:
            isir_stav_elem = conn_isir_elem.find(".//stav", ns)
            if isir_stav_elem is not None:
                isir_stav_elem.attrib["xmlns"] = "http://isirws.cca.cz/types/"        
            
        

    
    out_tree = ET.ElementTree(in_elem) # vytvor novy tree 
    path_out = dstpath / file
    #out_tree.write(path_out, encoding="utf-16le")  # BEE neakceptuje(?)
    out_tree.write(path_out, encoding="utf-8")                
    
            
"""    
"""
in_elem.attrib["xmlns"] = "uri:creditinfosolutions/cls"
out_tree.getroot().tag
in_elem.tag = "{uri:aaa}In"


out_tree = ET.ElementTree(in_elem)
ET.register_namespace('',"uri:creditinfosolutions/cls")
ET.register_namespace('nrki',"nrki_ToDo")
ET.register_namespace("types", "http://isirws.cca.cz/types/")
out_tree.write("C:/BEE_batch/in_spo/bflm.xml", encoding="utf-16le")

"""    