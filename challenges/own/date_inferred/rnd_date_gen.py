#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 21:24:33 2018

Primitive date inferrer
"""
import random

dates_a = ['11/11/07', '01/05/07', '05/12/04', '06/11/01', '10/03/09', 
           '10/08/09', '04/11/11', '02/05/10', '05/10/08', '12/03/01', 
           '10/10/12', '03/10/02']

dates_b = ['04/25/79', '08/09/70', '08/04/10', '95/31/10', '06/13/34',
           '04/03/22', '67/12/17', '34/10/12', '04/05/94', '07/12/41', 
           '88/11/05', '96/26/08']

dates_c = ['12/22/68', '31/09/87', '37/03/29', '11/28/03', '02/03/32',
           '18/08/74', '46/09/27', '49/07/10', '05/31/88', '28/12/17',
           '71/04/19', '85/08/09']

dates_d = ['10/21/05', '06/10/05', '06/05/08', '28/16/07', '10/07/90',
           '29/06/60', '46/11/02', '10/17/05', '11/08/94', '02/02/60', 
           '65/04/15', '62/14/12']

def _rand(n=12):
    r = random.randint(1,n)
    if r < 10:
        r = "0" + str(r)
    else:
        r = str(r)
    return r

dates = []
for n in range(3):
    rand_date = _rand() + "/" + _rand(31) + "/" + _rand(99)
    dates.append(rand_date)
    rand_date = _rand(31) + "/" + _rand() + "/" + _rand(99)
    dates.append(rand_date)
    rand_date = _rand(99) + "/" + _rand() + "/" + _rand(31)
    dates.append(rand_date)
    
    rand_date = _rand(31) + "/" + _rand() + "/" + _rand(99)
    dates.append(rand_date)
    

    
        
        