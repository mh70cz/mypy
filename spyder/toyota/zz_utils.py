# -*- coding: utf-8 -*-
"""

"""

#%%


_section = browser.find_element_by_xpath("//div[contains(text(),'Adresa ručitele')]")

section = _section.find_element_by_xpath("..") # typicky zahrnuje celou sekci kde jsou elementy

input_elems = section.find_elements_by_xpath(".//input")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in input_elems]

#%%

_section = browser.find_element_by_xpath("//div[contains(text(),'Bonita ručitele')]")

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
    print(" ".join([e.get_attribute("value")  + " " +  e.text + " ;" for e in options]))

#%%
import xml.etree.ElementTree as ET


root = ET.Element("guarantor_address")

for key in guar_address_values:
    e = ET.SubElement(root, str(key))
    e.text = guar_address_values[key]

tree = ET.ElementTree(root)
ET.dump(root)
#%%
import unicodedata
pangram_cz = "Příliš žluťoučký kůň úpěl ďábelské ódy." # (All the non-ASCII letters of the Czech alphabet )
pangram_sk = "Vypätá dcéra grófa Maxwella s IQ nižším ako kôň núti čeľaď hrýzť hŕbu jabĺk."
pangram_de = "Victor jagt zwölf Boxkämpfer quer über den großen Sylter Deic."
pangram_pl = "Mężny bądź, chroń pułk twój i sześć flag."
pangram_hu = "Jó foxim és don Quijote húszwattos lámpánál ülve egy pár bűvös cipőt készít."

unicodedata.normalize('NFD', pangram_cz).encode('ascii','ignore')
unicodedata.normalize('NFD', pangram_sk).encode('ascii','ignore')
_pangram_de = pangram_de.replace("ß", "ss")
unicodedata.normalize('NFD', _pangram_de).encode('ascii','ignore')
_pangram_pl = pangram_pl.replace("ł","l")
unicodedata.normalize('NFD', _pangram_pl).encode('ascii','ignore')
unicodedata.normalize('NFD', pangram_hu).encode('ascii','ignore')

# unicodedata.normalize('NFKD', string_to_normalize).encode('ascii','ignore')
# unicodedata.normalize('NFD', string_to_normalize).encode('ascii','ignore')
# Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu. (All 42 letters of the Czech alphabet)
#%%


    