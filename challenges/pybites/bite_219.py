# -*- coding: utf-8 -*-
"""
Bite 219. Bite notification planner
"""

from datetime import date, timedelta

TODAY = date.today()


def gen_bite_planning(num_bites=1, num_days=1, start_date=TODAY):
    date_now = start_date
    while True:        
        date_now += timedelta(days=num_days)
        for i in range(num_bites):
            yield date_now
        date_now            
        
        
#for _ in range(10):
#    print(next(g))