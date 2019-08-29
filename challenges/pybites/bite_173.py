"""
Bite 173. Set up future notifications
"""

from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6,
               hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str,
             start_time: datetime = NOW) -> datetime:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    
    parsed_time = _parse_time(delay_time)
    add_time = start_time + timedelta(*parsed_time)
    add_time = add_time.strftime("%Y-%m-%d %H:%M:%S")
    return f"{task} @ {add_time}"

def _parse_time(t_string):
    days = re.search(r"\d*d", t_string)
    hors = re.search(r"\d*h", t_string)
    mins = re.search(r"\d*m", t_string)
    secs = re.search(r"\d*s", t_string)
    secs_2 = re.match(r"\d*$", t_string)
                     
    
    days = int(days[0][:-1]) if days else 0
    hors = int(hors[0][:-1]) if hors else 0
    mins = int(mins[0][:-1]) if mins else 0
    if secs:
        secs = int(secs[0][:-1])
    elif secs_2:
        secs = int(secs_2[0])
    else:
        secs = 0
    
    secs_total = secs + mins * 60 + hors * 3600
    return (days, secs_total)
