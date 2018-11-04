"""
Bite 119. Xmas tree generator 

https://codechalleng.es/bites/119
"""

def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    tree = []
    for r in range(rows):
        spaces = (rows - r - 1)
        tree.append(spaces * " " +  "*" + 2*r*"*"  + spaces * " ")
    return "\n".join(tree)


import pytest


default_tree = """
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
"""
smaller_tree = """
  *
 ***
*****
"""


def test_height_xmas_tree():
    assert len(generate_xmas_tree().split('\n')) == 10  # default arg
    assert len(generate_xmas_tree(5).split('\n')) == 5
    assert len(generate_xmas_tree(20).split('\n')) == 20


def test_num_stars_used():
    assert generate_xmas_tree(3).count('*') == 9
    assert generate_xmas_tree(5).count('*') == 25
    assert generate_xmas_tree(20).count('*') == 400


def test_outputs():
    actual_tree = generate_xmas_tree().strip('\n').split('\n')
    expected_tree = default_tree.strip('\n').split('\n')
    for i, j in zip(actual_tree, expected_tree):
        assert i.rstrip() == j.rstrip()

    actual_tree = generate_xmas_tree(3).strip('\n').split('\n')
    expected_tree = smaller_tree.strip('\n').split('\n')
    for i, j in zip(actual_tree, expected_tree):
        assert i.rstrip() == j.rstrip()


    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          