"""
Bite 60. Create a deck of Uno cards 

https://codechalleng.es/bites/60
"""


from collections import namedtuple

SUITS = 'Red Green Yellow Blue'.split()
NAMES_2 = "1, 2, 3, 4, 5, 6, 7, 8, 9, Draw Two, Skip, Reverse".split(", ")
WILD_4 = "Wild, Wild Draw Four".split(", ")

UnoCard = namedtuple('UnoCard', 'suit name')


def create_uno_deck():
    """Create a deck of 108 Uno cards.
       Return a list of UnoCard namedtuples
       (for cards w/o suit use None in the namedtuple)"""
    deck = []
    for suit in SUITS:
        deck.append(UnoCard(suit, "0"))
        for i in range(2):
            for name in NAMES_2:
                deck.append(UnoCard(suit, name))
    for i in range(4):
        for name in WILD_4:
            deck.append(UnoCard(None, name))
    return deck       
            
    
import pytest


def _count_suits(deck, suit):
    return len([card for card in deck if card.suit == suit])


def _count_suitcard(deck, suit, name):
    return sum(1 for card in deck if card.suit == suit
               and str(card.name) == name)


@pytest.fixture(scope="module")
def deck():
    return create_uno_deck()


def test_create_uno_deck_len(deck):
    assert len(deck) == 108


def test_create_uno_deck_type(deck):
    assert type(deck) == list
    assert all(type(card) == UnoCard for card in deck)


@pytest.mark.parametrize("suit, count", [
    ('Red', 25),
    ('Green', 25),
    ('Yellow', 25),
    ('Blue', 25),
    (None, 8),  # wild cards don't have an associated suit
])
def test_create_uno_deck_suit_distribution(deck, suit, count):
    assert _count_suits(deck, suit) == count


@pytest.mark.parametrize("name, count", [
    ('0', 1), ('1', 2), ('2', 2), ('3', 2), ('4', 2),
    ('5', 2), ('6', 2), ('7', 2), ('8', 2), ('9', 2),
    ('Draw Two', 2), ('Skip', 2), ('Reverse', 2),
])
def test_create_uno_deck_suit_cards(deck, name, count):
    for suit in SUITS:
        _count_suitcard(deck, suit, name) == count
        
#import sys
#if __name__ == '__main__':
#    pytest.main(sys.argv)          