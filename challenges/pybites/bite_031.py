"""
Bite 31. Matrix multiplication / @ operator 

https://codechalleng.es/bites/31
"""
 
class Matrix(object):

    def __init__(self, values):
        self.values = values
        #self.l = len(self.values)

    def __repr__(self):
        return f'<Matrix values="{self.values}">'
    
    def _mm(self, other, rows, cols, ks):
        out = []
        for r in range(rows):
            out.append([])
            for c in range(cols):
                x = 0
                out[r].append(0)
                for k in range(ks):
                        x += self.values[r][k] * other.values[k][c]
                out[r][c] = x
        return Matrix(out)
            
    def __matmul__(self, other):
        rows = len(other.values[0]) # rows in output = columns in second input
        cols = len(self.values) # columns in output = rows in the first input
        ks = len(other.values) # columns in first input = rows in second output
        return self._mm(other, rows, cols, ks)
    
    
    def __rmatmul__(self, other):
        rows = len(self.values) # rows in output = rows in the first input
        cols = len(other.values[0]) # cols in output = columns in second input
        ks = len(self.values) # rows in first input = columns in second output
        return self._mm(other, rows, cols, ks)

    
    def __imatmul__ (self, other):
        return self.__matmul__(other)
        
    

import pytest


def test_matmul():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[11, 12], [13, 14]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[37, 40], [85, 92]]


def test_rmatmul():
    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[47, 70], [55, 82]]


def test_imatmul():
    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat1 @= mat2
    assert mat1.values == [[47, 70], [55, 82]]

    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat2 @= mat1
    assert mat2.values == [[37, 40], [85, 92]]


def test_matmul_bigger():
    mat1 = Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[59, 82, 105], [69, 96, 123], [79, 110, 141]]


def test_imatmul_bigger():
    mat1 = Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mat1 @= mat2
    assert mat1.values == [[59, 82, 105], [69, 96, 123], [79, 110, 141]]

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    