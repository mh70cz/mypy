#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Bite 154. Write your own Data Class 

https://codechalleng.es/bites/154


"""

from dataclasses import dataclass

@dataclass 
class Bite:
    number: int
    title: str
    level: str = "Beginner"
    
    def __post_init__(self):
        self.title = self.title.capitalize()
    
    def __lt__(self, other):
        return self.number < other.number
        
    