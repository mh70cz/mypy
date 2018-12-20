#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:37:01 2018

@author: mh70
"""

from bs4 import BeautifulSoup
import requests
import re

VERDI_URL = "https://en.wikipedia.org/wiki/List_of_compositions_by_Giuseppe_Verdi"
HAYDN_URL = "https://en.wikipedia.org/wiki/List_of_operas_by_Joseph_Haydn"
MOZART_URL = "https://en.wikipedia.org/wiki/List_of_operas_by_Wolfgang_Amadeus_Mozart"

html_doc = requests.get(VERDI_URL).text
soup = BeautifulSoup(html_doc, 'html.parser')

table = soup.body.table
rows = table.tbody.find_all("tr")


reg_date = re.compile(r"\d{1,2} (January|February|March|April|May|June|July|August|September|October|November|December) \d{4}")



operas_verdi = []
for r in rows[1:]:
    line = r.find_all("td")
    line_id = line[0].text.strip()
    title = line[1].text.strip()
    first_p_raw = line[4].text
    if reg_date.search(first_p_raw):
        first_p = reg_date.search(first_p_raw)[0]
    else:
        first_p = first_p_raw.strip()
    
    operas_verdi.append((title, first_p))

