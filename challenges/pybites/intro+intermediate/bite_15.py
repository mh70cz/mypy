#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 21:59:38 2018;@author: mh70
Bite 15. Enumerate 2 sequences
"""

names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico
       
       """
    for i, q in enumerate(list(zip(names, countries))):
        print(f"{i+1}. {q[0]:<10s} {q[1]}")


"""
def test_pythonic_idioms():
    with open(SCRIPT) as f:
        content = f.read()

    assert "for" in content, "Need a for loop"
    assert "enumerate" in content, "Best to use enumerate here"
    assert "zip" in content, "Best to use zip here"
    
other (not listed here) tests apply    
"""    