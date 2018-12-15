"""
 Bite 88. Write a performance monitoring context manager 


https://codechalleng.es/bites/088
"""

from collections import Counter
from contextlib import contextmanager
from datetime import date
from time import time

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: suffering performance hit today'

violations = Counter()


def get_today():
    """Making it easier to test/mock"""
    return date.today()


@contextmanager
def timeit():
    start_time = time()
    try:
        yield
    except:
        pass
    finally:
        stop_time = time()
        duration = stop_time - start_time
        if duration > OPERATION_THRESHOLD_IN_SECONDS:
            violations[get_today()] += 1
        if violations[get_today()] >= ALERT_THRESHOLD:
            print (ALERT_MSG)
            
    
            
"""
from time import sleep
with timeit():
    sleep(3)
"""