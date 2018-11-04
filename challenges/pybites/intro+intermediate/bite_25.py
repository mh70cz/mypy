#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mh70; 2018-07-11; Bite 25. https://codechalleng.es/bites/25/

classes, exception handling, properties, by value vs by reference
"""

"""
slack: mh70 [9:34 PM]
Hi,
I have a question related to the Bite 25. https://codechalleng.es/bites/25/ :
The proposed solution passes tests OK. Nevertheless, it does not fulfill the initial requirement "update *both* self.bites and self.bites_done".
Furthermore, it modifies the constant BITES_DONE = {6, 10, 16, 18, 21}.
Are my assumptions correct?
"""

import random

BITES = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
BITES_DONE = {6, 10, 16, 18, 21}


class NoBitesAvailable(Exception):
    pass


class Promo_mh70:
    def __init__(self, bites=BITES, bites_done=BITES_DONE):
        self.bites = dict(bites)
        self.bites_done = set(bites_done)

        assert self.bites is not BITES
        assert self.bites_done is not BITES_DONE

    def _pick_random_bite(self):
        available = set(self.bites.keys()).difference(self.bites_done)

        try:
            k = random.choice(list(available))
        except IndexError:
            raise NoBitesAvailable
        return k

    def new_bite(self):
        k = self._pick_random_bite()
        self.bites_done.add(k)
        bite = self.bites.pop(k)
        return bite


class Promo:
    def __init__(self, bites=BITES, bites_done=BITES_DONE):
        self.bites = bites
        self.bites_done = bites_done
        # assert self.bites is not BITES
        # assert self.bites_done is not BITES_DONE

    @property
    def available_bites(self):
        return list(self.bites.keys() - self.bites_done)

    def _pick_random_bite(self):
        if not self.available_bites:
            raise NoBitesAvailable
        return random.choice(self.available_bites)

    def new_bite(self):
        bite = self._pick_random_bite()
        self.bites_done.add(bite)
        return bite


p = Promo()
p_mh = Promo_mh70()


print("\n", BITES_DONE)
for b in range(8):
    print(p._pick_random_bite())
    print(p.new_bite())

print("\n", BITES_DONE)

