"""
Bite 189. Filter a list of names
"""

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    #filtered_names = []
    count = 0
    for name in names:
        if name[0] in IGNORE_CHAR:
            continue
        if any([x.isnumeric() for x in name]):
            continue
        if name[0] in QUIT_CHAR:
            break
        #if len(filtered_names) == 5:
        #    break
        #filtered_names.append(name)
        if count == MAX_NAMES:
            break
        count += 1
        yield name
    #return filtered_names
        