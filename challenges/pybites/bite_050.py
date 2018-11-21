"""
 Bite 50. Make a little PyBites search engine (feedparser) 

https://codechalleng.es/bites/50
"""
 
from collections import namedtuple
from datetime import datetime, date

import feedparser

FEED = 'http://projects.bobbelderbos.com/pcc/all.rss.xml'

Entry = namedtuple('Entry', 'date title link tags')


def _convert_struct_time_to_dt(stime):
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)"""
    return datetime.strptime("-".join(stime.split(" ")[1:4]), "%d-%b-%Y")


def get_feed_entries(feed=FEED):
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)"""
    feed = feedparser.parse(FEED)
    entries = []
    for e in feed["entries"]:
        dat = _convert_struct_time_to_dt(e["published"])
        title = e["title"]
        link = e["link"]
        tags = e["tags"]
        entry = Entry(dat, title, link, tags)
        entries.append(entry)
    return entries
        
    


def filter_entries_by_tag(search, entry):
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags"""
    terms = [t["term"].lower() for t in entry.tags]
    
    
    if "&" in search:
        search1, search2 = search.split("&")
        if (search1.lower() in terms) and (search2.lower() in terms):
            return True
        return False
        
    if "|" in search:
        search1, search2 = search.split("|")
        if (search1.lower() in terms) or (search2.lower() in terms):
            return True
        return False
    
    if search.lower() in terms:
        return True
    return False
    
        

def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term, exit on 'q', try again upon empty input
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the date+title+link of each match ordered by date desc
       6. Secondly, print the number of matches"""
    entries = get_feed_entries()

e

from unittest.mock import patch

import pytest


class AttrDict(dict):
    """feedparser lets you access dict keys as attributes, hence a bit of
       mocking, got this from https://stackoverflow.com/a/14620633"""
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


dt1 = datetime(2018, 2, 18, 19, 52, 0).timetuple()
dt2 = datetime(2017, 1, 6, 11, 0, 0).timetuple()

MOCK_ENTRIES = {'entries':
                [AttrDict({'author': 'PyBites',
                           'link':
                           'https://pybit.es/twitter_digest_201808.html',  # noqa E501
                           'published': 'Sun, 18 Feb 2018 20:52:00 +0100',  # noqa E501
                           'published_parsed': dt1,
                           'summary': '<p>Every weekend we share ...',
                           'tags': [AttrDict({'term': 'twitter'}),
                                    AttrDict({'term': 'Flask'}),
                                    AttrDict({'term': 'Python'}),
                                    AttrDict({'term': 'Regex'})],
                           'title': 'Twitter Digest 2018 Week 08'}),
                 AttrDict({'author': 'Julian',
                           'link': 'https://pybit.es/pyperclip.html',
                           'published': 'Fri, 06 Jan 2017 12:00:00 +0100',  # noqa E501
                           'published_parsed': dt2,
                           'summary': '<p>Use the Pyperclip module to ...',
                           'tags': [AttrDict({'term': 'python'}),
                                    AttrDict({'term': 'tips'}),
                                    AttrDict({'term': 'tricks'}),
                                    AttrDict({'term': 'code'}),
                                    AttrDict({'term': 'pybites'})],
                           'title': 'Copy and Paste with Pyperclip'})]}


@pytest.mark.parametrize("arg, ret", [
    (datetime(2017, 9, 12, 8, 50, 0).timetuple(),
     date(year=2017, month=9, day=12)),
    (datetime(2017, 9, 8, 14, 30, 0).timetuple(),
     date(year=2017, month=9, day=8)),
    (datetime(2016, 12, 19, 9, 26, 0).timetuple(),
     date(year=2016, month=12, day=19)),
])
def test_convert_struct_time_to_dt(arg, ret):
    assert _convert_struct_time_to_dt(arg) == ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
def test_get_feed_entries(inp):
    first, last = tuple(get_feed_entries())

    assert first.date == date(year=2018, month=2, day=18)
    assert first.title == 'Twitter Digest 2018 Week 08'
    assert first.link == 'https://pybit.es/twitter_digest_201808.html'
    expected = ['flask', 'python', 'regex', 'twitter']
    # allow list or set
    assert sorted(list(first.tags)) == expected

    assert last.date == date(year=2017, month=1, day=6)
    assert last.title == 'Copy and Paste with Pyperclip'
    assert last.link == 'https://pybit.es/pyperclip.html'
    expected = ['code', 'pybites', 'python', 'tips', 'tricks']
    assert sorted(list(last.tags)) == expected


@pytest.mark.parametrize("arg, ret", [
    ('blabla', False),
    ('tricks', True),
    ('TRICKS', True),  # case should not matter
    ('TriCkS', True),
    ('python', False),  # whole term only so python != pythonic
    ('matplotlib&pandas', True),
    ('matplotlib&pandas&collections', True),
    ('matplotlib&pandas&flask', False),
    ('matplotlib|flask', True),
    ('matplotlib|django|flask', True),
    ('pyramid|django|flask', False),
])
def test_filter_entries_by_tag(arg, ret):
    entry = Entry(date=date(2016, 12, 22),
                  title='2016 py articles and useful books',
                  link='https://pybit.es/py-articles-books2016.html',
                  tags={'pythonic', 'data science',
                        'tips', 'tricks', 'matplotlib',
                        'pandas', 'books', 'collections'})
    assert filter_entries_by_tag(arg, entry) is ret


@patch("feedparser.parse", side_effect=[MOCK_ENTRIES])
@patch("builtins.input", side_effect=['pycon', 'twitter', 'python', 'nonsense',
                                      'python|regex', 'python&regex', 'REGeX',
                                      '', 'q'])
def test_main(entries, inp, capfd):
    main()
    out, _ = capfd.readouterr()

    output = [line for line in out.split('\n') if line.strip()]
    expected = ['0 entries matched', 'Twitter Digest 2018 Week 08',
                '1 entry matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                '0 entries matched', 'Copy and Paste with Pyperclip',
                'Twitter Digest 2018 Week 08', '2 entries matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Twitter Digest 2018 Week 08', '1 entry matched',
                'Please provide a search term', 'Bye']
    for line, exp in zip(output, expected):
        assert exp in line

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    