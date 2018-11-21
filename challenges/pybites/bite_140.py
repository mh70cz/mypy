"""
Bite 140. PyBites First Pandas Bite

https://codechalleng.es/bites/140
"""
 
import pandas as pd
import tempfile
import urllib


data = "http://projects.bobbelderbos.com/data/summer.csv"

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    print(type(tmpdirname))
    urllib.request.urlretrieve (data, tmpdirname+"/summer.csv")
    df = pd.read_csv(tmpdirname+"/summer.csv")
# directory and contents have been removed

def athletes_most_medals():
    men = df.where(df["Gender"] == "Men").groupby(["Athlete"])['Medal'].count()
    woman = df.where(df["Gender"] == "Women").groupby(["Athlete"])['Medal'].count()
    men_mm = men[[men.idxmax()]].to_dict()
    woman_mm = woman[[woman.idxmax()]].to_dict()
    return {**men_mm, **woman_mm}
    
def by_pybites_athletes_most_medals():
    df = pd.read_csv(data)
    return df.Athlete.value_counts().head(2)    

import pytest

def test_athletes_most_medals():
    ret = athletes_most_medals()
    larisa = "LATYNINA, Larisa"
    michael = "PHELPS, Michael"

    assert larisa in ret
    assert ret[larisa] == 18

    assert michael in ret
    assert ret[michael] == 22

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    