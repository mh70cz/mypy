#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 155. Split a string by spaces or quoted text 

https://codechalleng.es/bites/155
"""
def split_words_and_quoted_text(text):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    words = []
    word = ""
    toggle_dquotes = False
    for c in text:
        if c == '"':
            toggle_dquotes = not(toggle_dquotes)
            continue
        
        if c == " " and not toggle_dquotes:
            words.append(word) 
            word = ""
            continue
        word += c
    words.append(word)
    return words
        
    
