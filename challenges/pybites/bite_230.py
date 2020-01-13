# -*- coding: utf-8 -*-
"""
Bite 230. Thumbs up for operator overloading 
"""

THUMBS_UP = '👍'
THUMBS_DOWN = '👎'

class Thumbs:  

    def __mul__(self, other):      
        return self._write(other)
                       
    def __rmul__(self, other):
        return self._write(other)

    def _write(self, cnt):        
        if cnt == 0:
            raise ValueError("Specify a number")
        if cnt < -3:
            return f"{THUMBS_DOWN} ({-cnt}x)"
        if cnt < 0:
            return -cnt * THUMBS_DOWN
        if cnt < 4:
            return cnt * THUMBS_UP
        else:
            return  f"{THUMBS_UP} ({cnt}x)"        