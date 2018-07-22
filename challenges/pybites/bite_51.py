#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 51. When does Python 2 die on Planet Miller? 
https://codechalleng.es/bites/51/
Created on Sat Jul 21 20:24:02 2018
Python 2.7 will indeed retire on April 12th of 2020
@author: mh70
"""

from datetime import datetime

BITE_CREATED_DT = datetime.strptime('2018-02-26 23:24:04', '%Y-%m-%d %H:%M:%S')


def py2_earth_hours_left():
    """Return how many hours, rounded to 2 decimals, Python 2 has
       left on Planet Earth"""
    td =  datetime(2020, 4, 12) - BITE_CREATED_DT
    return round(td.days*24 + td.seconds/(60*60), 2)


def py2_miller_min_left():
    """Return how many minutes, rounded to 2 decimals, Python 2 has
       left on Planet Miller"""
    H_7EY = 7*365*24       
    return round(py2_earth_hours_left() / H_7EY * 60, 2)

def test_py2_earth_hours_left():
    assert py2_earth_hours_left() == 18600.6


def test_py2_miller_min_left():
    assert py2_miller_min_left() == 18.2