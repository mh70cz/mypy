"""
Bite 63. Use an infinite iterator to simulate a traffic light 


https://codechalleng.es/bites/063
"""

from collections import namedtuple
from itertools import cycle, islice
from time import sleep

State = namedtuple('State', 'color command timeout')


def traffic_light():
    """Returns an itertools.cycle iterator that
       when iterated over returns State namedtuples
       as shown in the Bite's description"""
       
    red_state = State("red", "Stop", 2)
    amber_state = State("amber", "Caution", 0.5)
    green_state = State("green", "Go", 2)
    states = cycle([red_state, green_state, amber_state])
    return states

if __name__ == '__main__':
    # print a sample of 10 states if run as standalone program
    for state in islice(traffic_light(), 10):
        print(f'{state.command}! The light is {state.color}')
        sleep(state.timeout)
            
            
            


    