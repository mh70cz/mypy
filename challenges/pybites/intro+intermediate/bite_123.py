"""
Bite 123. Find the user with most friends 

https://codechalleng.es/bites/123
"""
from collections import Counter

names = 'bob julian tim martin rod sara joyce nick beverly kevin'.split()
ids = range(len(names))
users = dict(zip(ids, names))  # 0: bob, 1: julian, etc

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
               (3, 4), (4, 5), (5, 6), (5, 7), (5, 9),
               (6, 8), (7, 8), (8, 9)]


def get_friend_with_most_friends(friendships=friendships):
    """Receives the friendships list of user ID pairs,
       parse it to see who has most friends, return a tuple
       of (name_friend_with_most_friends, his_or_her_friends)"""
    c = Counter()
    for t in friendships:
        c[t[0]] += 1
        c[t[1]] += 1
    has_most_f_id = c.most_common(1)[0][0]
    f_ids = []
    for t in friendships:
        if t[0] == has_most_f_id:
            f_ids.append(names[t[1]])
        if t[1] == has_most_f_id:
            f_ids.append(names[t[0]])
    return (names[has_most_f_id], f_ids)
    
                
import pytest

def test_get_friend_with_most_friends_default_arg():
    user, friends = get_friend_with_most_friends()
    assert user == 'sara'
    assert sorted(list(friends)) == ['joyce', 'kevin', 'nick', 'rod']


def test_get_friend_with_most_friends_different_friendship_data():
    friendships = [(0, 1), (0, 2), (1, 2), (1, 6), (2, 3),
                   (3, 4), (4, 6), (5, 6), (5, 7), (5, 9),
                   (6, 7), (6, 8), (6, 9)]
    user, friends = get_friend_with_most_friends(friendships)
    assert user == 'joyce'
    assert sorted(list(friends)) == ['beverly', 'julian', 'kevin', 'nick',
                                     'rod', 'sara']
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          