# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 20:55:30 2019 
"""

from pathlib import Path
import os
import pandas as pd
import parse_global_report

fpath = Path("C:/tmp/Cribis_PO")


files = []
for file in os.listdir(fpath):
    if file.endswith(".xml"):
        files.append(file)

data = []
for file in files:
    path = fpath / file
    #print(path)
    row = parse_global_report.get_vat_other_stat_facts(path)
    row["src_file"] = file
    data.append(row)
    
     
df = pd.DataFrame(data)  

df2 = df.drop_duplicates(subset ="ico",)
