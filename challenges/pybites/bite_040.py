"""
 Bite 34. Building a Karma app - implement the User class 

https://codechalleng.es/bites/31
"""
 
def binary_search(sequence, target):
    
    s_len = len(sequence)
    low = 0
    mid = s_len//2
    high = s_len
    i = 0
    print(F"{target}  :")
    print(low, mid, high)
    while mid != low:
        if i > len(sequence): break;
        i += 1
        if sequence[mid] == target:
            return mid
        if sequence[mid] > target:
            high = mid            
        else:
            low = mid
        mid = (high - low)//2 + low
        print(low, mid, high)
    if mid == 0:
        if sequence[0] == target:
            return 0
    return None
        
    

import pytest

from string import ascii_lowercase



PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
EVENS = [0,2,4,6,8,10,12,14,16,18, 20]
ODDS = [1,3,5,7,9,11,13,17,19,21,23,25]
ALPHABET = list(ascii_lowercase)


def test_binary_search_prime():
    assert binary_search(PRIMES, 2) == 0
    assert binary_search(PRIMES, 3) == 1
    assert binary_search(PRIMES, 5) == 2
    assert binary_search(PRIMES, 53) == 15
    assert binary_search(PRIMES, 59) == 16
    assert binary_search(PRIMES, 5) == 2
    assert binary_search(PRIMES, 61) == 17
    assert binary_search(PRIMES, 18) == None
    assert binary_search(PRIMES, 16) == None
    assert binary_search(PRIMES, 1) == None
    assert binary_search(PRIMES, 0) == None
    assert binary_search(PRIMES, -1) == None
    assert binary_search(PRIMES, 62) == None
    
def test_binary_search_even():
    for idx, num in enumerate(EVENS):
        assert binary_search(EVENS, num) == idx
    for idx, num in enumerate(ODDS):
        assert binary_search(EVENS, num) == None
        
def test_binary_search_odd():
    for idx, num in enumerate(ODDS):
        assert binary_search(ODDS, num) == idx
    for idx, num in enumerate(EVENS):
        assert binary_search(ODDS, num) == None
        

    


def test_binary_search_alpha():
    assert binary_search(ALPHABET, 'u') == 20
    assert binary_search(ALPHABET, 'a') == 0
    assert binary_search(ALPHABET, 'z') == 25

import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          
    
#python -m pytest xxx_test.py
    