# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 19:38:07 2019 
"""

import xml.etree.ElementTree as ET
from pathlib import Path

path = Path("C:/tmp/Cribis_PO")
path = path / "_Out637098686141202667.xml"

def get_vat_other_stat_facts(path):

    ns = {'urp': 'https://ws.urplus.sk',
          'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03'}
    
    with open(path, encoding="utf-8") as fp:
        tree = ET.parse(fp)
    root = tree.getroot()
    
    
    ico = ""
    ico_elems = root.findall(".//gr:Ico", ns)
    if ico_elems:
        ico = ico_elems[0].text
    
    vatid = ""
    vatid_elems = root.findall(".//gr:VATID", ns)
    if vatid_elems:
        vatid = vatid_elems[0].text
    
        
    #statutory_list = []
    num_statutories = 0
    statutory_list_elem = root.find(".//gr:StatutoryList", ns)
    if statutory_list_elem:
        statutories = statutory_list_elem.findall(".//gr:Statutory", ns)
        num_statutories = len(statutories)
    
    other_stat_facts = ""
    other_stat_facts_elems = root.findall(".//gr:OtherStatutoryFacts", ns)
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