"""
Bite 72. Retrieve the right Ninja Belt based on score 
https://codechalleng.es/bites/72/

Created on  2018-08-10

"""
from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    
    if user_score < MIN_SCORE:
        return None
    if user_score >= MAX_SCORE:
        return "red"
    last_key = None
    for k in HONORS:
        if user_score < k:
            return HONORS[last_key]
        else:
            last_key = k            
    
        



import pytest




@pytest.mark.parametrize("input_argument, expected_return", [
    (0, None),
    (9, None),
    (10, 'white'),
    (48, 'white'),
    (50, 'yellow'),
    (101, 'orange'),
    (249, 'green'),
    (250, 'blue'),
    (251, 'blue'),
    (400, 'brown'),
    (599, 'brown'),
    (600, 'black'),
    (788, 'black'),
    (800, 'paneled'),
    (999, 'paneled'),
    (1000, 'red'),
    (1200, 'red'),
])
def test_get_belt(input_argument, expected_return):
    assert get_belt(input_argument) == expected_return


#import sys
#if __name__ == '__main__':
#    pytest.main(sys.argv)             