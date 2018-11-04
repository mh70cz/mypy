# -*- coding: utf-8 -*-
"""
Bite 49. Scrape Packt's html with BeautifulSoup 
https://codechalleng.es/bites/49/
BeautifulSoup
Created on Fri Jul 20 17:45:16 2018

@author: mh70
"""

from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

import pytest
pytest.main(["bite_49.py"])

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')


def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, "html.parser")
    flb = soup.find("div", attrs={"id" : "free-learning-banner"})
    par = flb.parent
    dotd_title = par.find("div", attrs={"class": "dotd-title"})
    title = dotd_title.find("h2").contents[0].strip("\n\t")
    desc = dotd_title.findNext("div").contents[0].strip("\n\t")
    a = par.find("a")
    image = a.find("img").attrs["src"]
    link = a.attrs["href"]
    
    return Book(title=title, description=desc, image=image, link=link)
    


book = get_book()


def test_type():
    assert isinstance(book, tuple)


def test_book_title():
    assert book.title == 'Mastering TypeScript - Second Edition'


def test_book_description():
    assert book.description == ('Build enterprise-ready, industrial-strength '
                                'web applications using '
                                'TypeScript and leading JavaScript frameworks')


def test_book_image():
    assert book.image == '//d1ldz4te4covpm.cloudfront.net/sites/default/files/imagecache/dotd_main_image/B05588.png'  # noqa E501


def test_book_link():
    assert book.link == '/application-development/mastering-typescript-second-edition'  # noqa E501