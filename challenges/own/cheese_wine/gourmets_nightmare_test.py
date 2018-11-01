import pytest
from gourmets_nightmare import best_match_per_wine, match_wine_5cheeses


def test_best_match_per_wine_all():
    assert best_match_per_wine()[2] == 13.0


cases_best_by_wine = [
    ("white", "Sauvignon blanc", "Smoked Austrian", 8.0),
    ("red", "Cabernet sauvignon", "Dorset Blue Vinney", 13.0),
    ("sparkling", "Moscato d’Asti", "Carré de l'Est", 6.0),
]


@pytest.mark.parametrize("case", cases_best_by_wine)
def test_best_match_per_wine_type(case):
    wine_type, *result = case
    assert best_match_per_wine(wine_type) == tuple(result)


def test_invalid_wine_type():
    with pytest.raises(ValueError):
        best_match_per_wine("cocacola")


def test_all_wines_included():
    assert len(match_wine_5cheeses()) == 26


mw5c = match_wine_5cheeses()
cases = [
    (0, "Barbera", "Cheddar", "Gruyère"),
    (1, "Barolo", "Boursin", "Cheddar"),
    (2, "Cabernet sauvignon", "Dorset Blue Vinney", "Norwegian Jarlsberg"),
    (3, "Cava", "Edam", "Gouda"),
    (-1, "Zinfandel", "Caithness", "Limburger"),
]


@pytest.mark.parametrize("case", cases)
def test_match_wine_5cheeses(case):
    """ test of presence of first 2 cheeses only
    because if score is same for more pairs, order of pairs cannot be assumed
    """
    idx, wine, cheese1, cheese2 = case
    assert mw5c[idx][0] == wine
    assert cheese1 in mw5c[idx][1]  # first cheese is in the list
    assert cheese2 in mw5c[idx][1]  # second cheese is in the list
    assert len(mw5c[idx][1]) == 5   # 5 cheeses are in the list
