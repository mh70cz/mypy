# -*- coding: utf-8 -*-
"""
 Bite 222. Split an iterable in groups of size n
"""

from bite_222 import group


def test_split_10_ints_by_3():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    assert actual == expected


def test_passing_in_generator():
    iterable = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
    assert actual == expected


def test_different_iterable_size():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n = 3
    actual = group(iterable, n)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 1, 2],
                [3, 4, 5], [6, 7, 8], [9, 10]]
    assert actual == expected


def test_different_n():
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
    n = 5
    actual = group(iterable, n)
    expected = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
                [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
    assert actual == expected