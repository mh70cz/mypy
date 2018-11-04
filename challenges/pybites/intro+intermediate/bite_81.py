"""
 Bite 81. Filter and order tweets by polarity values 

https://codechalleng.es/bites/81
"""

from collections import namedtuple

Tweet = namedtuple('Tweet', 'text polarity')

# polarity < 0 = negative, > 0 = positive
# long strings and pep8: you can wrap strings in () to reduce line length
tweets = [
    Tweet(text=("It's shocking that the vast majority of online banking "
                "systems have critical vulnerabilities leaving customer "
                "accounts unprotected."),
          polarity=-0.3333333333333333),
    Tweet(text=("The most unbelievable aspect of the Star Trek universe "
                "is that every ship they meet has compatible video "
                "conferencing facilities."),
          polarity=0.125),
    Tweet(text=("Excellent set of tips for managing a PostgreSQL cluster "
                "in production."),
          polarity=1.0),
    Tweet(text=("This tutorial has a great line-by-line breakdown of how "
                "to train a pong RL agent in PyTorch."),
          polarity=0.8),
    Tweet(text="This is some masterful reporting by ... It's also an "
               "infuriating story. ... is trying to erase debt by preying "
               "on the city’s residents. The poorest get hit the worst. "
               "It’s shameful.",
          polarity=-0.19999999999999998),
]


def filter_tweets_on_polarity(tweets, keep_positive=True):
    """Filter the tweets by polarity score, receives keep_positive bool which
       determines what to keep. Returns a list of filtered tweets."""
    return [t for t in tweets if (t.polarity  > 0 
                                  if keep_positive else t.polarity < 0)]


def order_tweets_by_polarity(tweets, positive_highest=True):
    """Sort the tweets by polarity, receives positive_highest which determines
       the order. Returns a list of ordered tweets."""
    return sorted(tweets, key = lambda t: t.polarity, 
                  reverse = (True if positive_highest else False))
    
import pytest
def test_filter_tweets_keep_positive():
    actual = filter_tweets_on_polarity(tweets)
    expected = tweets[1:4]
    assert actual == expected


def test_filter_tweets_keep_negative():
    actual = filter_tweets_on_polarity(tweets, keep_positive=False)
    expected = [tweets[0], tweets[-1]]
    assert actual == expected


def test_order_tweets_positive_highest():
    actual = [tweet.polarity for tweet in order_tweets_by_polarity(tweets)]
    expected = [1.0, 0.8, 0.125, -0.19999999999999998,
                -0.3333333333333333]
    assert actual == expected


def test_order_tweets_negative_highest():
    actual = [tweet.polarity for tweet in
              order_tweets_by_polarity(tweets, positive_highest=False)]
    expected = [-0.3333333333333333, -0.19999999999999998,
                0.125, 0.8, 1.0]
    assert actual == expected

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          