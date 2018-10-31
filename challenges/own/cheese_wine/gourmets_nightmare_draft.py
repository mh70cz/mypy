#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gourmets' nightmare

A lot of gourmets struggle to find the perfect match of wine and cheese. 
A number of considerations are relevant, where each of them creates 
the unique combination, so finding the perfect match 
is a long-time assignment. 
Your assignment is not supposed to be long-time but it will use original but
scarry matching criteria.

1. criterion
Single-word wine names can be paired with single-word cheese names only, 
where a word separator is  space " " or dash "-".

2. criterion
Similarity of a letter frequency in a name of wine and cheese. 

             sum of occuremce of chars shared by both words
similarity = ------------------------------------------------
             1 + square of length difference of both words


Upper and lower case does not distinquish.
Space " ", dash "-", and aposthrope "'" 
are not considered as a char.



43 cheeses are mentioned in the in the "Cheese Shop" sketch 
(from Monty Python's Flying Circus)
http://montypython.wikia.com/wiki/Cheese_Shop_sketch

https://stackoverflow.com/questions/44012479/intersection-of-two-counters
"""

from collections import Counter
import operator

cheeses_43 = [
    'Red Leicester',
    'Tilsit',
    'Caerphilly',
    'Bel Paese',
    'Red Windsor',
    'Stilton',
    'Emmental',
    'Gruyère',
    'Norwegian Jarlsberg',
    'Liptauer',
    'Lancashire',
    'White Stilton',
    'Danish Blue',
    'Double Gloucester',
    'Cheshire',
    'Dorset Blue Vinney',
    'Brie',
    'Roquefort',
    "Pont l'Evêque",
    'Port Salut',
    'Savoyard',
    'Saint-Paulin',
    "Carré de l'Est",
    'Bresse-Bleu',
    'Boursin',
    'Camembert',
    'Gouda',
    'Edam',
    'Caithness',
    'Smoked Austrian',
    'Japanese Sage Derby',
    'Wensleydale',
    'Greek Feta',
    'Gorgonzola',
    'Parmesan',
    'Mozzarella',
    'Pipo Crème',
    'Danish Fynbo',
    "Czech sheep's milk",
    'Venezuelan Beaver Cheese',
    'Cheddar',
    'Ilchester',
    'Limburger']

red_wines = ["Châteauneuf-du-Pape", #95% of production is red
        "Syrah", "Merlot", "Cabernet sauvignon",
             "Malbec", "Pinot noir", "Zinfandel", "Sangiovese", "Barbera",
             "Barolo", "Rioja", "Garnacha"]

white_wines = ["Chardonnay", "Sauvignon blanc", "Semillon", "Moscato",
               "Pinot grigio", "Gewürztraminer", "Riesling"]

sparkling_wines = ["Cava", "Champagne", "Crémant d’Alsace", 
                   "Moscato d’Asti", "Prosecco", "Franciacorta", "Lambrusco"]


wines = red_wines + white_wines + sparkling_wines


#c_single = [c.lower() for c in cheeses_43 if (c.find(" ") == -1) and (c.find("-") == -1)]
#w_single = [w.lower() for w in wines if (w.find(" ") == -1) and (w.find("-") == -1)]


w_c = []
for c in cheeses_43:
    cc = Counter(c.lower())
    for w in wines:
        wc = Counter(w.lower())
        cc_wc = cc & wc
        square_len_diff = (len(c) - len(w))**2 
        similarity = sum([cc_wc[i] for i in cc_wc]) / ( 1 + square_len_diff )
        w_c.append((w, c, cc, wc, similarity))

w_c_srt = sorted(w_c, key = operator.itemgetter(0, 4))    

matches_wine_5cheeses = []
len_w = len(wines)
len_c = len(cheeses_43)

for i in range(0, len_c * len_w, len_c):
    w = w_c_srt[i][0]
    cheeses_5 = []
    for j in range(i+len_c -1 , i+len_c - 6, -1):
        cheeses_5.append(w_c_srt[j][1])
    matches_wine_5cheeses.append((w, cheeses_5))
    
wine_type = "sparkling"
wine_types = {"white": white_wines, "red": red_wines, "sparkling": sparkling_wines}
best_match = (None, None, None, None, 0)
for pair in w_c_srt:
    if pair[0] in wine_types[wine_type]:
        if pair[4] > best_match[4]:
            best_match = pair
            
        

    
        