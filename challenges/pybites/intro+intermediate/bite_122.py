"""
Bite 122. Check if two words are anagrams 

https://codechalleng.es/bites/122
"""

from collections import Counter

def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    c1 = Counter(word1)
    c2 = Counter(word2)
    if c1 == c2:
        return True
    else:
        return False

  

# https://en.wikipedia.org/wiki/Anagram
# Anagrams may be created as a commentary on the subject.
# They may be a synonym or antonym of their subject,
# a parody, a criticism or satire.
import pytest


@pytest.mark.parametrize("word1, word2", [
    ("rail safety", "fairy tales"),
    ("roast beef", "eat for BSE"),
    # An anagram which means the opposite of its subject is
    # called an "antigram". For example:
    ("restful", "fluster"),
    ("funeral", "real fun"),
    ("adultery", "true lady"),
    ("customers", "store scum"),
    ("forty five", "over fifty"),
    # They can sometimes change from a proper noun or personal
    # name into an appropriate sentence:
    ("William Shakespeare", "I am a weakish speller"),
    ("Madam Curie", "Radium came"),
])
def test_is_anagram(word1, word2):
    assert is_anagram(word1, word2)


@pytest.mark.parametrize("word1, word2", [
    ("rail safety", "fairy fun"),
    ("roast beef", "eat for ME"),
    ("restful", "fluester"),
    ("funeral", "real funny"),
    ("adultery", "true ladie"),
    ("customers", "store scam"),
    ("forty five", "over fifty1"),
    ("William Shakespeare", "I am a strong speller"),
    ("Madam Curie", "Radium come"),
])
def test_is_not_anagram(word1, word2):
    assert not is_anagram(word1, word2)
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          