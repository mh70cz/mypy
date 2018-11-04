"""
Bite 73. Organize a meeting between timezones (pytz) 

https://codechalleng.es/bites/73
"""

import pytz
from datetime import datetime

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    utc_with_tz =  pytz.timezone("UTC").localize(utc)
    for tz in timezones:
        if not(tz in TIMEZONES):
            raise ValueError
        hour = utc_with_tz.astimezone(pytz.timezone(tz)).hour        
        if not(hour in MEETING_HOURS):
            return False
    return True        

import pytest

def test_too_late_aus():
    # local hours [15, 23, 8]
    dt = datetime(2018, 4, 18, 13, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_all_good_aus_just_in_time_summertime():
    # local hours [14, 22, 7]
    dt = datetime(2018, 4, 18, 12, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert within_schedule(dt, *timezones)


def test_change_winter_time_aus_now_too_late():
    # local hours [14, 23, 7]
    dt = datetime(2018, 10, 18, 12, 28)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_too_late_for_chicago():
    # local hours [8, 16, 1]
    dt = datetime(2018, 4, 18, 6, 45)
    timezones = ['Europe/Madrid', 'Australia/Sydney', 'America/Chicago']
    assert not within_schedule(dt, *timezones)


def test_wrong_timezone():
    dt = datetime(2018, 4, 18, 12, 28)
    timezones = ['Europe/Madrid', 'bogus']
    with pytest.raises(ValueError):
        within_schedule(dt, *timezones)
        
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          