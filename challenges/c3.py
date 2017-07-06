""" chalenge 3 http://www.pythonchallenge.com/pc/def/equality.html
    http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import re
import urllib.request
import unittest

def get_inner_content(url):
    """ open file, strip the envelope <!-- -->, and give the inner content"""
    with urllib.request.urlopen(url) as f:
        read_data = f.read()
        read_data = read_data.decode("ascii")

    open_envel_pos = read_data.find("<!--")
    close_envel_pos = read_data.rfind("-->") # rfind from the end

    inner_data = read_data[(open_envel_pos + 4):close_envel_pos]

    chars_to_strip = ['\r', '\n']

    while inner_data[0] in chars_to_strip:
        inner_data = inner_data[1:]

    while inner_data[-1:] in chars_to_strip:
        inner_data = inner_data[:-1]

    return inner_data

def find_pattern_simple(inner_data):
    """ no edge cases """
    result = ""
    pattern = re.compile(r"[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]")
    # findall ...
    # If one or more groups are present in the pattern, return a list of groups
    # ([^A-Z][A-Z]{3}|^[A-Z]{3})[a-z]([A-Z]{3}[^A-Z]|[A-Z]{3}$) does not work

    found_results = re.findall(pattern, inner_data)
    for result_item in found_results:
        result += result_item[4]
    return result

def find_pattern(inner_data):
    """ covers edge cases:
        searched substring is at the beggining or end
        overlap """

    result = ""
    next_pos = 0
    pattern = re.compile(r"([^A-Z][A-Z]{3}|^[A-Z]{3})[a-z]([A-Z]{3}[^A-Z]|[A-Z]{3}$)")
    while True:
        found_result = pattern.search(inner_data, next_pos)
        if found_result is None:
            break
        result_item = found_result.group()
        next_pos = found_result.end() - 5 # -5 adjacent (with overlap)
        if (found_result.start() == 0) and (len(result_item) == 8):
            # at the begginig of a string
            result += result_item[3]
        else:
            result += result_item[4]
    return result

def main():
    """ Main entry """
    url = "http://www.pythonchallenge.com/pc/def/equality.html"

    res_s = find_pattern_simple(get_inner_content(url))
    res = find_pattern(get_inner_content(url))
    print("Simple find: " + res_s)
    print("Find:        " + res)


class TestFind(unittest.TestCase):
    """ ut """

    def test_a(self):
        """ string at start, middle, and end """
        inner_data = (
            "ABCsXYZwtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbC"
            "unkWDZmUZMiGqhRRiUvGmYmvnJIHEmbTMUKLECKdCthezSYBpIElRnXYZeFAQ"
        )
        self.assertEqual(find_pattern(inner_data), "sme")
        self.assertEqual(find_pattern_simple(inner_data), "m") #notOK

    def test_b(self):
        """ string at near start, near end """
        inner_data = "nABCsXYZwtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCnXYZeFAQn"
        self.assertEqual(find_pattern(inner_data), "se")
        self.assertEqual(find_pattern_simple(inner_data), "se") #OK

    def test_c(self):
        """ adjacent no overlap"""
        inner_data = "unkMiRSTyasABCaDEFqwGHIbJKLhRRiUvGmYmvnJIHEmbTMUKLECKd"
        self.assertEqual(find_pattern(inner_data), "ab")
        self.assertEqual(find_pattern_simple(inner_data), "ab") #OK

    def test_d(self):
        """ adjacent overlap"""
        inner_data = "ExFGHtloYgcABCaDEFbGHIcJKLxJhHVGxXDiQmzjfcpYbzxlWrVc"
        self.assertEqual(find_pattern(inner_data), "abc")
        self.assertEqual(find_pattern_simple(inner_data), "a") #notOK

    def test_e(self):
        """ adjacent no overlap at near start and near end"""
        inner_data = "sABCaDEFqwGHIbJKLnkMNOcPQRqwSTUdVWXe"
        self.assertEqual(find_pattern(inner_data), "abcd")
        self.assertEqual(find_pattern_simple(inner_data), "abcd") #OK

    def test_f(self):
        """ adjacent no overlap at start and end"""
        inner_data = "ABCaDEFqwGHIbJKLnkMNOcPQRqwSTUdVWX"
        self.assertEqual(find_pattern(inner_data), "abcd")
        self.assertEqual(find_pattern_simple(inner_data), "bc") #notOK

    def test_no_match(self):
        """ no match (new line separation in a pattern) """
        inner_data = (
            "xFGHtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmABC\n"
            "nDEFiGqhRRiUvGmYmvnJIHEmbTMUKLECKdCthezSYBpIE"
        )
        self.assertEqual(find_pattern(inner_data), "")
        self.assertEqual(find_pattern_simple(inner_data), "") #OK



if __name__ == '__main__':
    main()

# unittest.main()
