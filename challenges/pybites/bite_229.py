# -*- coding: utf-8 -*-
"""
Bite 229. Scrape best programming books 
"""

from pathlib import Path
from urllib.request import urlretrieve

from bs4 import BeautifulSoup
from dataclasses import dataclass

url = ("https://bites-data.s3.us-east-2.amazonaws.com/"
       "best-programming-books.html")
tmp = Path("/tmp")
html_file = tmp / "books.html"

if not html_file.exists():
    urlretrieve(url, html_file)

@dataclass
class Book:
    """Book class should instatiate the following variables:

    title - as it appears on the page
    author - should be entered as lastname, firstname
    year - four digit integer year that the book was published
    rank - integer rank to be updated once the books have been sorted
    rating - float as indicated on the page
    """
    title: str
    author: str
    year: int
    rank: int
    rating: float
    
    def __str__(self):
        line1 = (f"[{self.rank:03}] {self.title} ({self.year})") 
        line2 = (f"{6*' '}{self.author} {self.rating}")
        return line1 + "\n" + line2
    


def _get_soup(file):
    #return BeautifulSoup(file.read_text(), "html.parser")
    return BeautifulSoup(html_file.read_text(encoding="utf8"), "html.parser")


def display_books(books, limit=10, year=None):
    """Prints the specified books to the console

    :param books: list of all the books
    :param limit: integer that indicates how many books to return
    :param year: integer indicating the oldest year to include
    :return: None
    """
    pass


def load_data():
    """Loads the data from the html file

    Creates the soup object and processes it to extract the information
    required to create the Book class objects and returns a sorted list
    of Book objects.

    Books should be sorted by rating, year, title, and then by author's
    last name. After the books have been sorted, the rank of each book
    should be updated to indicate this new sorting order.The Book object
    with the highest rating should be first and go down from there.
    """
    soup = _get_soup(html_file)
    book_headers = soup.find_all("div", class_="book-header-title" )
    for bh in book_headers:
        title = bh.find("h2", class_="main")
        if title:
            title = title.text
        else:
            continue
        
        authors = bh.find("h3", class_="authors")
        if authors:
            authors = authors.text
        else:
            continue
        
        date = bh.find("span", class_="date")
        if date:
            date = date.text
        else:
            continue
        
        rating = bh.find("span", class_="our-rating")
        if rating:
            rating = rating.text
        else:
            continue
        
        if not "python" in title.lower():
            continue
        
        print(title, authors, date, rating)
        


def main():
    books = load_data()
    display_books(books, limit=5, year=2017)
    """If done correctly, the previous function call should display the
    output below.
    """


if __name__ == "__main__":
    main()

"""
[001] Python Tricks (2017)
      Bader, Dan 4.74
[002] Mastering Deep Learning Fundamentals with Python (2019)
      Wilson, Richard 4.7
[006] Python Programming (2019)
      Fedden, Antony Mc 4.68
[007] Python Programming (2019)
      Mining, Joseph 4.68
[009] A Smarter Way to Learn Python (2017)
      Myers, Mark 4.66
"""