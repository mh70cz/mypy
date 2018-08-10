"""
 Bite 70. Create your own iterator 
https://codechalleng.es/bites/70/

Created on  2018-08-10

"""
from random import choice

COLORS = 'red blue green yellow brown purple'.split()


class EggCreator:
    
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    
    def __iter__(self):
        return self
        
    def __next__(self):
        c = choice(COLORS)
        self.counter += 1
        if self.counter <= self.limit:
            return c + " egg"
        else:
            raise StopIteration






import pytest



def test_iterator_type():
    eg = EggCreator(10)
    assert type(eg) == EggCreator


def test_len_iterator_is_limit_input_arg():
    ec = EggCreator(2)
    assert len(list(ec)) == 2
    ec = EggCreator(5)
    assert len(list(ec)) == 5


def test_call_next_on_iterator():
    ec = EggCreator(2)
    next_egg = next(ec)
    assert next_egg.split()[0] in COLORS


def test_iterator_raises_stop_iteration_exception():
    ec = EggCreator(2)
    next(ec)
    next(ec)
    with pytest.raises(StopIteration):
        next(ec)


def test_iterator_generates_random_colors():
    ec = EggCreator(20)
    output1 = list(ec)
    ec = EggCreator(20)
    output2 = list(ec)
    assert output1 != output2
        
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)             