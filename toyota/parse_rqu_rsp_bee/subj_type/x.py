# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Thu Dec  5 14:55:51 2019 
"""

import pandas as pd

df = pd.read_excel (r'C:\Users\m.houska\Documents\_CIS\Toyota\CZ\SubjType_LegalFormCd.xlsx', sheet_name='unit_test')
# df = df.drop(columns=['Excel_result'])

df_out =  df.astype({
        'Ico': str, 
        'LegalForm': str, 
        'LegalFormCd': str, 
        'GR_SubjType': str, 
        'DcM_SubjType': int,
        "Result": bool,
        })



with open(r'C:\tmp\subj_type_unit_test.json', 'w', encoding='utf-8') as file:
    df_out.to_json(file, orient='records' ,force_ascii=False)