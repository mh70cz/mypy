# -*- coding: utf-8 -*-
"""
Bite 222. Split an iterable in groups of size n 
"""

import types
from itertools import islice


def group(iterable, n):
    """Splits an iterable set into groups of size n and a group
       of the remaining elements if needed.

       Args:
         iterable (list): The list whose elements are to be split into
                          groups of size n.
         n (int): The number of elements per group.

       Returns:
         list: The list of groups of size n,
               where each group is a list of n elements.
    """
    src = list(iterable)
    i = iter(src)
    num_std_groups = len(src)//n
    last_grp_size = len(src)%n
    out = []
    
    for j in range(num_std_groups):
        grp = []
        for k in range(n):
            grp.append(next(i))
        out.append(grp)
    grp = []        
    if last_grp_size > 0:
        for j in range (last_grp_size):
            grp.append(next(i))    
        out.append(grp)
    return out



if __name__ == '__main__':
    iterable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = 3
    ret = group(iterable, n)
    print(ret)
    
"""
    src = list(iterable)
    i = iter(src)
    num_std_groups = len(src)//n
    last_grp_size = len(src)%n
    out = []
    
    for j in range(num_std_groups):
        grp = []
        for k in range(n):
            grp.append(next(i))
        out.append(grp)
    grp = []        
    if last_grp_size > 0:
        for j in range (last_grp_size):
            grp.append(next(i))    
        out.append(grp)
    return out
    
    src = list(iterable)
    i = islice(src, n)
    num_std_groups = len(src)//n
    last_grp_size = len(src)%n
    out = []
    for j in range(num_std_groups):
        out.append(islice(i, n))
    if last_grp_size > 0:
        out.append(islice(i, last_grp_size))
      

    return out    
    
    
    
    
"""    