"""
wwwwwwwwww
"""

from datetime import datetime

composers = {
    "beethoven": ("Ludwig van Beethoven", "17 December 1770", "26 March 1827"),
    "wagner": ("Richard Wagner", "22 May 1813", "13 February 1883"),
    "verdi": ("Giuseppe Verdi", "9 October 1813", "27 January 1901"),
    "mozart": ("Wolfgang Amadeus Mozart", "27 January 1756", "5 December 1791"),
}

operas = [
    ("mozart", "Marriage of Figaro", "1 May 1786"),
    ("mozart", "Don Giovanni", "29 October 1787"),
    ("mozart", "Così fan tutte", "6 January 1790"),
    ("mozart", "The Clemency of Titus", "6 September 1791"),
    ("mozart", "The Magic Flute", "30 September 1791"),
    ("wagner", "The Fairies", "29 June 1888"),
    ("wagner", "Rienzi", "20 October 1842"),
    ("wagner", "The Flying Dutchman", "2 January 1843"),
    ("wagner", "Tannhäuser", "19 October 1845"),
    ("wagner", "Lohengrin", "28 August 1850"),
    ("wagner", "The Rhinegold", "22 September 1869"),
    ("wagner", "The Valkyrie", "26 June 1870"),
    ("wagner", "Siegfried", "16 August 1876"),
    ("wagner", "Twilight of the Gods", "17 August 1876"),
    ("wagner", "Tristan and Isolde", "10 June 1865"),
    ("wagner", "The Master-Singers of Nuremberg", "21 June 1868"),
    ("wagner", "Parsifal", "26 July 1882"),
    ("beethoven", "Fidelio", "20 November 1805"),
    ("verdi", "Nabucco", "9 March 1842"),
    ("verdi", "Ernani", "9 March 1844"),
    ("verdi", "Macbeth", "14 March 1847"),
    ("verdi", "Il corsaro", "25 October 1848"),
    ("verdi", "Rigoletto", "11 March 1851"),
    ("verdi", "La traviata", "6 March 1853"),
    ("verdi", "Aroldo", "16 August 1857"),
    ("verdi", "Macbeth", "21 April 1865"),
    ("verdi", "Don Carlos", "11 March 1867"),
    ("verdi", "Aida", "24 December 1871"),
    ("verdi", "Otello", "5 February 1887"),
    ("verdi", "Falstaff", "9 February 1893"),
]


def _get_date(date_str):
    return datetime.date(datetime.strptime(date_str, "%d %B %Y"))


def operas_both_at_premiere(guest, composer, operas=operas):
    """ Returns a list of operas,
    where the guest and the composer could have been together at premiere.
    """
    at_premiere = []

    guest_born = _get_date(composers[guest][1])
    guest_died = _get_date(composers[guest][2])
    composer_died = _get_date(composers[composer][2])

    for opera in operas:
        if opera[0] == composer:
            premiere = _get_date(opera[2])
            if (guest_born < premiere < guest_died) and (premiere < composer_died):
                at_premiere.append(opera[1])
    return at_premiere


def m_operas_both_on_premiere(composer_1, composer_2):
    both_on_premiere = []

    comp_1_born = _get_date(composers[composer_1][1])
    comp_1_died = _get_date(composers[composer_1][2])
    comp_2_born = _get_date(composers[composer_2][1])
    comp_2_died = _get_date(composers[composer_2][2])

    for opera in operas:
        if opera[0] in (composer_1, composer_2):
            premiere = _get_date(opera[2])
            if (comp_1_born < premiere < comp_1_died) and (
                comp_2_born < premiere < comp_2_died
            ):
                both_on_premiere.append(opera[1])
    return both_on_premiere

