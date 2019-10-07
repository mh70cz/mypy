# -*- coding: utf-8 -*-
"""
Bite 209. Write a Sphinx docstring
"""
import re
from bite_209 import sum_numbers
def test_sum_numbers():
    doc = f'\n{sum_numbers.__doc__.strip()}'

    # for some lines allow variable content after colon
    for line in ('Sums numbers',
                 '    :param numbers: \S.*?\n',
                 '    :type numbers: list',
                 '    :raises TypeError: \S.*?\n',
                 '    :return: \S.*?\n',
                 '    :rtype: int'):
        # newline to test proper indenting
        assert re.search(rf'\n{line}', doc)