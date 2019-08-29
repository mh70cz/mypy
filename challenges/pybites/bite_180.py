"""
Bite 180. Group names by country
"""

from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    lines = data.splitlines()
    for line in lines:
        chunks = line.split(",")
        surname = chunks[0]
        name = chunks[1]
        country = chunks[2] 
        if country == "country_code":
            continue
        countries[country].append(name + " " + surname)
    return countries