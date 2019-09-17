"""
 Bite 190. Parse income distribution from Latin America XML
"""

from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict
import xml.etree.ElementTree as ET

# import the countries xml file
tmp = Path('/tmp')
countries = tmp / 'countries.xml'

if not countries.exists():
    urlretrieve('https://bit.ly/2IzGKav', countries)


def get_income_distribution(xml=countries):
    """
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys = incomes (wb:incomeLevel)
      - values = list of country names (wb:name)
    """
    
    income = defaultdict(list)    
    ns = {"wb": "http://www.worldbank.org",}
    
    tree = ET.parse(xml)
    root = tree.getroot()
    countries = root.findall("wb:country", ns)
    for country in countries:
        income_level = country.find("wb:incomeLevel", ns).text
        name = country.find("wb:name", ns).text
        income[income_level].append(name)
    return income
            
        