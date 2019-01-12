#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 153. Round a sequence of numbers 
https://codechalleng.es/bites/153
"""

import math


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    if up:
        return list(map(math.ceil, transactions))
    return list(map(math.floor, transactions))