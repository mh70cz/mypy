"""
Bite 125. Get the most recommended books  

https://codechalleng.es/bites/125
"""
from collections import Counter

from bs4 import BeautifulSoup
import requests

AMAZON = "amazon.com"
TIM_BLOG = 'https://bit.ly/2NBnZ6P'


def load_page():
    """Download the blog html and return its decoded content"""
    with requests.Session() as session:
        return session.get(TIM_BLOG).content.decode('utf-8')


def get_top_books(content=None, limit=5):
    """Make a BeautifulSoup object loading in content,
       find all links and filter on AMAZON, extract the book title
       and count them, return the top "limit" books (default 5)"""
    if content is None:
        content = load_page()
    soup = BeautifulSoup(content, 'html.parser')
    body = soup.body
    links = body.find_all("a")
    titles = [link.text for link in links if AMAZON in link["href"] ]
    c = Counter(titles)
    c.most_common(limit)
    return [title[0] for title in  c.most_common(5)]
                
import pytest

content = load_page()  # make sure we do this once!
books = get_top_books(content=content)


def test_books_6_occurrences():
    assert books[0] == 'Man’s Search For Meaning'


def test_books_5_occurrences():
    assert books[1] == 'Tao Te Ching'


def test_books_4_occurrences():
    assert sorted(books[2:5]) == ['Sapiens: A Brief History of Humankind',
                                  ('The 4-Hour Workweek: Escape the 9-5, Live '
                                   'Anywhere and Join the New Rich'),
                                  'The Fountainhead']  # 4x
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          