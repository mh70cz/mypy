#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 23:02:08 2017

@author: mh70
"""

def my_decor(wrapped_func, num=15):
    def wrapper(text_to_print):
        if num <= 10:
            print(str(num) + " is less or equal than 10")
        else:
            print(str(num) + " is greater than 10")
        wrapped_func(text_to_print)
        print("after wrapped function is called")
    return wrapper

@my_decor
def test_func(text_to_print):
    print(text_to_print)
    
test_func("with @my_decor syntax sugar")   
#my_decor(test_func)("without wrapper syntax sugar")

    
#### http://scottlobdell.me/2015/04/decorators-arguments-python/
    
def pass_thru(func_to_decorate):
    def new_func(*original_args, **original_kwargs):
        print("function has been deforated")
        # do something here
        return func_to_decorate(*original_args, **original_kwargs)
    return new_func

@pass_thru
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)
        
        
def print_args_without_decor_sytax_sugar(*args):
    for arg in args:
        print(arg)

pass_thru(print_args_without_decor_sytax_sugar)("alpha", "beta", "gamma")