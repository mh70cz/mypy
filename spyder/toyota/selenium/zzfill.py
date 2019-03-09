# -*- coding: utf-8 -*-
"""

"""
import start
import zz_task_1
import zz_task_2


browser, web_app = start.init("cz_test", kr=True) 

# browser, web_app = start.init("cz_test", kr=True) 
# browser, web_app = start.init("cz_test_CI ", kr=False)
# 



""""

#SPO   #####
zz_task_1.fillscreen(browser, web_app, subj_type = "SPO", prod_type = "FO")
zz_task_1.fillscreen(browser, web_app, subj_type = "SPO", prod_type = "FC")

zz_task_2.fill_spo(browser)



#FOP  #########
zz_task_1.fillscreen(browser, web_app, subj_type = "FOP", prod_type = "FO")
zz_task_1.fillscreen(browser, web_app, subj_type = "FOP", prod_type = "FC")

zz_task_2.fill_fop(browser)  


#PO  #####
zz_task_1.fillscreen(browser, web_app, subj_type = "PO", prod_type = "FO")
zz_task_1.fillscreen(browser, web_app, subj_type = "PO", prod_type = "FC")

zz_task_2.fill_po(browser)      



##########

zz_task_2.init(browser, web_app, task_id)

web_task_edit = "Processing/TaskEdit.aspx?id="
task_id = "47166"     #  47018 46889  46891  46889
browser.get(web_app + web_task_edit + task_id)


browser, web_app = zz_task_1.open_browser()
zz_task_1.login(browser)


browser, web_app = 


"""