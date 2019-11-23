# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 20:55:30 2019 
"""

from pathlib import Path
import os
import pandas as pd
import parse_rqu_bee

fpath_spo = Path("C:/tmp/rqu_BEE_Live_spo")
fpath_fop = Path("C:/tmp/rqu_BEE_Live_fop")

#fpath = fpath_spo

paths = []
for fpath in [fpath_spo, fpath_fop]:
    for file in os.listdir(fpath):
        if file.endswith(".xml"):
            path = fpath / file
            paths.append(path)     

data = []
for path in paths[:]:
    
    print(path)
    file = path.name
    
    row = {}
    root = parse_rqu_bee.get_root(path)
        
    applicant_elem = parse_rqu_bee.get_applicant(root)

    app = parse_rqu_bee.get_applicant_info(applicant_elem)
    
    
    row = {
            #"ico": app["ico"],            
           }

    lsd_first_out = {}
    lsd_first = parse_rqu_bee.get_lsd(applicant_elem, order="first")
    if lsd_first is not None:
        lsd_first_out = {"lsd_1_sta_code": lsd_first["status_code"],
                         "lsd_1_rsp_value": lsd_first["response_value"],
                   }

    lsd_second_out = {}
    lsd_second = parse_rqu_bee.get_lsd(applicant_elem, order="second")
    if lsd_second is not None:
        lsd_second_out = {"lsd_2_sta_code": lsd_second["status_code"],
                          "lsd_2_rsp_value": lsd_second["response_value"],
                   }        
    
    row.update(lsd_first_out, **lsd_second_out)
    row["rqu_id_f"] = file[:6]
    row["src_file"] = file
    data.append(row)
    
     
df = pd.DataFrame(data)  

df2 = df.drop_duplicates(subset ="rqu_id_f",) # podle id zadosti
#df2 = df.drop_duplicates(subset ="pin",)    # podle RC


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