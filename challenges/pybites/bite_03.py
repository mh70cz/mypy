# -*- coding: utf-8 -*-
"""
Bite 3. Word Values
"""


import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    lst = list()
    with open(DICTIONARY, 'r') as f:
        for line in f:
            lst.append(line.strip())
    return lst


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    value = 0
    for l in word:
        value += LETTER_SCORES.get(l.upper(), 0)
    return value

def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    max_val = 0
    max_word = ""
    for w in words:
        word_val = calc_word_value(w)
        if  word_val > max_val:
            max_val = word_val
            max_word = w
    return max_word

words = load_words()
max_word = max_word_value(words)
