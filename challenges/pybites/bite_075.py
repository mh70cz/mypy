"""
Bite 75. Parse Unix cal to a weekday mapping


https://codechalleng.es/bites/075
"""

from itertools import cycle

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""
    
    
    first, *_ , last = calendar_output.split("\n")[2:-1]
    
    last_day = int(last.split(" ")[-1])
    
    first_week_day_idx = 7 - len( [x for x in first.split(" ") if x is not ""])
    
    
    c_week_days = cycle(['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'])
    for i in range(first_week_day_idx):
        _ = next(c_week_days)
    
    cal_dct = {}
    
    
    for i in range(1, last_day + 1):
        cal_dct[i]=next(c_week_days)
        
    
    return cal_dct    
    
    