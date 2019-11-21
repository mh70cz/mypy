# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 16:56:20 2019 
"""

from bs4 import BeautifulSoup


with open("c:/tmp/task_list.html", encoding="utf-8") as fp:
    soup = BeautifulSoup(fp)
    

rows = soup.find_all("tr", class_="rgRow")
icos = [r.find_all("td")[11].text for r in rows]

rows_alt = soup.find_all("tr", class_="rgAltRow")
icos_alt = [r.find_all("td")[11].text for r in rows_alt]

icos.extend(icos_alt)







"""

list(set(icos_long.split("\n")))


#ctl00_content_grid_ctl00__0 > td:nth-child(12)

//*[@id="ctl00_content_grid_ctl00__0"]/td[12]

#ctl00_content_grid_ctl00__1 > td:nth-child(12)


class="rgAltRow"
"""
