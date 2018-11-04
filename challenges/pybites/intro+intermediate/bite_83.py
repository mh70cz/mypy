#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timezone, pytz

@author: mh70; 2018-07-06
"""
import datetime

# from pytz import timezone, utc
import pytz

AUSTRALIA = pytz.timezone("Australia/Sydney")
SPAIN = pytz.timezone("Europe/Madrid")
CZ = pytz.timezone("Europe/Prague")


def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    aus = naive_utc_dt.astimezone(AUSTRALIA)
    esp = naive_utc_dt.astimezone(SPAIN)
    return (aus, esp)


now_utctz_d = datetime.datetime.now(tz=datetime.timezone.utc)  # import datetime
now_utctz_p = datetime.datetime.now(tz=pytz.utc)
# import pytz ; 3rd party: $ pip install pytz
now_naive = datetime.datetime.now()
now_naive_utc = datetime.datetime.utcnow()

print(f"now_utctz_d       {now_utctz_d } ")
print(f"now_utctz_p       {now_utctz_p } ")
print(f"now_naive         {now_naive } ")
print(f"now_naive_utc     {now_naive_utc } ")

print(f"naive to  UTC     {now_naive.astimezone(tz=datetime.timezone.utc)} ")
print(
    f"naive_utc to UTC  {now_naive_utc.astimezone(tz=datetime.timezone.utc)} WRONG, WRONG, WRONG"
)
