"""
Bite 20. Write a context manager 

https://codechalleng.es/bites/20
"""
             
class Account:

    
    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        if self.balance < 0:
            del self._transactions[-1]
            
#    solutions from pybites - better            
#    def __enter__(self):
#        self._copy_transactions = list(self._transactions)
#        return self
#
#    def __exit__(self, exc_type, exc_val, exc_tb):
#        if self.balance < 0:
#            print('Balance below 0, rolling back transaction')
#            self._transactions = self._copy_transactions            
#        

import pytest



@pytest.fixture()
def account():
    return Account()


def test_balance(account):
    assert account.balance == 0
    account + 10
    assert account.balance == 10
    account - 5
    assert account.balance == 5


def test_without_contextman_balance_negative(account):
    assert account.balance == 0
    account - 5
    assert account.balance == -5


def test_with_contextman_performs_rollback(account):
    assert account.balance == 0
    with account as acc:
        acc - 5
    assert account.balance == 0
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          