"""
Bite 147. 100 WEEKDays of Code Date Range 

https://codechalleng.es/bites/147
"""

     
            
from datetime import date


from dateutil.rrule import rrule, DAILY, MO,TU,WE,TH,FR


TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    mo_fr_days_rrule = rrule(DAILY, count=100, byweekday=(MO,TU,WE,TH,FR) ,
                             dtstart = start_date)
    mo_fr_days = [dt.date() for dt in mo_fr_days_rrule]
    return mo_fr_days

