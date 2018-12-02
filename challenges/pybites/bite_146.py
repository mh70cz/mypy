"""
Bite 146. Rhombus generator 

https://codechalleng.es/bites/146
"""
 
STAR = '*'

def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    sp = width // 2
    st = 0
    for r in range(width):
        yield (sp * " " + (2*st + 1) * STAR + sp * " ")
        if r < (width//2):
            sp -= 1
            st += 1
        else:
            sp += 1
            st -= 1
            
        
        
    
        
        
    

import pytest



def test_rhombus_width3():
    # recommended: actual before expected
    # https://twitter.com/brianokken/status/1063337328553295876
    actual = list(gen_rhombus(3))
    expected = [' * ', '***', ' * ']
    assert actual == expected


def test_rhombus_width5():
    actual = list(gen_rhombus(5))
    expected = ['  *  ', ' *** ', '*****',
                ' *** ', '  *  ']
    assert actual == expected


def test_rhombus_width11():
    """print('\n'.join(expected)) would give (ignore indents):
         *
        ***
       *****
      *******
     *********
    ***********
     *********
      *******
       *****
        ***
         *
    """
    actual = list(gen_rhombus(11))
    expected = ['     *     ', '    ***    ', '   *****   ',
                '  *******  ', ' ********* ', '***********', ' ********* ',
                '  *******  ', '   *****   ', '    ***    ', '     *     ']
    assert actual == expected
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    