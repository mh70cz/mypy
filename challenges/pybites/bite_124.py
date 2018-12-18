"""
Bite 124. Marvel data analysis 

https://codechalleng.es/bites/124

"""
 
from collections import namedtuple
import csv
import re
from collections import Counter

import requests

MARVEL_CSV = 'https://raw.githubusercontent.com/pybites/marvel_challenge/master/marvel-wikia-data.csv'  # noqa E501

Character = namedtuple('Character', 'pid name sid align sex appearances year')


# csv parsing code provided so this Bite can focus on the parsing

def _get_csv_data():
    """Download the marvel csv data and return its decoded content"""
    with requests.Session() as session:
        return session.get(MARVEL_CSV).content.decode('utf-8')


def load_data():
    """Converts marvel.csv into a sequence of Character namedtuples
       as defined above"""
    content = _get_csv_data()
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        name = re.sub(r'(.*?)\(.*', r'\1', row['name']).strip()
        yield Character(pid=row['page_id'],
                        name=name,
                        sid=row['ID'],
                        align=row['ALIGN'],
                        sex=row['SEX'],
                        appearances=row['APPEARANCES'],
                        year=row['Year'])


data = list(load_data())


# start coding

  


def most_popular_characters(top=5):
    """Get the most popular character by number of appearances,
       return top n characters (default 5)
    """
    top_records = sorted(data, key= lambda x: int(x.appearances) if x.appearances.isnumeric() else 0, reverse = True)[:top]
    return [x.name for x in top_records]
   
        
        
def max_and_min_years_new_characters():
    """Get the year with most and least new characters introduced respectively,
       use either the 'FIRST APPEARANCE' or 'Year' column in the csv data, or
       the 'year' attribute of the namedtuple, return a tuple of
       (max_year, min_year)"""
    cnt_year = Counter()
    for e in data:
        y = e.year
        if y.isnumeric():
            cnt_year[y] += 1
    return (cnt_year.most_common()[0][0], cnt_year.most_common()[-1][0])
    

def percentage_female():
    """Get the percentage of female characters as percentage of all genders,
       return a percentage rounded to 2 digits"""
    cnt_sex = Counter()
    for e in data:
        s = e.sex
        cnt_sex[s] += 1
    return round(cnt_sex["Female Characters"] / len(data) * 100 , 2)
    
