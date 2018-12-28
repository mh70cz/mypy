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
    actual_words = []
    for potential_word in _get_permutations_draw(draw):
        if potential_word in dictionary:
            actual_words.append(potential_word)
    if len(actual_words) == 1:
        return actual_words[0]
    else:
        return tuple(actual_words)
 
def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    r = 0
    p = 0
    draw = [letter.lower().strip() for letter in draw]
    no_repeat_perms = []
    num_letters = len(draw)
    for num in range(2,num_letters+1):
        for letters in itertools.permutations(draw, num):
            word = "".join(letters)
            if word not in no_repeat_perms:
                no_repeat_perms.append(word)
                p += 1
            else:
                r += 1
                print(str(r) + " repeated: " + word)
    print ("non repeated permutations: " + str(p))
    return no_repeat_perms 

def _get_permutations_draw_(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    draw = [letter.lower().strip() for letter in draw]
    perms = []
    num_letters = len(draw)
    for num in range(2,num_letters+1):
        for letters in itertools.permutations(draw, num):
            word = "".join(letters)
            perms.append(word)
    return set(perms)



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
        
import sys
if __name__ == '__main__':
#    pytest.main(sys.argv)   
#    print(get_possible_dict_words(["T", "I", "I", "G", "T", "T", "L"]))
    print(get_possible_dict_words(["T", "I",  "I", "G", "L"]))
    