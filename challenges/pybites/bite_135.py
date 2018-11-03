"""
Bite 135. Sort a list of book objects 

https://codechalleng.es/bites/135
"""
from collections import namedtuple
from datetime import datetime
from operator import attrgetter

Book = namedtuple('Book', 'title authors pages published')

books = [
    Book(title="Python Interviews",
         authors="Michael Driscoll",
         pages=366,
         published="2018-02-28"),
    Book(title="Python Cookbook",
         authors="David Beazley, Brian K. Jones",
         pages=706,
         published="2013-05-10"),
    Book(title="The Quick Python Book",
         authors="Naomi Ceder",
         pages=362,
         published="2010-01-15"),
    Book(title="Fluent Python",
         authors="Luciano Ramalho",
         pages=792,
         published="2015-07-30"),
    Book(title="Automate the Boring Stuff with Python",
         authors="Al Sweigart",
         pages=504,
         published="2015-04-14"),
]


# all functions return books sorted in ascending order.

def sort_books_by_len_of_title(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted([b for b in books], key = lambda x: len(x.title))




def sort_books_by_first_authors_last_name(books=books):
    """
    Expected last book in list:
    Automate the Boring Stuff with Python
    """
    return sorted([b for b in books], key = lambda x: x.title.split(" ")[1])

    


def sort_books_by_number_of_page(books=books):
    """
    Expected last book in list:
    Fluent Python
    """
    #return sorted([b for b in books], key = lambda x: x.pages)
    return sorted([b for b in books], key = attrgetter("pages"))


def sort_books_by_published_date(books=books):
    """
    Expected last book in list:
    Python Interviews
    """
    # return sorted([b for b in books], key = lambda x: x.published)
    return sorted([b for b in books], key = attrgetter("published"))

import pytest



def test_sort_books_by_len_of_title():
    last_book = sort_books_by_len_of_title()[-1]
    assert last_book.title == 'Automate the Boring Stuff with Python'


def test_sort_books_by_first_authors_last_name():
    last_book = sort_books_by_first_authors_last_name()[-1]
    assert last_book.title == 'Automate the Boring Stuff with Python'


def test_sort_books_by_number_of_page():
    last_book = sort_books_by_number_of_page()[-1]
    assert last_book.title == 'Fluent Python'


def test_sort_books_by_published_date():
    last_book = sort_books_by_published_date()[-1]
    assert last_book.title == 'Python Interviews'

    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          