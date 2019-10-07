# -*- coding: utf-8 -*-
"""
Bite 220. Analysing @pythonbytes RSS feed
"""
from collections import namedtuple, Counter
import re
from typing import NamedTuple
from time import strftime, gmtime



import feedparser

SPECIAL_GUEST = 'Special guest'

# using _ as min/max are builtins
Duration = namedtuple('Duration', 'avg max_ min_')

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = 'http://projects.bobbelderbos.com/pcc/python_bytes'
IGNORE_DOMAINS = {'https://pythonbytes.fm', 'http://pythonbytes.fm',
                  'https://twitter.com', 'https://training.talkpython.fm',
                  'https://talkpython.fm', 'http://testandcode.com'}


class PythonBytes:

    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(URL)["entries"]

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        episodes = []
        for entry in self.entries:
            summary = entry["summary"]
            domains_raw = re.findall("https?://[^/\"]+", summary)
            domains = [x.split("//")[1] for x in domains_raw]
            if domain in domains:
                episodes.append(entry["itunes_episode"])
        return episodes
            
        
    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """   
        domains =[]
        for e in self.entries:
            summary = e["summary"]
            domains.extend(set(re.findall('https?://[^/]+', summary)))
        domains = [x for x in domains if x not in IGNORE_DOMAINS] 
        c_domain = Counter(domains)
        return c_domain.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        cnt = 0
        for e in self.entries: 
            summary = e["summary"]
            if SPECIAL_GUEST in summary:
                cnt += 1
        return cnt   

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """       
        durations = []
        for e in self.entries: 
            dur_raw = e["itunes_duration"]
            dur = sum([a*b for a,b in zip([3600,60,1], [int(i) for i in dur_raw.split(":")])])
            durations.append(dur)
        dur_min = min(durations)
        dur_max = max(durations)
        dur_avg = sum(durations)/len(durations)
        d = Duration(int(dur_avg), strftime("%H:%M:%S", gmtime(dur_max)), strftime("%H:%M:%S", gmtime(dur_min)))
        return d
        
    
