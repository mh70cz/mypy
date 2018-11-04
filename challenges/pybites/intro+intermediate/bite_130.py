"""
Bite 130. Analyze some basic Car Data  

https://codechalleng.es/bites/130
"""

from collections import Counter
import json

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

# pre-work: load JSON data into program

with requests.Session() as s:
    download = s.get(CAR_DATA)
    data = json.loads(download.content.decode('utf-8'))


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    c = Counter()
    for record in data:
        if record["year"] == year:
            c[record["automaker"]] += 1
    return c.most_common(1)[0][0]
    
    
import pytest

def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = set()
    for record in data:
        if record["automaker"] == automaker and record["year"] == year:
            models.add(record["model"])
    return models
    


def test_most_prolific_automaker_1999():
    assert most_prolific_automaker(1999) == 'Dodge'


def test_most_prolific_automaker_2008():
    assert most_prolific_automaker(2008) == 'Toyota'


def test_most_prolific_automaker_2013():
    assert most_prolific_automaker(2013) == 'Hyundai'


def test_get_models_volkswagen():
    models = get_models('Volkswagen', 2008)
    # sets are unordered
    assert len(models) == 2
    assert 'Jetta' in models
    assert 'Rabbit' in models


def test_get_models_nissan():
    assert get_models('Nissan', 2000) == {'Pathfinder'}


def test_get_models_open():
    # not in data set
    assert get_models('Opel', 2008) == set()


def test_get_models_mercedes():
    models = get_models('Mercedes-Benz', 2007)
    assert len(models) == 3
    assert 'SL-Class' in models
    assert 'GL-Class' in models
    assert 'CL-Class' in models
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          