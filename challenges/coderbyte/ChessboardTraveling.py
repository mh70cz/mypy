#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
https://coderbyte.com/editor/Chessboard%20Traveling:Python

Using the Python language, have the function ChessboardTraveling(str) 
read str which will be a string consisting of the location of 
a space on a standard 8x8 chess board with no pieces on the board 
along with another space on the chess board. The structure of 
str will be the following: "(x y)(a b)" where (x y) represents 
the position you are currently on with x and y ranging from 1 
to 8 and (a b) represents some other space on the chess board 
with a and b also ranging from 1 to 8 where a > x and b > y. 
Your program should determine how many ways there are of traveling 
from (x y) on the board to (a b) moving only up and to the right.
 For example: if str is (1 1)(2 2) then your program should output 
2 because there are only two possible ways to travel from space 
(1 1) on a chessboard to space (2 2) while making only moves 
up and to the right.  
"""

'''
Input:"(1 1)(3 3)"

Output:6


Input:"(2 2)(4 3)"

Output:3
'''


def ChessboardTraveling(pos): 

    x,y,a,b = Parse(pos)
    #print(x,y,a,b)
    hor_shift = a - x
    ver_shift = b - y
    return Permutations_of_multiset(hor_shift, ver_shift)
    

def Parse(pos):
    x = int(pos[1])
    y = int(pos[3])
    a = int(pos[6])
    b = int(pos[8])
    return (x,y,a,b)

def Permutations_of_multiset(hor_shift, ver_shift):
    size_of_multiset = hor_shift + ver_shift
    num_of_perm = fact(size_of_multiset) / (fact(hor_shift) * fact(ver_shift))
    return int(num_of_perm)
 
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

def Break_text(txt):
    out = ""
    counter = 0
    for c in txt:
        out += c
        counter += 1
        if counter > 60 and (c in [' ', '\n', ',', '.']):
            out += '\n'
            counter = 0
    return out