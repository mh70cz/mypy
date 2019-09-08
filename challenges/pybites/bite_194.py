"""
Bite 194. Add caching to a Fibonacci function
"""

from functools import lru_cache

@lru_cache()
def cached_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return cached_fib(n-2) + cached_fib(n-1)
    
    