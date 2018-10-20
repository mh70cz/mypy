"""
Bite 99. Write an infinite sequence generator 

https://codechalleng.es/bites/99
"""
from itertools import cycle


def sequence_generator():
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    z = zip(range(1, len(s)+1), s)
    c = cycle(z)
    while True:
        t = next(c)
        yield t[0] 
        yield t[1]
                
import pytest
from itertools import islice


@pytest.fixture
def gen():
    """Return a fresh new generator object for each test"""
    return sequence_generator()


def test_first_ten_first_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    # generators == use islice, a regular slicing on a list object == hang
    # because it tries to load in an infinite iterator = not good.
    # don't believe me? change the line below to: `actual = list(gen)[:10]`
    actual = list(islice(gen, 10))
    assert expected == actual


def test_first_ten_second_round(gen):
    expected = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E']
    actual = list(islice(gen, 52, 62))  # zero-based
    assert expected == actual


def test_last_ten_third_round(gen):
    expected = [22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z']
    actual = list(islice(gen, 146, 156))
    assert expected == actual
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          