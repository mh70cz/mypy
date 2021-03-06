# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 20:55:30 2019 
"""

from pathlib import Path
import os
import pandas as pd
import parse_rqu_bee

fld_path_fop = Path("C:/BEE_rqu/rqu_BEE_Live_fop")
fld_path_po = Path("C:/BEE_rqu/rqu_BEE_Live_po")


paths = []
for fld_path in [fld_path_fop, fld_path_po]:
    for file in os.listdir(fld_path):
        if file.endswith(".xml"):
            path = fld_path / file
            paths.append(path)

data = []
for path in paths[:]:
    print(path)
        
    root = parse_rqu_bee.get_root(path)
            
    applicant_elem = parse_rqu_bee.get_applicant(root)

    app = parse_rqu_bee.get_applicant_info(applicant_elem)

    row = { "subj_type_dcm": app["subj_type"], 
            #"num_repr": parse_rqu_bee.get_representatives(root, num_only=True),
            #"ico": app["ico"],  
            
            }
    
    gr_info_out ={}
    gr_root = parse_rqu_bee.get_global_report(applicant_elem)
    if gr_root is not None:      
        gr = gr_root["gr"]
        gr_info = parse_rqu_bee.get_global_report_info(gr)
        gr_info_out = {"ico_gr": gr_info["ico"],
                       #"vatid_gr": gr_info["vatid"],
                       #"num_stat": gr_info["num_statutories"],
                       #"other_stat_facts": gr_info["other_stat_facts"],
                       #"stries_positions": gr_info["stries_positions"],                       
                       "legal_form_cd": gr_info["legal_form_cd"],
                       "legal_form": gr_info["legal_form"],
                       "subj_type_gr": gr_info["subj_type"],                       
                       }
        
    row.update(gr_info_out)

    file = path.name
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