#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 158. Subclass the list built-in 

https://codechalleng.es/bites/158
"""
from decimal import Decimal
class IntList(list):
    
    
    def append(self, items):
        if isinstance(items, (int, float)):
            super().append(items)
        elif isinstance(items, Decimal):
            super().append(float(items))
        elif isinstance(items, list):
            for i in items:
                if not isinstance(i, (int, float, Decimal)):
                    raise TypeError
                if isinstance(i, Decimal):
                    i = float(i)
                super().append(i)
        else:
            raise TypeError

    def __add__(self, other):
        if not isinstance(other, list):
            raise TypeError
        self._extend_add(other)
        return self
    
    def __iadd__(self, other):
        if not isinstance(other, list):
            raise TypeError
        self._extend_add(other)
        return self
    
    def _extend_add(self, other):
        for i in other:
            if not isinstance(i, (int, float, Decimal)):
                raise TypeError
            if isinstance(i, Decimal):
                i = float(i)            
            super().append(i)        
            
            
    """
    from pybites:
        def _check_int(self, num):
            try:
                if type(num) == list:
                    return [int(i) for i in num]
                return int(num)
            except(ValueError, TypeError):
                raise TypeError
    
        def append(self, num):
            num = self._check_int(num)
            super().append(num)
    
        def __add__(self, num):
            num = self._check_int(num)
            return super().__add__(num)
    
        def __iadd__(self, num):
            num = self._check_int(num)
            return super().__iadd__(num)
    
    """            
                        
    @property
    def mean(self):
        return sum(self)/ (max(len(self),1))
    
    @property
    def median(self):
        s = sorted(self)
        if len(s) % 2 == 0:
            return (s[len(s)//2 - 1] + s[len(s)//2])/2 # // -> int ; / -> float
        else:
            return s[len(s)//2]
        
    
l = IntList([1, 3, 5, 7])   
print(l)
l += [1, 2, 3]
print(l)
