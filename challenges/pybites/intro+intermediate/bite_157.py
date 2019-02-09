#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 157. Filter out accented characters 

https://codechalleng.es/bites/157
"""
def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in text string
    """
    #return  set([x.lower() for x in text if ord(x) > 122])
    return set([x.lower() for x in text if not x.isascii()]) # python 3.7
    
#solution from pybites    
import unicodedata    
    # decomposition return base char + added symbol or ''
    # you could also use unicodedata.normalize
    return {c for c in text.lower() if
            unicodedata.decomposition(c)}