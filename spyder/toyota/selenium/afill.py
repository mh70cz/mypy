# -*- coding: utf-8 -*-
"""

"""
import start
import task_1
import task_2
import task_3_spo
import task_3_fop
import task_3_po
import task_3_guar_fo


""""
browser, web_app = task_1.open_browser()
task_1.login(browser)


browser, web_app = start.init("cz_test_CI ", kr=False)

# browser, web_app = start.init("cz_test", kr=True) 
# browser, web_app = start.init("cz_test_CI ", kr=False)
# 


#SPO   #####
task_1.fillscreen(browser, web_app, subj_type = "SPO", prod_type = "FO")
task_1.fillscreen(browser, web_app, subj_type = "SPO", prod_type = "FC")

task_2.fill_spo(browser)

task_3_spo.fill(browser)


#FOP  #########
task_1.fillscreen(browser, web_app, subj_type = "FOP", prod_type = "FO")
task_1.fillscreen(browser, web_app, subj_type = "FOP", prod_type = "FC")

gender, pin = task_2.fill_fop(browser)  

task_3_fop.fill(browser, data=None, gender=gender, pin=pin)

#PO  #####
task_1.fillscreen(browser, web_app, subj_type = "PO", prod_type = "FO")
task_1.fillscreen(browser, web_app, subj_type = "PO", prod_type = "FC")

task_2.fill_po(browser)      # fill_po(browser, full_statements = False)

task_3_po.fill(browser)

##########

task_2.init(browser, web_app, task_id)



task_3_guar_fo.fill(browser)


web_task_edit = "Processing/TaskEdit.aspx?id="
task_id = "47166"     #  47018 46889  46891  46889
browser.get(web_app + web_task_edit + task_id)



"""