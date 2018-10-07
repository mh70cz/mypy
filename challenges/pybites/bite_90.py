"""
Bite 90. What South Park characters talk most? 

https://codechalleng.es/bites/90
"""
from collections import Counter, defaultdict
import csv

import requests

CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv' # noqa E501


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    dd = defaultdict(Counter)
    csv_reader = csv.reader(content.splitlines(), delimiter=",")
    next(csv_reader) #read header
    for row in csv_reader:
        episode = row[1]
        character = row[2]
        n_words = len(row[3].split())
        #dd[character].update({episode:n_words})
        dd[character][episode] += n_words
    return dd

   


import pytest




@pytest.fixture(scope="module")
def words_spoken_s1():
    # module scope to not call requests for every test function
    content = get_season_csv_file(season=1)
    return get_num_words_spoken_by_character_per_episode(content)


@pytest.fixture(scope="module")
def words_spoken_s5():
    content = get_season_csv_file(season=5)
    return get_num_words_spoken_by_character_per_episode(content)


def test_get_words_spoken_season1_stan(words_spoken_s1):
    expected = [('4', 615), ('6', 572), ('5', 514)]
    assert words_spoken_s1['Stan'].most_common()[:3] == expected


def test_get_words_spoken_season1_cartman(words_spoken_s1):
    expected = [('1', 735), ('10', 669), ('13', 621)]
    assert words_spoken_s1['Cartman'].most_common()[:3] == expected


def test_get_words_spoken_season1_cartman_least_talkative(words_spoken_s1):
    expected = [('11', 285), ('6', 264), ('4', 244)]
    assert words_spoken_s1['Cartman'].most_common()[-3:] == expected


def get_words_spoken_non_existing_character(words_spoken_s1):
    assert words_spoken_s1['bogus'].most_common() == []


# let's look at another season and other characters

def test_get_words_spoken_season5_sheila(words_spoken_s5):
    expected = [('11', 295), ('6', 212), ('7', 52)]
    assert words_spoken_s5['Sheila'].most_common()[:3] == expected


def test_get_words_spoken_season5_choksondik(words_spoken_s5):
    expected = [('7', 749), ('10', 131), ('1', 129)]
    assert words_spoken_s5['Ms. Choksondik'].most_common()[:3] == expected


        
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          