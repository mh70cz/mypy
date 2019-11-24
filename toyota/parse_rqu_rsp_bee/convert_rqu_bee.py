# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 20:55:30 2019 
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import os


srcpath = Path("C:/BEE_rqu/rqu_BEE_Live_spo")
dstpath = Path("C:/BEE_batch/in_spo")

ns = {"cls":"uri:creditinfosolutions/cls",
      "nrki":"nrki_ToDo",
      'urp': 'https://ws.urplus.sk',
      'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03',
      "types": "http://isirws.cca.cz/types/"}

ET.register_namespace('cls',"uri:creditinfosolutions/cls")
ET.register_namespace('nrki',"nrki_ToDo")
ET.register_namespace("types", "http://isirws.cca.cz/types/")
ET.register_namespace("urp", "https://ws.urplus.sk")
ET.register_namespace("cee", "urn:crif-cribiscz-ExekuceGet:2013-01-10")
ET.register_namespace("gr", "urn:crif-cribiscz-GetGlobalReport:2013-05-03")


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



files = []
for file in os.listdir(srcpath):
    if file.endswith(".xml"):
        files.append(file)

data = []
for file in files[:5]:
    
    path = srcpath / file
    print(path)
    root = get_root(path)
    
    in_elem = root.find(".//cls:In", ns)
    in_elem.attrib["xmlns"] = "uri:creditinfosolutions/cls"
    
    if in_elem is not None:
        cr_rep_elem = in_elem.find(".//CR_REP", ns)
        if cr_rep_elem is not None:
            cr_rep_elem.attrib["xmlns"] = "nrki_ToDo"
            
        conn_isir_elem = in_elem.find(".//cls:ConnectorIsir", ns)
        if conn_isir_elem is not None:
            isir_stav_elem = conn_isir_elem.find(".//stav", ns)
            if isir_stav_elem is not None:
                isir_stav_elem.attrib["xmlns"] = "http://isirws.cca.cz/types/"        
            
        

    
    out_tree = ET.ElementTree(in_elem)
    path_out = dstpath / file
    #out_tree.write(path_out, encoding="utf-16le")
    out_tree.write(path_out, encoding="utf-8")                
    
        
        
        
#    nrki = subj_elem.find(".//cls:ConnectorNrki", ns)
#    if nrki is None:
#        return None
#    
#    if (nrki.attrib["status"] != "ok") and (nrki.attrib["cnavStatus"] != "100"):
#        return None
    
    
"""
in_elem.attrib["xmlns"] = "uri:creditinfosolutions/cls"
out_tree.getroot().tag
in_elem.tag = "{uri:aaa}In"


out_tree = ET.ElementTree(in_elem)
ET.register_namespace('cls',"uri:creditinfosolutions/cls")
ET.register_namespace('nrki',"nrki_ToDo")
ET.register_namespace("types", "http://isirws.cca.cz/types/")
out_tree.write("C:/BEE_batch/in_spo/bflm.xml", encoding="utf-16le")

"""    