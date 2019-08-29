"""
Bite 178. Parse PyBites blog git commit log
"""

from collections import Counter
import os
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join('/tmp', 'commits')
urlretrieve('https://bit.ly/2H1EuZQ', commits) 

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = '{y}-{m:02d}'


def get_min_max_amount_of_commits(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    
    with open(commit_log) as f:
        lines = f.readlines()
    
    date_changes = []
    cnt = Counter()
    for line in lines:
        date_raw, changes_raw = line.split("|")
        date = _parse_date(date_raw)
        changes = _parse_changes(changes_raw)
        if year is not None:
            if year != date.year:
                continue
        ym = YEAR_MONTH.format(y=date.year, m=date.month)
        date_changes.append((ym, changes))
        cnt[ym] += changes
    return (cnt.most_common()[-1][0], cnt.most_common()[0][0])
        

def _parse_date(date_raw):
    date_raw = date_raw[8:].rstrip()
    date = parse(date_raw)
    return date

def _parse_changes(changes_raw):
    insertions = deletions = 0
    insdel = changes_raw.split(",")
    for chunk in insdel:
        if "insertion" in chunk:
            insertions = chunk.strip().split(" ")[0]
            insertions = int(insertions)
        elif "deletion" in chunk:
            deletions = chunk.strip().split(" ")[0]
            deletions = int(deletions)
    changes = insertions + deletions
    return changes





def get_min_max_amount_of_commits_orig(commit_log: str = commits,
                                  year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    
    with open(commit_log) as f:
        lines = f.readlines()
    
    date_changes = []
    cnt = Counter()
    for line in lines:
        date_raw, changes_raw = line.split("|")
        date = _parse_date(date_raw)
        changes = _parse_changes(changes_raw)
        date_changes.append((date, changes))
    
    for dc in date_changes:
        if year is not None:
            if year != dc[0].year:
                continue
        ym = YEAR_MONTH.format(y=dc[0].year, m=dc[0].month)
        cnt[ym] += dc[1]
    return (cnt.most_common()[-1][0], cnt.most_common()[0][0])
        
