#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def KaprekarsConstant(num): 
    num = str(num)
    counter = 0
    while  not(num == '6174'):
        num = distract(num)
        counter += 1
    return counter

def distract(num):
    
    num_low = sorted(num)
    num_low = ''.join(num_low)
    num_low = int(num_low)
    
    num_high = sorted(num, reverse = True)
    num_high = ''.join(num_high)
    num_high = int(num_high)
    
    num_out = num_high - num_low
    num_out = str(num_out)
            
    num_out = (4 - len(num_out)) * '0' + num_out
    
    #print(num_out)    
    return num_out
    
