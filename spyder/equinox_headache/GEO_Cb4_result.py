# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:53:57 2017

@author: mh70
"""

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

def batch_result(ri_id):
    
    body = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <soap:Body>
            <BatchResponseChunk xmlns="http://cb4.creditinfosolutions.com/">
                <id>$ri_id</id>
                <partNumber>1</partNumber>
            </BatchResponseChunk>
        </soap:Body>
    </soap:Envelope>
    """
    
    url="https://getest.creditinfosolutions.com/WebService/Service.asmx"
    
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': '"http://cb4.creditinfosolutions.com/BatchResponseChunk"',
               'Content-Length': str(len(body)),
               'Host': 'getest.creditinfosolutions.com',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
               'Authorization': 'Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE=',
               'Accept': None
               }
    
    ns_response = "http://cb4.creditinfosolutions.com/"
    
    #batch_id = "" #BatchId
    
    # body_new =  replace_uuid_short(body, "$ident1")
    
    body_new = body.replace("$ri_id", str(ri_id))
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    
    tree = ET.fromstring(response.text)
    
    x  = tree.find('.//{' + ns_response + '}' + "BatchResponseChunkResult")
    batch_response_chunk_result = x.text
    

    
    return (batch_response_chunk_result)
