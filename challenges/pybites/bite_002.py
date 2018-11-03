"""
 Bite 2. Regex Fun

https://codechalleng.es/bites/2
"""
import re

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    r = re.compile(r"\d\d:\d\d")
    return r.findall(flask_course)


def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""
    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')
    r = re.compile(r"(http\S+) (#\w+) (#\w+)")
    return list(r.search(tweet).groups())
    #return re.findall(r'((?:#|http)\S+)', tweet)

def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    return re.search(r"pybites != greedy", html)[0]

import pytest


def test_extract_course_times():
    expected = ['01:47', '32:03', '41:51', '27:48', '05:02']
    assert extract_course_times() == expected


def test_get_all_hashtags_and_links():
    expected = ['http://pybit.es/requests-cache.html', '#python', '#APIs']
    assert get_all_hashtags_and_links() == expected


def test_match_first_paragraph():
    expected = 'pybites != greedy'
    assert match_first_paragraph() == expected

    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          