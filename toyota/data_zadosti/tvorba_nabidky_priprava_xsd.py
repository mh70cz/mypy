# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Mon Dec 16 18:44:08 2019 
"""

import pandas as pd

df = pd.read_excel (r'c:/tmp/book.xlsx', sheet_name="Calculation")
# Calculation


df = df.sort_values(by=['Field'])

"""
<xs:element name="DealerUserName" type="xs:string" nillable="0">
	<xs:annotation>
		<xs:documentation>Jméno uživatele, který založil kalkulaci a případně kód jeho složky</xs:documentation>
	</xs:annotation>
</xs:element>
"""


for index, row in df.iterrows():

    elem_1 = f'<xs:element name="{row["Field"]}" type="xs:{row["DataType"]}" minOccurs="0">'
    anno_1 = f'\n  <xs:annotation>\n    <xs:documentation>{row["Desc"]}</xs:documentation>'
    anno_2 = '\n  </xs:annotation>'
    elem_2 = '\n</xs:element>'
    print(elem_1 + anno_1 + anno_2 + elem_2)
