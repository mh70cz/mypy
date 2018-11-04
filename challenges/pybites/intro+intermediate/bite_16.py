# -*- coding: utf-8 -*-

"""
Bite 16. Special PyBites date generator
"""

from datetime import datetime
from datetime import timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    d = PYBITES_BORN
    yd = timedelta(days=365)
    hd = timedelta(days=100)
    counter = 1
    while True:
        if (d + hd) > PYBITES_BORN + timedelta(days=counter*365):
            yield PYBITES_BORN + yd * counter           
            counter += 1
        else:            
            d += hd
            yield d

g = gen_special_pybites_dates()
for n in range(20):
    print(next(g))


"""

def test_gen_special_pybites_dates():
    gen = gen_special_pybites_dates()
    dates = list(islice(gen, 100))

    expected = [datetime.datetime(2017, 3, 29, 0, 0),
                datetime.datetime(2017, 7, 7, 0, 0),
                datetime.datetime(2017, 10, 15, 0, 0),
                datetime.datetime(2017, 12, 19, 0, 0),
                datetime.datetime(2018, 1, 23, 0, 0),
                datetime.datetime(2018, 5, 3, 0, 0),
                datetime.datetime(2018, 8, 11, 0, 0),
                datetime.datetime(2018, 11, 19, 0, 0),
                datetime.datetime(2018, 12, 19, 0, 0),
                datetime.datetime(2019, 2, 27, 0, 0)]

    assert dates[:10] == expected
    
"""    