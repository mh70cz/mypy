"""
Bite 132. Find the word with the most vowels 

https://codechalleng.es/bites/132
"""
from collections import Counter
VOWELS = list('aeiou')
        



def get_word_max_vowels(text):
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)"""
    words = text.split(" ")
    mv_cnt, mv_word = 0, None
    for w in words:
        cnt = 0
        for letter in w.lower():
            if letter in VOWELS:
               cnt += 1
        # if mv_cnt <= cnt:  #the last occurence
        if mv_cnt < cnt:  #the first occurence
            mv_word, mv_cnt  = w, cnt
    return (mv_word, mv_cnt)


def get_word_max_vowels_(text):
    """sorted alphabetically"""
    words = text.split(" ")
    words_v_c = []
    for w in words:
        vow_cnt = 0
        for c in w:
            if c in VOWELS:
                vow_cnt += 1
        words_v_c.append((w, vow_cnt))
    pre_sorted = sorted(words_v_c, key=lambda x: x[0])
    return sorted(pre_sorted, key=lambda x: x[1], reverse=True)[0]

def get_word_max_vowels___(text):
    """unique vowels"""
    words = text.split(" ")
    mv_cnt, mv_word = 0, None
    for w in words:
        cnt = 0
        for v in VOWELS:
            if v in w.lower():
               cnt += 1
        if mv_cnt <= cnt:
            mv_word, mv_cnt  = w, cnt
    return (mv_word, mv_cnt)

import pytest


paragraphs = [
    ("Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms."),
    ("The Python interpreter and the extensive standard library "
     "are freely available in source or binary form for all major "
     "platforms from the Python Web site, https://www.python.org/, "
     "and may be freely distributed. The same site also contains "
     "distributions of and pointers to many free third party Python "
     "modules, programs and tools, and additional documentation."),
    ("The Python interpreter is easily extended with new functions "
     "and data types implemented in C or C++ (or other languages "
     "callable from C). Python is also suitable as an extension "
     "language for customizable applications."),
    ("This tutorial introduces the reader informally to the basic "
     "concepts and features of the Python language and system. "
     "It helps to have a Python interpreter handy for hands-on "
     "experience, but all examples are self-contained, so the "
     "tutorial can be read off-line as well."),
    ("For a description of standard objects and modules, see The "
     "Python Standard Library. The Python Language Reference gives "
     "a more formal definition of the language. To write extensions "
     "in C or C++, read Extending and Embedding the Python "
     "Interpreter and Python/C API Reference Manual. There are "
     "also several books covering Python in depth."),
    ("This tutorial does not attempt to be comprehensive and cover "
     "every single feature, or even every commonly used feature. "
     "Instead, it introduces many of Python’s most noteworthy "
     "features, and will give you a good idea of the language’s "
     "flavor and style. After reading it, you will be able to read and "
     "write Python modules and programs, and you will be ready to "
     "learn more about the various Python library modules described "
     "in The Python Standard Library.")
]
expected = [
    ('object-oriented', 6),
    ('documentation.', 6),
    ('customizable', 5),
    ('experience,', 5),
    ('definition', 5),
    ('comprehensive', 5),
]


@pytest.mark.parametrize('text, result', zip(paragraphs, expected))
def test_get_word_max_vowels(text, result):
    assert get_word_max_vowels(text) == result

    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          