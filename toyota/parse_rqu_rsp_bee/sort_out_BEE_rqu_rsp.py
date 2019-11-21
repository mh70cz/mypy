# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Thu Nov 21 16:53:22 2019 
"""

from pathlib import Path
import os
from shutil import copyfile

srcfld = Path("C:/tmp/rqu_rsp_BEE_Live")
dstfld = Path("C:/tmp/rqu_BEE_Live")

for file in os.listdir(srcfld):
    if file.endswith(".xml"):
        if "_IN_" in file:
            print (file)
            path = srcfld / file
            dstpath = dstfld / file
            copyfile(path, dstpath)