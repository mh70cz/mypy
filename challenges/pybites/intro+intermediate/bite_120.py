"""
Bite 120. Write a numbers validation decorator 

https://codechalleng.es/bites/120
"""

from functools import wraps


def int_args(func):
    @wraps(func)
    def real_dec(*args):        
        for a in args:
            if not isinstance(a, int):
                raise TypeError
            if a < 0:
                raise ValueError
        return func(*args)
    return real_dec            


import pytest


@int_args
def sum_numbers(*numbers):
    return sum(numbers)


def test_valid_args():
    assert sum_numbers(1, 2, 3) == 6


def test_invalid_type_str():
    with pytest.raises(TypeError):
        sum_numbers(1, 'string', 3)


def test_invalid_type_float():
    with pytest.raises(TypeError):
        sum_numbers(1, 2.1, 3)


def test_negative_number():
    with pytest.raises(ValueError):
        sum_numbers(1, 2, -3)
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          