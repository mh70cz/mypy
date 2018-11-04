# -*- coding: utf-8 -*-
"""
Bite 39. Calculate the total duration of a course
https://codechalleng.es/bites/39/
datetime, re
Created on Thu Jul 19  2018 ;  

"""

from datetime import datetime, timedelta
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    cre = re.compile(r"\(\d+:\d\d\)")
    stamps = []
    with open(COURSE_TIMES) as f:
        for line in f:
            m = re.search(cre, line)
            if m:
                s = m.group(0).strip("()")
                stamps.append(s)
    return stamps
    

def calc_total_course_duration(timestamps):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    total = timedelta(0)
    for s in timestamps:
        mi = int(s[:s.index(":")])
        se = int(s[-2:])
        #print(mi, se)
        total += timedelta(minutes=mi, seconds=se)
    return str(total)

def test_get_all_timestamps():
    timestamps = get_all_timestamps()
    assert len(timestamps) == 99
    assert '2:29' in timestamps
    assert '4:19' in timestamps
    assert '6:06' in timestamps
    assert '8:39' in timestamps


def test_calc_total_course_duration():
    timestamps = get_all_timestamps()
    assert '6:50:31' in calc_total_course_duration(timestamps)