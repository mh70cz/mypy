# -*- coding: utf-8 -*-
"""
Bite 208. Find the number pairs summing up N
"""
from itertools import combinations
def find_number_pairs(numbers, N=10):
   combs = combinations(numbers, 2) 
   return [c for c in combs if c[0] + c[1] == N]
   