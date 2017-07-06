""" http://www.pythonchallenge.com/pc/def/linkedlist.php
    http://www.pythonchallenge.com/pc/def/peak.html
"""

import urllib.request
import re

def get_nothings():
    """ get list of nothings """
    nothing = "8022" # 12345 8022
    nothings = [nothing]
    rsps = list()
    base_url = r"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

    for n in range(1, 401):
        url = base_url + nothing

        try:
            with urllib.request.urlopen(url) as f:
                rsp = f.read(300)
                rsp = rsp.decode("ascii")
                rsps.append(rsp)
        except Exception as e:
            print(str(n) + " " + str(e))
            break
        print(f"{n}:  {rsp}")
        nothing = extract_num(rsp)
        if nothing and ("and the next nothing " in rsp):     
            nothings.append(nothing)
        else:
            print(str(n) + " " + rsp)
            break
    return nothings

def extract_num(rsp):
    """ extract number of nothing at the end, return None if not found"""
    pattern = re.compile(r"\d{1,5}$")
    result = pattern.search(rsp)
    if result:
        return result.group()
def main():
    """main entry"""
    nthgs = get_nothings()
    print(nthgs)

main()
