"""
 Bite 139. Calculate a coding streak in days 

https://codechalleng.es/bites/139
"""
 
from datetime import datetime, timedelta, date

TODAY = date(2018, 11, 12)


def extract_dates(data):
    """Extract dates from DB table representation as shown in Bite"""
    lines = data.split("\n")
    dates_txt = [line[6:16] for line in lines if len(line) > 12 and line[6].isnumeric()]
    return {date(int(d[0:4]), int(d[5:7]), int(d[8:10])) for d in dates_txt}
    


def calculate_streak(dates):
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    dts =sorted(dates , reverse=True)

    if dts[0] == TODAY:
        shift = TODAY    
    else:
        shift = TODAY - timedelta(days=1)
    streak = 0    
    
    for d in dts:
        if d != shift:
            break
        shift -= timedelta(days=1)
        streak += 1        
    return streak


import pytest







def test_extract_dates():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    #print(dates)
    assert len(dates) == 8
    assert date(2018, 9, 18) in dates
    assert date(2018, 10, 23) in dates
    assert date(2018, 11, 9) in dates


def test_streak_of_0_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-10 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 0


def test_streak_of_1_day_can_still_make_today():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-23 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-18 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 1


def test_streak_of_1_day_thanks_to_todays_progress():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-09 | 100d       | 1       |
    | 2018-11-07 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 1


def test_streak_of_3_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-12 | pcc        | 1       |
    | 2018-11-11 | 100d       | 1       |
    | 2018-11-10 | 100d       | 2       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-15 | pcc        | 1       |
    | 2018-10-05 | bite       | 1       |
    | 2018-09-21 | bite       | 4       |
    | 2018-09-18 | bite       | 2       |
    | 2018-09-16 | bite       | 4       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 3


def test_streak_of_10_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-06 | bite       | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 10


def test_streak_of_almost_10_days_but_gap_so_only_5_days():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-08 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-05 | bite       | 4       |
    | 2018-11-04 | bite       | 2       |
    | 2018-11-03 | bite       | 4       |
    | 2018-11-02 | 100d       | 2       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 5


def test_streak_of_5_days_dates_out_of_order():
    data = """
    +------------+------------+---------+
    | date       | activity   | count   |
    |------------+------------+---------|
    | 2018-11-11 | pcc        | 1       |
    | 2018-11-07 | pcc        | 1       |
    | 2018-11-09 | 100d       | 2       |
    | 2018-11-10 | 100d       | 1       |
    | 2018-11-08 | pcc        | 1       |
    +------------+------------+---------+
    """
    dates = extract_dates(data)
    streak = calculate_streak(dates)
    assert streak == 5
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    