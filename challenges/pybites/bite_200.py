# -*- coding: utf-8 -*-
"""
Bite 200.  Minecraft Enchantable Items
"""

from pathlib import Path
from urllib.request import urlretrieve
from collections import defaultdict

from bs4 import BeautifulSoup as Soup

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"


ITEMS_LST = {'armor': 'armor',
             'axe': 'axe',
             'boots': 'boots',
             'bow': 'bow',
             'chestplate': 'chestplate',
             'crossbow': 'crossbow',
             'rod': 'fishing_rod',
             'helmet': 'helmet',
             'pickaxe': 'pickaxe',
             'shovel': 'shovel',
             'sword': 'sword',
             'trident': 'trident'}


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """

    def __init__(self, id_name, name, max_level, description, items=None):
        self.id_name = id_name
        self.name = name
        self.max_level = max_level
        self.description = description
        if items is None:
            self.items = []
        else:
            self.items = items
    
    
    def append(self, item):
        self.items.append(item)
        
    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"
        
        


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """

    def __init__(self, name, enchantments=None):
        self.name = name
        if enchantments is None:
            self.enchantments = []
        else:
            self.enchantments = enchantments
        
    def __str__(self):
        name = self.name.title().replace("_", " ")
        string = f"{name}: "
        for e in sorted(self.enchantments, key=lambda x:x.id_name):
            string += f"\n  [{e.max_level}] {e.id_name}"
        return string


def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
 

    
    romans_map = {"I":1, "II":2, "III":3, "IV":4, "V":5}
    
    
    table = soup.find("table", id='minecraft_items')
    rows = table.find_all("tr")
    
    enchantments = {}

    for row in rows[1:]:
        cols = row.find_all("td")
        for col in cols:
            id_name = cols[0].find("em").text
            name =  cols[0].find("a").text
            max_level = romans_map[cols[1].text]
            description = cols[2].text
            #minecraft_id = cols[3].text
            items_raw = cols[4].find("img")["data-src"].split(".")[0].split("/")[-1]
            items_raw = items_raw.split("_")
            items = [x for x in ITEMS_LST.keys() if x in items_raw]
            items = [ITEMS_LST[x] for x in items]
            
        enchantments[id_name] = Enchantment(id_name, name, max_level, description, items)
        
    return enchantments

def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    dd = defaultdict(list)
    for k,v in data.items():
        items = v.items
        for item in items:
            dd[item].append(v)
    
    item_classes = {} 
    for k in sorted(dd.keys()):
        item_class = Item(k,dd[k])
        item_classes[k] = item_class
        
    return item_classes


def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup


def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""