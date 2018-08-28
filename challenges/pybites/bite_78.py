"""
Bite 78. Find programmers with common languages 

https://codechalleng.es/bites/78
"""

def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    langs = []
    for k in programmers:
        s = set(programmers[k])
        langs.append(s)
    int_langs = langs[0].intersection(*langs[1:])
    return  int_langs 
    



import pytest


@pytest.fixture()
def programmers():
    return dict(bob=['JS', 'PHP', 'Python', 'Perl', 'Java'],
                tim=['Python', 'Haskell', 'C++', 'JS'],
                sara=['Perl', 'C', 'Java', 'Python', 'JS'],
                paul=['C++', 'JS', 'Python'])


def test_common_languages(programmers):
    expected = ['JS', 'Python']
    actual = common_languages(programmers)
    assert sorted(list(actual)) == expected


def test_adding_programmer_without_js(programmers):
    programmers['sue'] = ['Scala', 'Python']
    expected = ['Python']
    actual = common_languages(programmers)
    assert list(actual) == expected


def test_adding_programmer_without_js_nor_python(programmers):
    programmers['fabio'] = ['PHP']
    expected = []
    actual = common_languages(programmers)
    assert list(actual) == expected


def test_common_languages_adding_new_common_language(programmers):
    programmers['bob'].append('C++')
    programmers['sara'].append('C++')
    expected = ['C++', 'JS', 'Python']
    actual = common_languages(programmers)
    assert sorted(list(actual)) == expected
    
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          