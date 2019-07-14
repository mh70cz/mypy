"""
https://codechalleng.es/bites/160/

"""

import csv
import os
from urllib.request import urlretrieve

BATTLE_DATA = os.path.join('/tmp', 'battle-table.csv')
if not os.path.isfile(BATTLE_DATA):
    urlretrieve('https://bit.ly/2U3oHft', BATTLE_DATA)


def _create_defeat_mapping():
    """Parse battle-table.csv building up a defeat_mapping dict
       with keys = attackers / values = who they defeat.
    """
    table = {}
    with open(BATTLE_DATA) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            itms = list(row.items())
            table[row["Attacker"]] = dict(itms[1:])
    return table      
        
        



def get_winner(player1, player2, defeat_mapping=None):
    """Given player1 and player2 determine game output returning the
       appropriate string:
       Tie
       Player1
       Player2
       (where Player1 and Player2 are the names passed in)

       Raise a ValueError if invalid player strings are passed in.
    """
    defeat_mapping = defeat_mapping or _create_defeat_mapping()
    valid_gestures = defeat_mapping.keys()
    if player1 not in valid_gestures:
        raise ValueError()
    if player2 not in valid_gestures:
        raise ValueError()

    result = defeat_mapping[player1][player2]
    if result == "draw":
        return "Tie"
    if result == "win":
        return player1
    return player2
    

    
    