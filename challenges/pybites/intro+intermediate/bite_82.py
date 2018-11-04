"""
Bite 82. Define a Score Enum and customize it adding methods

https://codechalleng.es/bites/82
"""

from enum import Enum

THUMBS_UP = '👍'  # in case you go f-string ...

# move these into an Enum:
class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1
    
    def __str__(self):
        return f"{self.name} => {self.value*THUMBS_UP}"
    
    @classmethod
    def average(cls):
        return sum([s.value for s in cls]) / len([s.value for s in cls])



import pytest

def test_enum_content():
    assert list(Score) == [Score.BEGINNER, Score.INTERMEDIATE,
                           Score.ADVANCED, Score.CHEATED]


def test_equality_comparison():
    assert Score.BEGINNER is Score.BEGINNER
    assert Score.INTERMEDIATE is not Score.ADVANCED


def test_str_using_thumbsup():
    assert str(Score.BEGINNER) == 'BEGINNER => 👍👍'
    assert str(Score.INTERMEDIATE) == 'INTERMEDIATE => 👍👍👍'
    assert str(Score.ADVANCED) == 'ADVANCED => 👍👍👍👍'
    assert str(Score.CHEATED) == 'CHEATED => 👍'


def test_average():
    assert Score.average() == 2.5
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          