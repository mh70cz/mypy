'''Bite 5. Parse a list of names'''
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    names = set(NAMES)
    return [x.title() for x in names]


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names, key = lambda x: x.split(" ")[1], reverse = True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    # return sorted(names, key = lambda x: x.split(" ")[0])[0].split(" ")[0]
    return sorted([name.split(" ")[0] for name in names],
                   key = lambda x: len(x))[0]



names = dedup_and_title_case_names(NAMES)
assert names.count('Bob Belderbos') == 1
assert names.count('julian sequeira') == 0
assert names.count('Brad Pitt') == 1
assert len(names) == 10
assert all(n.title() in names for n in NAMES)



names = sort_by_surname_desc(NAMES)
assert names[0] == 'Julian Sequeira'
assert names[-1] == 'Alec Baldwin'


assert shortest_first_name(NAMES) == 'Al'