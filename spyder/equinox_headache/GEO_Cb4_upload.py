# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:10:56 2017

@author: mh70
"""

import requests
import xml.etree.ElementTree as ET
import uuid

# suppress InsecureRequestWarning if SSL and no cert + see below verify=False 
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def replace_uuid(docum, string_to_replace):
    """V textu docum nahrad uuid,
    V pripade multiplicity left_string se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    new_docum = docum.replace(string_to_replace, uuid_str)

    return new_docum


def replace_uuid_short(docum, string_to_replace):
    """V textu docum nahrad uuid,
    V pripade multiplicity left_string se bere prvni vyskyt."""
    uuid_str = str(uuid.uuid4()) # make a random UUID
    uuid_str = uuid_str.replace("-", "")
    new_docum = docum.replace(string_to_replace, uuid_str)

    return new_docum

def upload():

    body = """<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><BatchUpload xmlns="http://cb4.creditinfosolutions.com/"><data><Batch xmlns="http://cb4.creditinfosolutions.com/BatchUploader/Batch">           
        <Header>
            <!-- <Identifier>ab2254f3-26fe-4983-8845-47ec73cc9dbf</Identifier> -->
            <Identifier>$ident1</Identifier>
            
            <Subscriber>AdminSubscriber</Subscriber>
            <SubscriberUnit>AdminSubscriberUnit</SubscriberUnit>
        </Header>
        <Commands>
            <Command identifier="$ident2">
                <Cis.CB4.Projects.GE.CIG.Reports.Body.Products.PersonalInformation>
                    <NationalID>01012002417</NationalID>
                </Cis.CB4.Projects.GE.CIG.Reports.Body.Products.PersonalInformation>
            </Command>
        </Commands>
    </Batch></data></BatchUpload></soap:Body></soap:Envelope>
    """
    
    url="https://getest.creditinfosolutions.com/WebService/Service.asmx"
    
    headers = {'Accept-Encoding': 'gzip,deflate',
               'Content-Type': 'text/xml;charset=UTF-8',
               'SOAPAction': '"http://cb4.creditinfosolutions.com/BatchUpload"',
               'Content-Length': str(len(body)),
               'Host': 'getest.creditinfosolutions.com',
               'Connection': 'Keep-Alive',
               'User-Agent': 'Apache-HttpClient/4.1.1 (java 1.5)',
               'Authorization': 'Basic Q0lTX0luZmluaXR5OktvYmxpaGE1NyE=',
               'Accept': None
               }
    
    ns_response = "http://cb4.creditinfosolutions.com/BatchUploader/Batch"
    
    batch_id = "" #BatchId
    
    body_new =  replace_uuid_short(body, "$ident1")
    body_new =  replace_uuid_short(body_new, "$ident2")
    
    
    response = requests.post(url,data=body_new, headers=headers, verify=False)
    
    tree = ET.fromstring(response.text)
    
    x  = tree.find('.//{' + ns_response + '}' + "BatchId")
    batch_id = x.text
    
    return batch_id
