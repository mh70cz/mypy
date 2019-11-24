# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 20:55:30 2019 
"""

from pathlib import Path
import os
import pandas as pd
import parse_rqu_bee

fpath = Path("C:/BEE_rqu/rqu_BEE_Live_po")


files = []
for file in os.listdir(fpath):
    if file.endswith(".xml"):
        files.append(file)

data = []
for file in files[:100]:
    
    path = fpath / file
    print(path)

    
    row = {}
    root = parse_rqu_bee.get_root(path)
        
    applicant_elem = parse_rqu_bee.get_applicant(root)

    app = parse_rqu_bee.get_applicant_info(applicant_elem)
    
    gr_info_out ={}
    gr_root = parse_rqu_bee.get_global_report(applicant_elem)
    if gr_root is not None:      
        gr = gr_root["gr"]
        gr_info = parse_rqu_bee.get_global_report_info(gr)
        gr_info_out = {"ico_gr": gr_info["ico"],
                       "vatid_gr": gr_info["vatid"],
                       "num_statutories": gr_info["num_statutories"],
                       "other_stat_facts": gr_info["other_stat_facts"],
                       }
    
    row = {
            #"ico": app["ico"],            
           }
    
    row.update(gr_info_out)

    row["rqu_id_f"] = file[:6]
    row["src_file"] = file
    data.append(row)
    
     
df = pd.DataFrame(data)  

#df2 = df.drop_duplicates(subset ="rqu_id_f",) # podle id zadosti
df2 = df.drop_duplicates(subset ="ico_gr",)    # podle ico


"""
    applicant_subj_type = parse_rqu_bee.get_applicant_subj_type(applicant_elem)
    row["applicant_subj_type"] = applicant_subj_type
    
    nrki =  parse_rqu_bee.get_nrki(applicant_elem)
    if nrki is not None:
        contract_data =  nrki["contract_data"]    
        cbs = parse_rqu_bee.get_nrki_cbscore(contract_data)
        row["cbs"] = cbs
    
    gr_root = parse_rqu_bee.get_global_report(applicant_elem)
    if gr_root is not None:      
        gr = gr_root["gr"]
        gr_info = parse_rqu_bee.get_global_report_info(gr)
        row["gr_info"] = gr_info
    

    row["src_file"] = file
    data.append(row)
    
     
df = pd.DataFrame(data)  

# df2 = df.drop_duplicates(subset ="ico",)

"""