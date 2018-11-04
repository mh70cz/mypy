# -*- coding: utf-8 -*-
"""
Bite 41. Write a login_required decorator
https://codechalleng.es/bites/41/
decorator
Created on Thu Jul 19  2018 ;  


"""
from functools import wraps

known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']


def login_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user in known_users:
            return "please create an account"
        
        if not user in loggedin_users:
            return "please login"
        
        return func(user, *args, **kwargs)
        
    return wrapper


@login_required
def welcome(user):
    '''Return a welcome message if logged in'''
    return f"welcome back {user}"
    





def test_no_account():
    """User is not on the system"""
    assert welcome('anonymous') == 'please create an account'


def test_not_loggedin():
    """User is on the system but not logged in"""
    assert welcome('julian') == 'please login'


def test_loggedin():
    """User is on the system and logged in"""
    assert welcome('sue') == 'welcome back sue'


def test_docstring():
    """Decorator should not lose function's docstring"""
    assert welcome.__doc__ == 'Return a welcome message if logged in'