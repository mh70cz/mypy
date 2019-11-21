"""
Bite 187. Actor/actress age at movie release
"""

from dataclasses import dataclass

#import dateutil
from dateutil.parser import parse


@dataclass
class Actor:
    name: str
    born: str


@dataclass
class Movie:
    title: str
    release_date: str


def get_age(actor: Actor, movie: Movie) -> str:
    """Calculates age of actor / actress when movie was released,
       return a string like this:

       {name} was {age} years old when {movie} came out.
       e.g.
       Wesley Snipes was 28 years old when New Jack City came out.
    """
    name = actor.name
    born = parse(actor.born)
    title = movie.title
    release = parse(movie.release_date)
    
    age = (release - born).days // 365
    return f"{name} was {age} years old when {title} came out."
    
    