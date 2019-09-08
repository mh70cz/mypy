"""
Bite 197. What date is Mother's Day celebrated?
"""

from datetime import date


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    d = date(year, 5, 1)
    wd = d.weekday() #0 Monday , 6 Sunday
    return date(year, 5, 14 - wd)