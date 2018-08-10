"""
Bite 65. Get all valid dictionary words for a draw of letters 
https://codechalleng.es/bites/65/

Created on  2018-08-10

"""
import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])


def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    valid_words= []
    all_p = _get_permutations_draw(draw)
    for ll in all_p:
        w = "".join(ll).lower()
        if w in dictionary:
            valid_words.append(w)
    return valid_words

def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    #w = draw.split(", ")
    all_p = []
    for i in range(1, len(draw)):
        p = itertools.permutations(draw, i)
        all_p.extend(p)
    return all_p



import pytest



scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


@pytest.mark.parametrize("draw, expected", [
    ('T, I, I, G, T, T, L', 'gilt'),
    ('O, N, V, R, A, Z, H', 'zonar'),
    ('E, P, A, E, I, O, A', ('apio', 'peai')),
    ('B, R, C, O, O, E, O', 'boce'),
    ('G, A, R, Y, T, E, V', 'garvey'),
])
def test_max_word(draw, expected):
    draw = draw.split(', ')
    words = get_possible_dict_words(draw)
    if len(expected) > 1:
        assert max_word_value(words) in expected
    else:
        assert max_word_value(words) == expected
        
#import sys
#if __name__ == '__main__':
#    pytest.main(sys.argv)             