# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Thu Nov 21 16:53:22 2019 
"""

from pathlib import Path
import os
from shutil import copyfile
import parse_rqu_bee

srcfld = Path("C:/BEE_rqu/rqu_BEE_Live__new")
dstfld_spo = Path("C:/BEE_rqu/rqu_BEE_Live_spo")
dstfld_fop = Path("C:/BEE_rqu/rqu_BEE_Live_fop")
dstfld_po = Path("C:/BEE_rqu/rqu_BEE_Live_po")


max_files  = 2000
cnt_files = 0
cnt_spo, cnt_fop, cnt_po, cnt_err = 0, 0, 0, 0

for file in os.listdir(srcfld):
    
    cnt_files += 1
    if cnt_files > max_files:
        break
    
    path = srcfld / file
    root =  parse_rqu_bee.get_root(path)
    
    applicant_elem = parse_rqu_bee.get_applicant(root)
    if applicant_elem == None:
        print ("chyba v SubjType - None " + file)
        cnt_err += 1
        continue
    
    applicant_subj_type = parse_rqu_bee.get_applicant_info(applicant_elem)["subj_type"]

    print(applicant_subj_type)
        
    if applicant_subj_type == "1":
        dstpath = dstfld_spo / file
        cnt_spo += 1
    elif applicant_subj_type == "2":
        dstpath = dstfld_fop / file
        cnt_fop += 1
    elif applicant_subj_type == "3":
        dstpath = dstfld_po / file
        cnt_po += 1
    else:
        print ("chyba v SubjType " + file)
        dstpath = None
        cnt_err += 1

    print (dstpath)
    copyfile(path, dstpath)
    
print (f"cnt_spo: {cnt_spo}, cnt_fop: {cnt_fop}, cnt_po: {cnt_po}, cnt_err: {cnt_err}")
    