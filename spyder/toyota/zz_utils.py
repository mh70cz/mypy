# -*- coding: utf-8 -*-
"""

"""

#%%


_section = browser.find_element_by_xpath("//div[contains(text(),'Adresa ručitele')]")

section = _section.find_element_by_xpath("..") # typicky zahrnuje celou sekci kde jsou elementy

input_elems = section.find_elements_by_xpath(".//input")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in input_elems]

#%%
select_elems = section.find_elements_by_xpath(".//select")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in select_elems]

#%%
_section = browser.find_element_by_xpath("//div[contains(text(),'Zaměstnání ručitele')]")

section = _section.find_element_by_xpath("..") # typicky zahrnuje celou sekci kde jsou elementy

input_elems = section.find_elements_by_xpath(".//input")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in input_elems]

#%%

select_elems = section.find_elements_by_xpath(".//select")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in select_elems]



#%%
le = 70
ws = 20
we = 65

n = 48

wp = ((n-ws) / (we - ws)) * 100
lp = n/le * 100

#%%

for se in select_elems:
    options = se.find_elements_by_xpath(".//option")
    print(" ".join([e.text + " " +  e.get_attribute("value") + " ;" for e in options]))

#%%
    