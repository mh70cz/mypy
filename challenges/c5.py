""" challenge 5
    http://www.pythonchallenge.com/pc/def/peak.html
    http://www.pythonchallenge.com/pc/def/channel.html
"""


import urllib.request
import pickle

def get_banner():
    """ get banner - no decoding"""
    url = "http://www.pythonchallenge.com/pc/def/banner.p"
    with urllib.request.urlopen(url) as f:
        return f.read()

def main():
    """ the main entry """
    banner_p = get_banner()

    banner = pickle.loads(banner_p)
    # load (without s) requires a file

    for x in banner:
        line = ""
        for y in x:
            line += y[1] * y[0]
        print(line)
main()
