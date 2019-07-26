"""
Bite 168. Ninja Rankings
"""

from dataclasses import dataclass
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int
    
    def __gt__(self, other):
        return self.bites > other.bites
    
    def __lt__(self, other):
        return(self.bites < other.bites)
    
    def __eq__(self, other):
        return(self.bites == other.bites)
        
    def __str__(self):
        return f"[{self.bites}] {self.name}"


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """

    
    def __post_init__(self):
        self._ninjas: List[Ninja] = list()
        

    def add(self,ninja):
        self._ninjas.append(ninja)
        self._ninjas.sort(reverse=True)

        
    def dump(self):
        del self._ninjas[-1]
    
    def highest(self, n=1):
        return self._ninjas[:n]
    
    def lowest(self, n=1):
        return self._ninjas[-n:]
    
    def __len__(self):
        return len(self._ninjas)
    
    def pair_up(self, n=1):
        possible_pairs = len(self._ninjas) // 2
        print(f"num of possible pairs: {possible_pairs}")
        if possible_pairs < 1:
            return None
        pairs = []
        for i in range(possible_pairs):
            if i > n-1:
                break
            pairs.append((self._ninjas[i], self._ninjas[-i-1]))
        return pairs            
    
        
"""
a = Ninja("a", 2)
b = Ninja("b", 50)
c = Ninja("c", 22)
d = Ninja("d", 28)
e = Ninja("e", 12)
f = Ninja("f", 2)
g = Ninja("g", 112)
h = Ninja("h", 1)


r = Rankings()
r.add(a)
r.add(b)
r.add(c)
r.add(d)
r.add(e)
r.add(f)
r.add(g)
r.add(h)

r._ninjas


"""    
    
    