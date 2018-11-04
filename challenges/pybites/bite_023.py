"""
Bite 23. Find words that are > 95% similar

https://codechalleng.es/bites/23
"""
 
import os
import re
from difflib import SequenceMatcher
from itertools import product, combinations
from urllib.request import urlretrieve

# prep
TAG_HTML = re.compile(r'<category>([^<]+)</category>')
TEMPFILE = os.path.join('/tmp', 'feed')
MIN_TAG_LEN = 10
IDENTICAL = 1.0
SIMILAR = 0.95

#urlretrieve('http://bit.ly/2zD8d8b', TEMPFILE)


def _get_tags(tempfile=TEMPFILE):
    """Helper to parse all tags from a static copy of PyBites' feed,
       providing this here so you can focus on difflib"""
    with open(tempfile) as f:
        content = f.read().lower()
    # take a small subset to keep it performant
    tags = TAG_HTML.findall(content)
    tags = [tag for tag in tags if len(tag) > MIN_TAG_LEN]
    return set(tags)


def get_similarities_pybites(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    for pair in product(tags, tags):
        # bonus: better performance (shaved a second off pytest for me)
        if pair[0][0] != pair[1][0]:
            continue

        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair

def get_similarities_mh(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()

    sim_lst = []
    for t1 in tags:
        for t2 in tags:
            s = SequenceMatcher(None, t1, t2)
            if SIMILAR <= s.ratio() < IDENTICAL:            
                sim_lst.append((t1, t2))
    return sim_lst



def get_similarities(tags=None):
    """Should return a list of similar tag pairs (tuples)"""
    tags = tags or _get_tags()
    # do your thing ...
    
    for pair in combinations(tags, 2):
        # combinations are better than product (removes duplicates)
        
        #improves performance
        if pair[0][0] != pair[1][0]:
            continue
        if IDENTICAL > SequenceMatcher(None, *pair).ratio() > SIMILAR:
            yield pair            
        

import pytest

def test_get_similarities():
    # cast to list in case of generator
    similar_tags = list(get_similarities())

    # not interested in the order of the pairs
    similar_tags = {tuple(sorted(pair)) for pair in similar_tags}

    expected = [('cheat sheet', 'cheat sheets'),
                ('python anywhere', 'pythonanywhere'),
                ('web scraping', 'webscraping'),
                ('object oriented', 'objectoriented'),
                ('web scraping', 'webscraping'),
                ('contextmanager', 'contextmanagers'),
                ('python anywhere', 'pythonanywhere'),
                ('contextmanager', 'contextmanagers'),
                ('magic methods', 'magicmethods'),
                ('magic methods', 'magicmethods'),
                ('code challenges', 'codechallenges'),
                ('cheat sheet', 'cheat sheets'),
                ('object oriented', 'objectoriented'),
                ('code challenges', 'codechallenges')]

    for hit in expected:
        assert tuple(sorted(hit)) in similar_tags, f'{hit} not in similar tags'
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    