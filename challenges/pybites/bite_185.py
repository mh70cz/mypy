"""
Bite 185. Create a simple spelling suggester
"""

from difflib import SequenceMatcher
from os import path
from urllib.request import urlretrieve


DICTIONARY = path.join('/tmp', 'dictionary.txt')
if not path.isfile(DICTIONARY):
    urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)


def load_words():
    """Return a set of words from DICTIONARY"""
    with open(DICTIONARY) as f:
        return {word.strip().lower() for word in f.readlines()}


def suggest_word(misspelled_word: str, words: set = None) -> str:
    """Return a valid alternative word that best matches
       the entered misspelled word"""
    if words is None:
        words = load_words()
    
    max_ratio = 0
    sugg_w = misspelled_word
    for dict_w in words:
        sm = SequenceMatcher(lambda x: x==" ", misspelled_word, dict_w)
        r = sm.ratio()
        if r > max_ratio:
            max_ratio = r
            sugg_w = dict_w
            #print(r, sugg_w)
    return sugg_w
    
        

   