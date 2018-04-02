#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 4. Top 10 PyBites tags
"""

import os
import re
from collections import Counter
import urllib.request

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')

tempfile = os.path.join('/tmp', 'feed')
urllib.request.urlretrieve('http://bit.ly/2zD8d8b', tempfile)

with open(tempfile) as f:
    content = f.read().lower()


# start coding

def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""
    tags = TAG_HTML.findall(content)
    cnt = Counter(tags)
    return cnt.most_common(n)

def test_get_pybites_top_tags():
    expected = [('python', 79),
                ('learning', 79),
                ('codechallenges', 72),
                ('twitter', 62),
                ('tips', 61),
                ('flask', 52),
                ('news', 49),
                ('django', 37),
                ('code', 25),
                ('github', 24)]
    assert get_pybites_top_tags() == expected