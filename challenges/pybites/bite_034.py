"""
 Bite 34. Building a Karma app - implement the User class 

https://codechalleng.es/bites/31
"""
 
from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL


class User:
    def __init__(self, name):
        self.name = name
        self._fans = set()
        self._points = list()
        self._transactions = list()
    
    def __add__(self, transaction):
        self._fans.add(transaction.giver)
        self._points.append(transaction.points)
        
    
    
    def __str__(self):
        return f"{self.name} has a karma of {self.karma} and {self.fans} fans"
    
   
    @property
    def fans(self):
        return len(self._fans)
    
    @property
    def points(self):
        return self._points
    
    @property
    def karma(self):
        return sum(self._points)
    

import pytest




alice = User('alice')
bob = User('bob')
tim = User('tim')

transactions = [
    Transaction(giver=alice, points=1),
    Transaction(giver=bob, points=2),
    Transaction(giver=tim, points=3),
    Transaction(giver=tim, points=4),
]


def test_init():
    assert alice.name == 'alice'
    assert bob.name == 'bob'
    assert alice._transactions == []
    assert bob._transactions == []


def test_adding_karma():
    bob + transactions[0]
    assert bob.karma == 1
    alice + transactions[1]
    assert alice.karma == 2
    bob + transactions[2]
    assert bob.karma == 4
    alice + transactions[3]
    assert alice.karma == 6


def test_upvotes_property():
    assert bob.points == [1, 3]
    assert alice.points == [2, 4]


def test_fans_property():
    assert tim.fans == 0
    assert bob.fans == 2
    assert alice.fans == 2


def test_str_dunder():
    assert str(tim) == 'tim has a karma of 0 and 0 fans'
    assert str(alice) == 'alice has a karma of 6 and 2 fans'
    assert str(bob) == 'bob has a karma of 4 and 2 fans'

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    