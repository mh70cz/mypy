"""
Bite 97. BeautifulSoup II - scrape US bank holidays  

https://codechalleng.es/bites/97
"""

from collections import defaultdict
import os
from urllib.request import urlretrieve

from bs4 import BeautifulSoup


# prep data
holidays_page = os.path.join('/tmp', 'us_holidays.php')
urlretrieve('https://bit.ly/2LG098I', holidays_page)

with open(holidays_page) as f:
    content = f.read()



def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    holidays = defaultdict(list)
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table", attrs={"class":"list-table"})
    tbody = table.find("tbody")
    rows = tbody.find_all("tr")
    
    for row in rows:
        tds = row.find_all("td")
        date = tds[1].find("time").attrs["datetime"]
        month = date[5:7]
        holiday = tds[3].text[1:-1]
        holidays[month].append(holiday)
    return holidays
                
import pytest

holidays = get_us_bank_holidays()


@pytest.mark.parametrize("month, holiday", [
    ('01', ["New Year's Day", 'Martin Luther King Jr. Day ']),
    ('02', ["Presidents' Day"]),
    ('04', ['Emancipation Day']),
    ('05', ["Mother's Day", 'Memorial Day ']),
    ('06', ["Father's Day"]),
    ('07', ['Independence Day ']),
    ('09', ['Labor Day ']),
    ('10', ['Columbus Day ']),
    ('11', ['Veterans Day ', 'Thanksgiving', 'Day after Thanksgiving ']),
    ('12', ['Christmas Day']),
])
def test_get_us_bank_holidays(month, holiday):
    assert holidays.get(month) == holiday
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          