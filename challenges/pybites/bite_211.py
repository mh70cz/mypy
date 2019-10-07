# -*- coding: utf-8 -*-
"""
Bite 211. Write a retry decorator
"""

from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):
        retries = 0
        while retries < MAX_RETRIES:
            try:
                func(*args, **kwargs)
                return
            except Exception as exc:                      
                retries +=1
                print(exc)
                continue
        raise MaxRetriesException
    return wrapper  
    