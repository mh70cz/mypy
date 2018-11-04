"""
 Bite 70. Create your own iterator 
https://codechalleng.es/bites/71/

Created on  2018-08-10

"""
class RecordScore:
    """Class to track a game's maximum score"""
    
    def __init__(self):
        self.record = 0
    
    def __call__(self, score):
        if score > self.record:
            self.record = score
        return (self.record)
            
    
        



import pytest

@pytest.fixture()
def record():
    """Make a RecordScore object with a few scores"""
    record = RecordScore()
    record(10)
    record(9)
    record(11)  # initial max
    record(5)
    return record


def test_record_unbeaten(record):
    assert record(9) == 11
    record(10)
    record(2)
    assert record(4) == 11


def test_record_got_beaten(record):
    assert record(4) == 11
    record(3)
    record(12)  # new record
    assert record(4) == 12
    record(5)
    record(16)  # another record
    assert record(4) == 16


#import sys
#if __name__ == '__main__':
#    pytest.main(sys.argv)             