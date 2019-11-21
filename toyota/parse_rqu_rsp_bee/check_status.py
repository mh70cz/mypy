# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 23:17:52 2019 
"""

from pathlib import Path
import os
from shutil import copyfile
import xml.etree.ElementTree as ET

srcfld = Path("C:/tmp/Cribis_raw")
dstfld = Path("C:/tmp/wrk")


        
        
        
def check_status(path):

    ns = {'urp': 'https://ws.urplus.sk',
          'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03'}
    
    with open(path, encoding="utf-8") as fp:
        tree = ET.parse(fp)
    root = tree.getroot()
    
    
    status_code = ""
    status_elem = root.find(".//urp:Status", ns)
    if status_elem is not None:
        #print(list(status_elem))
        status_code_elem = status_elem.find("urp:Code", ns)
        #print (status_code_elem)
        if status_code_elem is not None:
            # print (status_code_elem)
            status_code = status_code_elem.text
            if status_code == "101":
                return True
    return False

        
            
files = []
for file in os.listdir(srcfld):
    if file.endswith(".xml"):
        print (file)
        path = srcfld / file
        if check_status(path):    
            dstpath = dstfld / file
            copyfile(path, dstpath)
    
      

"""

<CN_Res_Direct xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Responses>
    <Response>
      <InputRequest>CribisGetGlobalReport</InputRequest>
      <Data>
        <CribisGetGlobalReportResponse xmlns="https://ws.urplus.sk">
          <CribisGetGlobalReportResult>
            <Status>
              <Code>101</Code>

"""