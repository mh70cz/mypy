#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:24:33 2018



trivial date format inferrer
dateparser https://dateparser.readthedocs.io/en/latest/
dateinfer
"""

from enum import Enum
from datetime import datetime
from collections import Counter

class DateFormat(Enum):
    DDMMYY = 0
    MMDDYY = 1
    YYMMDD = 2
    #DDMMYYYY = 3
    NONPARSABLE = -999
    
    @classmethod
    def d_parse_formats(cls, idx=None):
        d_parse_formats = ["%d/%m/%y", "%m/%d/%y", "%y/%m/%d"]
        if idx is None:
            return d_parse_formats
        if 0 <= idx < len(d_parse_formats):
            return d_parse_formats[idx]
        raise ValueError
        
    
    
    
#
#dates_a = ['11/11/07', '01/05/07', '05/12/04', '06/11/01', '10/03/09', 
#           '10/08/09', '04/11/11', '02/05/10', '05/10/08', '12/03/01', 
#           '10/10/12', '03/10/02']
#
#dates_b = ['04/25/79', '08/09/70', '08/04/10', '95/31/10', '06/13/34',
#           '04/03/22', '67/12/17', '34/10/12', '04/05/94', '07/12/41', 
#           '88/11/05', '96/26/08']
#
#dates_c = ['12/22/68', '31/09/87', '37/03/29', '11/28/03', '02/03/32',
#           '18/08/74', '46/09/27', '49/07/10', '05/31/88', '28/12/17',
#           '71/04/19', '85/08/09']
#
#dates_d = ['10/21/05', '06/10/05', '06/05/08', '28/16/07', '10/07/90',
#           '29/06/60', '46/11/02', '10/17/05', '11/08/94', '02/02/60', 
#           '65/04/15', '62/14/12']
#
#dates_x = ['12/16/30', '16.03.1954', '97/07/26', '04.04.1931', '01/08/07', 
#   '02/02/29', '73/03/08', '06.07.1955', '10/09/77', '18.03.1943', 
#   '30/11/24', '08.01.1951']


def _inf_date_formats(date_str):
    d_parse_formats = DateFormat.d_parse_formats()
    maybe_formats = []
    for idx, d_parse_fmt in enumerate(d_parse_formats):
        try:
            parsed_date = datetime.strptime(date_str, d_parse_fmt)
            maybe_formats.append(DateFormat(idx))
        except ValueError:
            pass
    if len(maybe_formats) == 0:
        maybe_formats.append(DateFormat.NONPARSABLE)
    return maybe_formats

dates = [
    "12/16/30",
    "16/03/54",
    "97/07/26",
    "04/04/31",
    "01/08/07",
    "02/02/29",
    "73/03/08",
    "06/07/55",
    "10/09/77",
    "18/03/43",
    "30/11/24",
    "08/01/51",
]


total_possible_d_formats = []
for date_str in dates:
#    d1 = date[0:2]
#    d2 = date[3:5]
#    d3 = date[5:7]
    possible_d_formats = _inf_date_formats(date_str)
    total_possible_d_formats.extend(possible_d_formats)
cnt_d_formats = Counter(total_possible_d_formats) 

if len(cnt_d_formats.most_common()) > 1: 
    if cnt_d_formats.most_common()[0][1] == cnt_d_formats.most_common()[1][1]:
        #tie    
        print("Cannot decide")

if cnt_d_formats.most_common()[0][0] == DateFormat.NONPARSABLE:
    print ("Too many invalid dates to infer a date format")
    
d_format_value = cnt_d_formats.most_common()[0][0].value
d_parse_format = DateFormat.d_parse_formats(d_format_value)

out_dates = []
for date_str in dates:
    try:
        date = datetime.strptime(date_str, d_parse_format)
        date = datetime.strftime(date,"%Y-%m-%d")
        out_dates.append(date)
    except ValueError:
        out_dates.append("Invalid")
    
    

     
    
    
    
    
        
        
    
    
    