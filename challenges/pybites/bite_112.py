"""
Bite 112. Social Media Username Validator 


https://codechalleng.es/bites/112
"""

# nice snippet: https://gist.github.com/tonybruess/9405134
from collections import namedtuple
import re

social_platforms = """Twitter
  Min: 1
  Max: 15
  Can contain: a-z A-Z 0-9 _

Facebook
  Min: 5
  Max: 50
  Can contain: a-z A-Z 0-9 .

Reddit
  Min: 3
  Max: 20
  Can contain: a-z A-Z 0-9 _ -
"""

# note range is of type range and regex is a re.compile object
Validator = namedtuple('Validator', 'range regex')


def parse_social_platforms_string():
    """Convert the social_platforms string above into a dict where
       keys = social platformsname and values = validator namedtuples"""
    sp_dct = dict()
    sp_long = social_platforms.split("\n\n")
    sp_split =[x.split("\n") for x in sp_long]
    for sp in sp_split:
        key = sp[0]
        min_raw = sp[1]
        max_raw = sp[2]
        reg_raw = sp[3]
        
        min_range = int(min_raw.replace("  Min: ",""))
        max_range = int(max_raw.replace("  Max: ", ""))
        reg_proc = reg_raw.replace("  Can contain: ","").replace(" ","")
        reg = re.compile(f"^[{reg_proc}]" + "{" + f"{min_range},{max_range}" + "}$")
        validator = Validator(range(min_range, max_range +1), reg)
        sp_dct[key] = validator
    return sp_dct

def validate_username(platform, username):
    """Receives platforms(Twitter, Facebook or Reddit) and username string,
       raise a ValueError if the wrong platform is passed in,
       return True/False if username is valid for entered platform"""
    all_validators = parse_social_platforms_string()
    if platform not in all_validators.keys():
        raise ValueError
    validator = all_validators[platform]
    found = validator.regex.search(username)
    return bool(found)
    
    
    