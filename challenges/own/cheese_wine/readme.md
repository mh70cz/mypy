# Gourmets' nightmare

A lot of gourmets struggle to find the perfect match of wine and cheese. 
A number of considerations are relevant, where each of them creates 
the unique combination, so finding the perfect match is a long-time assignment.  
Your assignment is not supposed to be long-time but it will use original but
weird and scary matching criteria.

You will match by similarity of cheese and wine name, where the name similarity is defined as follows:

```
             sum of values of intersection of char counters of names
similarity = ―――――――――――――――――――――――――――――――――――――――――――――――――――――――
             1 + square of length difference of both words
```
Upper and lower case variants are ignored in the mathing process.  
Space " ", dash "-", and aposthrope "'" are considered as valid chars.

Examples:  
'house' 'mouse'            -> {'e': 1, 'o': 1, 's': 1, 'u': 1}  -> 4 / (1 + (5 - 5)**2) = 4  
'parapraxis' 'explanation' -> {'a': 2, 'i': 1, 'p': 1, 'x': 1}  -> 5 / (1 + (10 - 11)**2) = 2.5  
'parapraxis' 'parallax'    -> {'a': 3, 'p': 1, 'r': 1, 'x': 1}  -> 6 / (1 + (10 - 8)**2 ) = 1.2  
'roosters-do-sound' 'cocka-doodle-doo' -> {'-': 2, 'd': 2, 'e': 1, 'o': 4} -> 9 / (1 + (17-16)**2) = 4.5  
'Cabernet sauvignon' 'Dorset Blue Vinney' ->  
{'e': 2, 'n': 2, 'o': 1, 'r': 1, 's': 1, 't': 1, ' ': 1, 'b': 1, 'u': 1, 'v': 1, 'i': 1} -> 13 / (1 + (18 - 18)**2) = 13


3 lists of wine are provided (red, white, sparkling).  
You will match them with 43 cheeses mentioned in the in the "Cheese Shop" sketch  
(from Monty Python's Flying Circus  http://montypython.wikia.com/wiki/Cheese_Shop_sketch )
  
---
### Tasks
1\. Complete the method *best_match_per_wine* which returns the best scored wine-cheese pair.
Matching can be for a certain wine type (i.e. red, white, sparkling) or for all types.
For an invalid wine type raise ValueError.

2\. Complete the method *match_wine_5cheeses* which returns a sorted list of wines , where for each wine are listed 5 best matching cheeses.  
All types of wines (i.e. red, white, and sparkling) are included.  
List of cheeses is sorted by score descending then alphabetically ascending.  
Output example:
```
[
('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
...
...
('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
]
```
---


Keywords: Counter intersection, Operator, Multi key sort



