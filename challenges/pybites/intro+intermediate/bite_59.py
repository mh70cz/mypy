"""
Bite 59. Create a multiplication table class of variable length
https://codechalleng.es/bites/59/
Created on 2018-08-07


"""

class MultiplicationTable:

    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""
        self.length = length
        self.lst = []
        for x in range(length):
            for y in range(length):
                t = ((x+1, y+1), (x+1)*(y+1))
                self.lst.append(t)


    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self.lst)
        

    def __str__(self):
        """Returns a string representation of the table"""
        s = ""
        for x in range(self.length):
            line = []
            #print (f"x: {x}")
            for y in range(self.length):
                #print (f"y: {y}")
                line.append(str(self.lst[x*self.length +y][1])) 
                #print (line)
            s += " | ".join(line) + "\n"
        return (s)

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        if x < 1 or x > self.length or y < 1 or y > self.length:
            raise IndexError
        n = (x - 1) * self.length + y - 1
        return self.lst[n][1]
    
    
import pytest


@pytest.fixture
def t10():
    return MultiplicationTable(10)


@pytest.fixture
def t3():
    return MultiplicationTable(3)


@pytest.mark.parametrize("arg, ret", [
    (1, 1),
    (5, 25),
    (10, 100),
    (100, 10000),

])
def test_table_len(arg, ret):
    assert len(MultiplicationTable(arg)) == ret


@pytest.mark.parametrize("arg, ret", [
    ((6, 6), 36),
    ((4, 2), 8),
    ((7, 6), 42),
    ((8, 8), 64),
    ((10, 10), 100),
])
def test_calc(t10, arg, ret):
    t10.calc_cell(*arg) == ret


def test_calc_exception(t3, capfd):
    with pytest.raises(IndexError):
        t3.calc_cell(3, 4)
    with pytest.raises(IndexError):
        t3.calc_cell(4, 3)


def test_table_str(t3):
    output = str(t3)
    assert '1 | 2 | 3' in output
    assert '2 | 4 | 6' in output
    assert '3 | 6 | 9' in output    
    
#import sys
#if __name__ == '__main__':
#    pytest.main(sys.argv)       