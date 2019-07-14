# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Jun 24 10:55:54 2019 
"""

import os
import xml.etree.ElementTree as ET


src_dir = r"C:\tmp\PotvrzeniOPojisteni\unzip"
dst_dir = r"C:\Users\m.houska\Documents\_CIS\Toyota\xml" 
src_file = "reportXslt.xslt"
dst_file = "reportXslt_.xslt"


src_path = os.path.join(src_dir, src_file)
dst_path = os.path.join(dst_dir, dst_file)


with open(src_path, encoding='utf-8') as reader:
    src_xml = reader.read()
    #print(type(src_xml))
    
#mod_xml = src_xml.replace("-<","<")

#xml_lines = [] 
lines = src_xml.splitlines()


patterns =["toy:", "cis:", "fmt:"]
for idx, line in enumerate(lines):
    if "xmlns:" in line:
        continue
    for pattern in patterns:
        if pattern in line:
            lines[idx] = "<!-- " + line + " -->"

mod_xml = "\n".join(lines)        


with open(dst_path, 'w', encoding='utf-8') as writer:
    writer.write(mod_xml)