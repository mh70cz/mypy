# -*- coding: utf-8 -*-
"""

"""

#%%


_section = browser.find_element_by_xpath("//div[contains(text(),'Adresa ručitele')]")

section = _section.find_element_by_xpath("..") # typicky zahrnuje celou sekci kde jsou elementy

input_elems = section.find_elements_by_xpath(".//input")

[(e.get_attribute("id") , e.get_attribute("name") , e.get_attribute("data-bind") ) for e in input_elems]

#%%

_section = browser.find_element_by_xpath("//div[contains(text(),'Bonita žadatele ')]")

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
#%%
_section = browser.find_element_by_xpath("//div[contains(text(),'Firma')]")

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
import xml.etree.ElementTree as ET

root = ET.fromstring(data["applicant"])
ET.dump(root)
#%%


process_id_elem = browser.find_element_by_xpath("//td[@data-bind='text: ProcessId']")
process_id  = process_id_elem .text
#%%
import requests
from bs4 import BeautifulSoup

url = web_app + "Processing/processData.aspx?id=" + process_id
usr = r"cis\m.houska"
pwd = "heslo"
auth_data =  {'txtUsername':usr,'txtPassword':pwd}
cookies =  {'domain': 'cishd-cls-app01',
  'expiry': "1551704099.043258",
  'httpOnly': "true",
  'name': 'cisLogin',
  'path': '/',
  'secure': "false",
  'value': 'A40D854BC3AA02D9021DD74B08855F228B61F123CD3222AC1EACF25F2BE55BFF1B0B7E499B7B8597D11AF4FF7D86A8125D420CA1B486F6BE32D5F02E5C295878498E0C090975995C8BC5861AAF097FB81D6A179E151FD36A385FA50C0E3829F9D0EF1188C6CE05E0C908656FD02975C613594D0460FFC26D664273946D81598203D47EBB5DF4A824615688C5C648F4A7C58611494E1DDD6C3B6ACC83841A95FEB42E7FF85C2DF0102731EF7D67B433AACE407D7FD3635695DF5AD08FC26FA14977D6ACB19A5A4EA16A6F1E3AE974B7144A71DBBEBABF9B8F42205E7319F0782D'}

headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36"}

session = requests.Session()
#r = session.post(url, headers=headers,  data=auth_data)   
r = session.post(url, headers=headers,  cookies=cookies )   

soup = BeautifulSoup(r.content)

soup
#%%
from selenium.webdriver.common.keys import Keys
_body = browser.find_element_by_css_selector('body')
_body.send_keys(Keys.PAGE_DOWN)

#%%
_prilohy_lst = browser.find_elements_by_xpath("//div[contains(text(), 'Přílohy')]")
if len(_prilohy_lst) > 0:
    _prilohy_lst[0].click()
#%%
#c:\temp\wolf.jpg
label_ns = browser.find_element_by_xpath("//label[contains(text(), 'Nahrát Soubor')]")
op_btn = label_ns.find_element_by_xpath("../input")
op_btn.send_keys(r"c:\temp\wolf.jpg")
vlozit_btn = label_ns.find_element_by_xpath("../span/input")
vlozit_btn.click()

#%%
label_ns_lst = browser.find_elements_by_xpath("//label[contains(text(), 'Nahrát Soubor')]")
_first_time = True
for label in label_ns_lst:
    op_btn = label.find_element_by_xpath("../input")
    op_btn.send_keys(r"c:\temp\wolf_small.jpg")
    vlozit_btn = label.find_element_by_xpath("../span/input")
    vlozit_btn.click()
    if _first_time:
        sleep(0.5)
        _first_time = False
    sleep(0.5)    

Coapp_AttachmentNote = browser.find_element_by_id("__Coapp_AttachmentNote")
Coapp_AttachmentNote.send_keys("uživatelská poznámka")
#%%
browser.execute_script("alert('qwer');")
sleep(1)
browser.switch_to.alert.accept()
