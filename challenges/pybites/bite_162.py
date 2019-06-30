#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 162. Vertically align output of counters
"""

HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length"""
    out_val = str(value)
    return ((column_length - len(out_val)) * fill_char + out_val)