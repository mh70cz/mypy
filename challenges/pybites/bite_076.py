"""
Bite 76. The singledispatch countdown challenge 


https://codechalleng.es/bites/076
"""

from functools import singledispatch

#data_type = '1234'
#data_type = [1, 2, 3, 4]
#data_type = ["1", "2", "3", "4"]
#data_type = (1, 2, 3, 4)
#data_type = ("1", "2", "3", "4")
#data_type = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
#data_type = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}
#data_type = {x for x in range(1, 5)}
#data_type = range(1, 5)
#data_type = 1234
data_type = 12.34

@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    #print(f'({type(data_type).__name__}) {data_type}')
    raise ValueError


@count_down.register(str)
def _(data_type):
    for i in range(len(data_type),0,-1):
        print(data_type[:i])


#@count_down.register(list)
#@count_down.register(tuple)
#def _(data_type):
#    for i in range(len(data_type),0,-1):
#        strings = map(str,data_type[:i])
#        print("".join(strings))

@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(dict)
@count_down.register(range)
def _(data_type):
    strings = [str(x) for x in data_type]
    for i in range(len(strings),0,-1):
        print("".join(strings[:i]))
            
@count_down.register(int)
@count_down.register(float)
def _(data_type):
    string = str(data_type)
    for i in range(len(string),0,-1):
        print(string[:i])



if __name__ == "__main__":
    count_down(data_type)    