# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:15:36 2017

@author: mh70
"""

import GEO_Cb4_upload
import GEO_Cb4_status
import GEO_Cb4_result
import time


class MyBusinessException(Exception):
    pass

try:
    batch_id = GEO_Cb4_upload.upload()
    state, ri_id = GEO_Cb4_status.batch_status(batch_id)
    
    
    counter = 1
    while state != "Finished":
        print("iteration: " + str(counter) + " batch is: " + str(state))
        time.sleep(0.1) 
        state, ri_id = GEO_Cb4_status.batch_status(batch_id)
        if counter > 30:
            raise MyBusinessException("Batch not finished in a given time limint")
            #break
        counter += 1
    print("iteration: " + str(counter) + " batch is: " + str(state))
    
    batch_response_chunk_result = GEO_Cb4_result.batch_result(ri_id)

except(MyBusinessException) as e:
    print(e)
except(Exception):
    pass    