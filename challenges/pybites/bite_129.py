"""
Bite 129. Analyze Stock Data 

https://codechalleng.es/bites/129
"""
import requests
from collections import Counter

STOCK_DATA = 'https://bit.ly/2MzKAQg'

# pre-work: load JSON data into program
#
with requests.Session() as s:
    data = s.get(STOCK_DATA).json()


# your turn:

def _cap_str_to_mln_float(cap):
    """If cap = 'n/a' return 0, else:
       - strip off leading '$',
       - if 'M' in cap value, strip it off and return value as float,
       - if 'B', strip it off and multiple by 1,000 and return
         value as float"""
    if cap == "n/a":
        return 0
    cap = cap.lstrip("$")
    if cap[-1] == "B":
        return float(cap[:-1]) * 1000
    if cap[-1] == "M":
        return float(cap[:-1])
      


def get_industry_cap(industry):
    """Return the sum of all cap values for given industry, use
       the _cap_str_to_mln_float to parse the cap values,
       return a float with 2 digit precision"""
    #round(sum([_cap_str_to_mln_float(d["cap"]) for d in data if d["industry"] == "Business Services"]),2)
    ind_sum = 0
    for d in data:
        if industry == d["industry"]:
            ind_sum += _cap_str_to_mln_float(d["cap"])
    return round(ind_sum, 2)


def get_stock_symbol_with_highest_cap():
    """Return the stock symbol (e.g. PACD) with the highest cap, use
       the _cap_str_to_mln_float to parse the cap values"""
    m_cap, m_symbol = 0, None
    for d in data:
        c = _cap_str_to_mln_float(d["cap"]) 
        if c >= m_cap:
            m_cap, m_symbol = c, d["symbol"] 
    return m_symbol


def get_sectors_with_max_and_min_stocks():
    """Return a tuple of the sectors with most and least stocks,
       discard n/a"""
    cnt = Counter()
    for d in data:
        if d["sector"] == "n/a":
            continue
        cnt[d["sector"]] += 1
    return (cnt.most_common()[0][0], cnt.most_common()[-1][0])
        
        
    
        
                
import pytest


def test_cap_str_to_mln_float():
    assert _cap_str_to_mln_float('n/a') == 0
    assert _cap_str_to_mln_float('$100.45M') == 100.45
    assert _cap_str_to_mln_float('$20.9B') == 20900


def test_get_stock_symbol_with_highest_cap():
    assert get_stock_symbol_with_highest_cap() == 'JNJ'


def test_get_industry_cap():
    assert get_industry_cap("Business Services") == 368853.27
    assert get_industry_cap("Real Estate Investment Trusts") == 243295.36


def test_get_sectors_with_max_and_min_stocks():
    assert get_sectors_with_max_and_min_stocks() == ('Finance',
                                                     'Transportation')

    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          