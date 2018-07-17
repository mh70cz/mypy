# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 09:37:46 2018; @author: mh70
Bite 19. Write a simple property
"""

from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, s, d):
        self.s = s
        self.d = d

    @property
    def expired(self):
        if self.d < NOW:
            return True
        else:
            return False


"""
from datetime import timedelta

from simple_property import Promo, NOW


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired

"""
