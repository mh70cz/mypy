"""
Bite 138. OOP fun at the Zoo 

https://codechalleng.es/bites/138
"""
 
class Animal:
    _counter = 10_000
    _zoo = []
    def __init__(self, name):
        Animal._counter += 1
        self.animal = str(Animal._counter) + ". " + name.title()
        Animal._zoo.append(self.animal)

    def __str__(self):
        return self.animal
    
    @classmethod
    def zoo(self):
        return Animal._zoo

import pytest


def test_zoo_5_animals():
    for animal in 'dog cat fish lion mouse'.split():
        Animal(animal)
    zoo = Animal.zoo()
    assert "10001. Dog" in zoo
    assert "10002. Cat" in zoo
    assert "10003. Fish" in zoo
    assert "10004. Lion" in zoo
    assert "10005. Mouse" in zoo


def test_animal_instance_str():
    horse = Animal('horse')
    assert str(horse) == "10006. Horse"
    horse = Animal('monkey')
    assert str(horse) == "10007. Monkey"
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    