"""
@author: mh70; 2018-07-17; Bite 33. Transpose a data structure  
https://codechalleng.es/bites/33/ 

zip, transpose
"""

from collections import namedtuple

POSTS = {'2017-8': 19, '2017-9': 13, '2017-10': 13,
         '2017-11': 12, '2017-12': 11, '2018-1': 3}
NAMES = ['Bob', 'Julian', 'Tim', 'Carmen', 'Henk', 'Sofia', 'Bernard']

Member = namedtuple('Member', 'name since_days karma_points bitecoin_earned')

def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data2 = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if isinstance(data, dict):
        return [data.keys(), data.values()] #solution from PyBites
        
        # return list(zip(*[(p, data[p]) for p in data]))
  
    
    if isinstance(data, list):
        return(*data) #solution from PyBites
        # return list(zip(*[[dd for dd in d] for d in data]))
    

    



"""

        lx = []
        ly = []
        for d in data:
            lx.append(d)
            ly.append(POSTS[d])
        return [tuple(lx), tuple(ly)]  




        l = []
        for d in data:
            ll = []
            for e in d:
                ll.append(e)
            l.append(ll)
        return list(zip(*l))


    if type(data) == list:
        l = []
        num_f = len(Member._fields)
        for f in range(num_f):
            l.append([None]*len(data))
        for i in range(len(data)):
            for f in range(num_f):
                l[f][i]= data[i][f]
        out_l = []
        for f in range(num_f):
            out_l.append(tuple(l[f]))
        return out_l
"""        
