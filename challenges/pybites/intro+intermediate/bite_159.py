#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 159. Create a simple calculator 

https://codechalleng.es/bites/159
"""
def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 x 3' -> 6
       '2 + 6' -> 8

       Support +, -, x and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """

    calc_list = [x for x in calculation.strip().split(" ") if x != ""]
    if len(calc_list) != 3:
        raise ValueError
    
    l_operand, operator, r_operand = calc_list
    try:
        l_operand = int(l_operand)
        r_operand = int(r_operand)
    except:
        raise ValueError
    
    

    d = {
        '+': lambda l_operand,r_operand : l_operand + r_operand ,
        '-': lambda l_operand,r_operand : l_operand - r_operand ,
        '*': lambda l_operand,r_operand : l_operand * r_operand ,
        '/': lambda l_operand,r_operand : l_operand / r_operand 
        }

    try:
        result = d[operator](l_operand,r_operand)
    except:
        raise ValueError
        
    return result



