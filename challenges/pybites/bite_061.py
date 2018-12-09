"""
Bite 61. Create a variable size Paw Patrol card deck with random actions


https://codechalleng.es/bites/061
"""

from collections import namedtuple
import random
from string import ascii_uppercase
from itertools import cycle

ACTIONS = ['draw_card', 'play_again',
           'interchange_cards', 'change_turn_direction']
NUMBERS = range(1, 5)

PawCard = namedtuple('PawCard', 'card action')

def create_paw_deck(n=8):
    if n > 26:
        raise ValueError      
        
    c_actions = cycle(ACTIONS)    
    rs = random.sample(range(n*4),n)
    letters = ascii_uppercase[:n]
    card_no = 0
    deck = []
    for n in NUMBERS:
        for l in letters:
            if card_no in rs:
                action = next(c_actions)
            else:
                action = None
            deck.append(PawCard(l+str(n) , action))
            card_no += 1
    return deck
            
            
            

#if __name__ == "__main__":
#     

    