"""
Bite 181. Keep a list sorted upon insert
"""

import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        position = bisect.bisect(self._numbers, num)
        self._numbers.insert(position, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)