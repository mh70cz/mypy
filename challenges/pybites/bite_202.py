"""
Bite 202. Analyze some Bite stats data - part II
"""
import csv
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        reader.__next__() # throw header
        lines = list(reader)
    lines.sort(key=lambda x:float(x[1]) if x[1] != "None" else -1, reverse=True)
        
    return [x[0].split(" ")[1].strip(".") for x in lines[:N]]
    


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
