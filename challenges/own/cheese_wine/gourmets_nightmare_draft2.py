#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pair wines and cheeses by similarity of wine name and cheese name.

             sum of occuremce of chars shared by both words
similarity = ------------------------------------------------
             1 + square of length difference of both words

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


def _match_sort():

    wines = red_wines + white_wines + sparkling_wines
    wi_ch_pairs = []
    for c in cheeses_43:
        c_cnt = Counter(c.lower())
        for w in wines:
            w_cnt = Counter(w.lower())
            c_cnt_w_cnt = c_cnt & w_cnt
            square_len_diff = (len(c) - len(w))**2 
            similarity = sum([c_cnt_w_cnt[i] for i in c_cnt_w_cnt]) / ( 1 + square_len_diff )
            wi_ch_pairs.append((w, c, c_cnt, w_cnt, similarity))
    
    return sorted(wi_ch_pairs, key = operator.itemgetter(0, 4))    

def match_wine_5cheeses(wi_ch_pairs_srt = _match_sort()):
    matches_wine_5cheeses = []
    len_c = len(cheeses_43)
    
    for i in range(0, len(wi_ch_pairs_srt), len_c):
        w = wi_ch_pairs_srt[i][0]
        cheeses_5 = []
        for j in range(i+len_c -1 , i+len_c - 6, -1):
            cheeses_5.append(wi_ch_pairs_srt[j][1])
        matches_wine_5cheeses.append((w, cheeses_5))
    return matches_wine_5cheeses
    
def best_match_per_wine(wi_ch_pairs_srt = _match_sort(), wine_type="all"):

    wine_types = {"white": white_wines, "red": red_wines, "sparkling": sparkling_wines}
    best_match = (None, None, None, None, 0)
    for pair in wi_ch_pairs_srt:
        if pair[0] in wine_types[wine_type]:
            if pair[4] > best_match[4]:
                best_match = pair
    return best_match
            
mwc = match_wine_5cheeses()
bm = best_match_per_wine(wine_type="white")        

    
        