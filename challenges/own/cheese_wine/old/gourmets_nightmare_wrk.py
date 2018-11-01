#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.

"""

from collections import Counter
import operator

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _score(wine_type="all"):
    """ scores wine-cheese pairs by similiarity of names
                 sum of values of intersection of char counters of names
    similarity = -------------------------------------------------------
                 1 + square of length difference of names
    returns a list of tuples, where each tuple contains: cheese, wine, score
    """
    wine_types = {"white": WHITE_WINES, "red": RED_WINES, "sparkling": SPARKLING_WINES}
    if wine_type == "all":
        wines = RED_WINES + WHITE_WINES + SPARKLING_WINES
    else:
        if wine_type not in wine_types.keys():
            raise ValueError("unrecognized wine type")
        wines = wine_types[wine_type]
    wi_ch_pairs = []
    for cheese in CHEESES:
        ch_cnt = Counter(cheese.lower())
        for wine in wines:
            wi_cnt = Counter(wine.lower())
            wi_cnt_ch_cnt = wi_cnt & ch_cnt
            square_len_diff = (len(cheese) - len(wine)) ** 2
            similarity = sum(wi_cnt_ch_cnt.values()) / (1 + square_len_diff)
            # ToDo remove diagnostic wi_cnt, ch_cnt + modify test
            wi_ch_pairs.append((wine, cheese, similarity, wi_cnt, ch_cnt))
    return wi_ch_pairs


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest score
    returns a tuple which contains wine, cheese, score
    """
    return sorted(_score(wine_type), key=lambda x: x[2])[-1]


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses
    """
    wi_ch_pairs_srt = sorted(_score(), key=operator.itemgetter(0, 2))
    matches_wine_5cheeses = []
    len_c = len(CHEESES)

    for i in range(0, len(wi_ch_pairs_srt), len_c):
        w = wi_ch_pairs_srt[i][0]
        cheeses_5 = []
        for j in range(i + len_c - 1, i + len_c - 6, -1):
            cheeses_5.append(wi_ch_pairs_srt[j][1])
        matches_wine_5cheeses.append((w, cheeses_5))
    return matches_wine_5cheeses


# ToDo remove
mwc = match_wine_5cheeses()
bmw = best_match_per_wine(wine_type="white")
bmr = best_match_per_wine(wine_type="red")
bms = best_match_per_wine(wine_type="sparkling")
bma = best_match_per_wine(wine_type="all")
