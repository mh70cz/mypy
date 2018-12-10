"""
Bite 69. Regex Fun - part II


https://codechalleng.es/bites/069
"""

import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
    result = pattern.search(text)
    return bool(result)


def is_integer(number):
    """Return True if number is an integer"""
    pattern = re.compile(r"^-?\d+$")
    return bool(pattern.search(str(number)))


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = re.compile(r"\w-\w")
    result = pattern.search(text)
    return bool(result)
    


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = re.compile(r"\s\([^)]+\)")
    return pattern.sub("", text)
    


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    pattern = re.compile(r"[?!.,;]\s?")
    split =  pattern.split(text)
    return [x for x in split if x is not ""]



def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pattern = re.compile(r"\s{2,}")
    return pattern.sub(" ",text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = re.compile(r"[aeiou]{3}")
    return bool(pattern.search(word))


def convert_emea_date_to_amer_date_mh(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pattern = re.compile(r"\d\d/\d\d/")
    mmdd = pattern.search(date)
    if mmdd is None:
        return date
    else:
        mmdd = mmdd[0]
    pattern2 = re.compile(mmdd)
    ddmm = mmdd[3:5] + "/" + mmdd[0:2] + "/"
    return pattern2.sub(ddmm, date)

def convert_emea_date_to_amer_date(date):
    return re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2/\1/\3', date)
    
    