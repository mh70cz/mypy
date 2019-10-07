"""
Bite 207. Cached property decorator
"""
# -*- coding: utf-8 -*-

from random import random
from time import sleep

def cached_property(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper

class Planet():
    
    GRAVITY_CONSTANT = 42
    TEMPORAL_SHIFT = 0.12345
    SOLAR_MASS_UNITS = 'M\N{SUN}'    
    
    
    def __init__(self, color):
        self.color = color
        self._mass = None
        
    def __repr__(self):
        return f'{self.__class__.__name__}({repr(self.color)})'        
    
    @property
    @cached_property
    def mass(self):    
        scale_factor = random()
        sleep(self.TEMPORAL_SHIFT)
        self._mass = (f'{round(scale_factor * self.GRAVITY_CONSTANT, 4)} '
                      f'{self.SOLAR_MASS_UNITS}')
        return self._mass
        
