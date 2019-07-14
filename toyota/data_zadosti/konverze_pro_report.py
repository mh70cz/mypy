# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Jun 24 10:03:14 2019 

konverze dat zadosti //items/item do formy, kdy lze spustit xslt konverzi pro Xtra rep
"""
import os
import xml.etree.ElementTree as ET


src_dir = r"C:\Users\m.houska\Documents\_CIS\Toyota\xml"
dst_dir = src_dir 
src_file = "178068_src.xml"
dst_file = "178068_dst.xml"


src_path = os.path.join(src_dir, src_file)
dst_path = os.path.join(dst_dir, dst_file)


with open(src_path, encoding='utf-8') as reader:
    src_xml = reader.read()
    #print(type(src_xml))
    
mod_xml = src_xml.replace("-<","<")


with open(dst_path, 'w', encoding='utf-8') as writer:
    writer.write(mod_xml)