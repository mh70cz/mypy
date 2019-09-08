"""
Bite 199. Multiple inheritance (__mro__)
"""

class Person():
    def __str__(self):
        return 'I am a person'

class Father(Person):
    def __str__(self):
        s = super().__str__()
        return s + ' and cool daddy'

class Mother(Person):
    def __str__(self):
        s = super().__str__()
        return s + ' and awesome mom'   

class Child(Father, Mother, Person):
    def __str__(self):
        return 'I am the coolest kid'