# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:15:36 2017

@author: mh70
"""

import GEO_Cb4_upload
import GEO_Cb4_status
import GEO_Cb4_result
import GEO_Cb4_parse
import time
import json


class MyBusinessException(Exception):
    pass

national_id = "01012002417"


try:
    batch_id = GEO_Cb4_upload.upload(national_id) # odešli batch a vrať jeho Id 
    
    #zjištuj stav dokud není Finished, 
    #pak vrať ResponseInfo.Id (ri_id) pro vyzvednutí výsledku
    state = ""    
    counter = 1
    while state != "Finished":          
        state, ri_id = GEO_Cb4_status.batch_status(batch_id)
        print("iteration: " + str(counter) + " batch is: " + str(state))
        time.sleep(1) 
        if counter > 30:
            raise MyBusinessException("Batch not finished in a given time limint")
            #break
        counter += 1

    # vyzvedni výsledek
    batch_response_chunk_result = GEO_Cb4_result.batch_result(ri_id)
    
    #dekoduj z Base64 a odzipuj
    xml_txt = GEO_Cb4_parse.unzip_result_xml(batch_response_chunk_result)
    
    #proveď parsing 
    result = GEO_Cb4_parse.parse_result(xml_txt)
    
    result_json = json.dumps(result, ensure_ascii=False)    
    print(result_json)

except MyBusinessException as e:
    print(e)
 
 