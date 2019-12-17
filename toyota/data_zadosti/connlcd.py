# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Tue Dec 10 15:13:54 2019 
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import pandas as pd


src_fld_path = Path("C:/tmp")
path = src_fld_path / "reportSchema.xsd"

ns = {"xs":"http://www.w3.org/2001/XMLSchema",}

def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root


root =  get_root(path)
#seq = root.find("./xs:element[@name='LCContract']/xs:complexType/xs:sequence", ns)
#seq = root.find("./xs:element[@name='LCSubject']/xs:complexType/xs:sequence", ns)
#seq = root.find("./xs:element[@name='LCVariables']/xs:complexType/xs:sequence", ns)
#seq = root.find("./xs:element[@name='LCVehicle']/xs:complexType/xs:sequence", ns)



data = []


seq = root.find(".//xs:element[@name='Connector1ACD']/xs:complexType/xs:sequence", ns)
for s in seq:
    name = s.attrib["name"]
    type_ = s.attrib["type"].replace("xs:","")
    
    doc = ""
    doc_elem = s.find("./xs:annotation/xs:documentation",ns)
    if doc_elem is not None:
        doc = doc_elem.text
    
    data.append({"name": name, "type": type_, "doc": doc,})
    print ( str(name) + " " + str(type_) + " " + str(doc))
    
    
df = pd.DataFrame(data)