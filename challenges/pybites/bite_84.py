"""
Bite 84. Flatten lists recursively (Droste Bite) 
https://codechalleng.es/bites/84
"""

def flatten(list_of_lists):
    flat = []
    
    def inner_f(lst):
        for e in lst:
            print (e)
            if isinstance(e, (list, tuple)):
                inner_f(e)
            else:
                flat.append(e)
    inner_f(list_of_lists)
    return flat
    
    
    
import pytest

def test_flatten_various_levels():
    inp = [1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(flatten(inp)) == expected


def test_flatten_various_levels_different_contant():
    inp = [1, 2, [3, 4], [5, [6, 7]], [8, [9, [10]]],
           [11, [12, 13], [14, [15, 16, [17, 18, [19, 20]]]]]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18, 19, 20]
    assert list(flatten(inp)) == expected


def test_flatten_ints_and_chars():
    inp = ['a', 'b', [1, 2, 3],
           ['c', 'd', ['e', 'f', ['g', 'h']]],
           [4, [5, 6, [7, [8]]]]]
    expected = ['a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g',
                'h', 4, 5, 6, 7, 8]
    assert list(flatten(inp)) == expected


def test_works_with_tuple_as_well():
    inp = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(flatten(inp)) == expected
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          