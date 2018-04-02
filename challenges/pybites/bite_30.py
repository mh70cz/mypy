#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 30. Movie data analysis
"""

import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve


BASE_URL = 'http://projects.bobbelderbos.com/pcc/movies/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    movies = dict()
    with open(MOVIE_DATA) as f:
        reader = csv.DictReader(f)
        for row in reader:        
            try:   
                y = int(row['title_year'])
                s = float(row['imdb_score'])
            except:
                # print (row['movie_title'], row['title_year'], row['imdb_score'])
                pass
            else:
                if y >= 1960:
                    if row['director_name'] in movies:
                        v = movies[row['director_name']]
                        v.append(Movie(row['movie_title'], y, s))
                    else:
                        movies[row['director_name']] = [Movie(
                            row['movie_title'], y, s), ]
    return movies
            


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = list()    
    for m in movies:
        scores.append(m.score)
    return round(sum(scores)/len(scores), 1)
        


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    dir_avg_scr = list()
    for k, v in directors.items():
        if len(v) >= MIN_MOVIES:
            avg_scr = calc_mean_score(v)
            dir_avg_scr.append((k, avg_scr))
    return sorted(dir_avg_scr, key=lambda x: x[1], reverse=True)


#test

director_movies = get_movies_by_director()


def test_get_movies_by_director():
    assert 'Sergio Leone' in director_movies
    assert len(director_movies['Sergio Leone']) == 4
    assert len(director_movies['Peter Jackson']) == 12


def test_director_movies_data_structure():
    assert type(director_movies) in (dict, defaultdict)
    assert type(director_movies['Peter Jackson']) == list
    assert type(director_movies['Peter Jackson'][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies['Sergio Leone']
    movies_nolan = director_movies['Christopher Nolan']
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    avg_scores = get_average_scores(director_movies)[:10]
    expected = [('Sergio Leone', 8.5),
                ('Christopher Nolan', 8.4),
                ('Quentin Tarantino', 8.2),
                ('Hayao Miyazaki', 8.2),
                ('Frank Darabont', 8.0),
                ('Stanley Kubrick', 8.0),
                ('James Cameron', 7.9),
                ('Joss Whedon', 7.9),
                ('Alejandro G. Iñárritu', 7.8),
                ('Alfonso Cuarón', 7.8)]
    assert avg_scores == expected