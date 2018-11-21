"""
Interview Bite: Write a Basic Generator 

https://codechalleng.es/bites/147
"""
 
def my_generator():
    
    yield from ["julian", "is", "awesome"]
    
#    yield("julian")
#    yield("is")
#    yield("awesome")
    

import pytest


import types


def test_is_gerator():
    gg = my_generator()
    assert isinstance(gg, types.GeneratorType)


def test_generator_outputs():
    gg = my_generator()
    assert next(gg) == 'julian'
    assert next(gg) == 'is'
    assert next(gg) == 'awesome'
    with pytest.raises(StopIteration):
        next(gg)  # reached end

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    