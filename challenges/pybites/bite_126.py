"""
Bite 126. The Emoji (Unicode) Bite 

https://codechalleng.es/bites/126

"""
 
import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate
STOP_EMOJI_RANGE = sys.maxunicode
#START_EMOJI_RANGE = 127748 # sunrise over mountains
#STOP_EMOJI_RANGE = 128526  # smiling face with sunglasses 128526

def what_means_emoji(emoji):
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except (TypeError, ValueError):
        return 'Not found'


def _make_emoji_mapping():
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""

    for i in range(START_EMOJI_RANGE, STOP_EMOJI_RANGE + 1):
        char = chr(i)
        try:
            u_name = what_means_emoji(char).lower()
            yield (char, u_name)
        except ((TypeError, ValueError)):
            continue
        


def find_emoji(term):
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()

    emoji_mapping = _make_emoji_mapping()
    
    for k, v in emoji_mapping:
        if term in v:
            print(k + v)
    

    