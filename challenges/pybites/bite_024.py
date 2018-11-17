"""
Bite 24. ABC's and class inheritance 

https://codechalleng.es/bites/24
"""
 
from abc import ABC, abstractmethod


class Challenge(ABC):
    
    
    def __init__(self, idx, title):
        self.idx = idx
        self.title = title

    
    @abstractmethod
    def verify(self):
        pass
        
    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):
    def __init__(self, idx, title, merged_prs):
        super().__init__(idx, title)
        self.merged_prs = merged_prs
        
    def verify(self, idx):
        return idx in self.merged_prs
    
    @property
    def pretty_title(self):
        return "PCC" + str(self.idx) + " - " + self.title


class BiteChallenge(Challenge):
    
    def __init__(self, idx, title, result):
        super().__init__(idx, title)
        self.result = result
    
    def verify(self, result):
        return self.result == result
    
    @property
    def pretty_title(self):
        return "Bite " + str(self.idx) + ". " + self.title
    

import pytest

def test_should_not_instantiate_abc():
    with pytest.raises(TypeError):
        ch = Challenge(0, 'Should not instantiate ABC')
        ch.number


def test_super_and_abst_method_implementation():
    try:
        blog = BlogChallenge(1, 'Wordvalues', [41, 42, 44])
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert blog.verify(41)
    assert not blog.verify(43)
    assert blog.pretty_title == 'PCC1 - Wordvalues'


def test_super_and_abst_property_implementation():
    try:
        bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')
    except TypeError:
        pytest.fail("Unexpected TypeError, missing methods/properties?")

    assert bite.verify('my result')
    assert not bite.verify('other result')
    assert bite.pretty_title == 'Bite 24. ABC and class inheritance'

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    