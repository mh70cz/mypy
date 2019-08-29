# -*- coding: utf-8 -*-
"""
Bite 171. Make a terminal spinner animation
"""

from itertools import cycle
import sys
from time import time, sleep

SPINNER_STATES = ['-', '\\', '|', '/']  # had to escape \
STATE_TRANSITION_TIME = 0.1


def spinner(seconds):
    """Make a terminal loader/spinner animation using the imports aboveself.
       Takes seconds argument = time for the spinner to runself.
       Does not return anything, only prints to stdout."""
    time_start = time()
    for c in cycle(SPINNER_STATES):
        if time() >= (time_start + seconds):
            break
        sleep(STATE_TRANSITION_TIME)
        print("\r" + c , end="", flush=True)

            
            



if __name__ == '__main__':
    spinner(2)
    
    
#def spinner(seconds):
#    """Make a terminal loader/spinner animation using the imports aboveself.
#       Takes seconds argument = time for the spinner to runself.
#       Does not return anything, only prints to stdout."""
#    time_start = time()
#    for c in cycle(SPINNER_STATES):
#        print(c, end="", flush=True)
#        sleep(STATE_TRANSITION_TIME)
#        print("\b", end="", flush=True)
#        if time() > time_start + seconds:
#            break    