"""
Bite 175. Find missing dates
"""
import datetime
import random

def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    ord_dates = []
    missing_dates = []
    for d in dates:
        ord_dates.append(d.toordinal())
    ord_dates.sort()
    first = ord_dates[0]
    last = ord_dates[-1]
    
    for d in range(first + 1, last):
        if d not in ord_dates:
            missing_dates.append(datetime.date.fromordinal(d))
    return missing_dates
    
    
def gen_rnd_dates():
    dates = []
    for i in range(10):
        rnd_y = random.randint(1900,2019)
        rnd_m = random.randint(1,12)
        rnd_d = random.randint(1,28)
        #dates.append(datetime.date(rnd_y, rnd_m, rnd_d))
        dates.append(datetime.date(2019, 8, rnd_d))
    return dates

# gen_rnd_dates()
    