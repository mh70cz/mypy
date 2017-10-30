# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:01:59 2017

@author: mh70
"""


import requests
import xml.etree.ElementTree as ET
import uuid

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def replace_uuid_short(docum, string_to_replace):
    """V textu docum nahrad uuid,
    V pripade multiplicity left_string se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    uuid_str = uuid_str.replace("-", "")
    new_docum = docum.replace(string_to_replace, uuid_str)

    return new_docum

def batch_status(batch_id):
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:cb4="http://cb4.creditinfosolutions.com/">
       <soapenv:Header/>
       <soapenv:Body>
          <cb4:BatchResponseStatus>
             <cb4:id>$batch_id</cb4:id>
          </cb4:BatchResponseStatus>
       </soapenv:Body>
    </soapenv:Envelope>
    """
    
    url="https://getest.creditinfosolutions.com/WebService/Service.asmx"
    
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': '"http://cb4.creditinfosolutions.com/BatchResponseStatus"',
               'Content-Length': str(len(body)),
               'Host': 'getest.creditinfosolutions.com',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
               'Authorization': 'Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE=',
               'Accept': None
               }
    
    ns_response = "http://cb4.creditinfosolutions.com/BatchUploader/Batch"
    
    #batch_id = "" #BatchId
    
    # body_new =  replace_uuid_short(body, "$ident1")
    
    body_new = body.replace("$batch_id", str(batch_id))
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    
    tree = ET.fromstring(response.text)
    
    x  = tree.find('.//{' + ns_response + '}' + "State")
    state = x.text
    
    if not state == "Finished":
        return (state, None)
    
    response_info = tree.find('.//{' + ns_response + '}' + "ResponseInfo")
    ri_id = response_info.find('{' + ns_response + '}' + 'Id').text
    
    return (state, ri_id)
