# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 08:53:48 2018

@author: mh70
"""

from enum import Enum

class Q(Enum):
    A = 1

print("class Q in global scope")    
print(id(Q))  
print(Q.A.value)  


def xxx():
    class Q(Enum):
        A = 2

    print("class Q in local scope")
    print(id(Q))  
    print(Q.A.value)
xxx()    

print("class Q in global scope again")    
print(id(Q))  
print(Q.A.value)


del Q
class Q(Enum):
    A = 3

print("class Q in global scope - deleted and redefined")    
print(id(Q))  
print(Q.A.value) 
    