# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Fri Jun 21 19:21:41 2019 
"""

import random


ico_po = ["27880800",  # Mramor Slivenec 
         ]
ico_fop = ["10454055", #  Václav Koča 
          ]

def rnd_ico(typ = "PO"):

    if typ == "PO":
        ico = random.choice(ico_po)
    else:
        ico = random.choice(ico_fop)
    return ico
 

