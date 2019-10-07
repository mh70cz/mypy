"""
 Bite 205. Female speakers @ Pycon US
"""

from urllib.request import urlretrieve
from pathlib import Path

import gender_guesser.detector as gender
from bs4 import BeautifulSoup as Soup

TMP = Path('/tmp')
PYCON_HTML = TMP / "pycon2019.html"
if not PYCON_HTML.exists():
    urlretrieve('https://bit.ly/2O5Bik7', PYCON_HTML)

def _get_soup(html=PYCON_HTML):
    return Soup(html.read_text(encoding="utf-8"), "html.parser")


def get_pycon_speaker_first_names(soup=None):
    """Parse the PYCON_HTML using BeautifulSoup, extracting all
       speakers (class "speaker"). Note that some items contain
       multiple speakers so you need to extract them.
       Return a list of first names
    """
    soup = _get_soup()
    speakers = []
    xsps = []
    speakers_raw = soup.find_all("span", class_="speaker") #<span class="speaker">
    for speaker_raw in speakers_raw:
        sp = speaker_raw.text.strip()
        xsps.append(sp)
        if ("," in sp):
            sps = sp.split(",") 
            speakers.extend(sps)
        elif ("/" in sp):
            sps = sp.split("/") 
            speakers.extend(sps)          
        else:    
            speakers.append(sp)
    first_names = []
    for speaker in speakers:
        names = speaker.strip().split(" ")
        if names[0][1] != ".":
            first_names.append(names[0].strip())
        else:
            first_names.append(names[1].strip())
    return first_names
        
    
    

def get_percentage_of_female_speakers(first_names):
    """Run gender_guesser on the names returning a percentage
       of female speakers, rounded to 2 decimal places."""
    males = 0
    females = 0
    d = gender.Detector()
    for name in first_names:
        gend = d.get_gender(name)
        if gend in ["female", "mostly_female"]:
            females += 1
        if gend in ["male", "mostly_male"]:
            males += 1
    return round(females/len(first_names)*100, 2)
            

if __name__ == '__main__':
    names = get_pycon_speaker_first_names()
    perc = get_percentage_of_female_speakers(names)
    print(perc)