#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 152. Manipulate string decorator 

https://codechalleng.es/bites/152
"""
from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def real_decorator(wrapped_f):
        def wrapper(*args, **kwargs):
            f_out = wrapped_f(*args, **kwargs)
            out = ""
            for idx, c in enumerate(f_out):
                if start <= idx < end:
                    out += DOT
                else:
                    out += c
            return out
        return wrapper
    return real_decorator

@strip_range(3, 5)    
def gen_dt():
    return DEFAULT_TEXT
    
gen_dt()                        
            
    
