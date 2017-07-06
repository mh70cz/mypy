""" challenge 2 http://www.pythonchallenge.com/pc/def/ocr.html
    http://www.pythonchallenge.com/pc/def/equality.html
"""

from collections import Counter
import urllib.request

def get_inner_content(url):
    """ open file, strip the envelope <!-- -->, and give the inner content"""

    with urllib.request.urlopen(url) as f:
        read_data = f.read()
        read_data = read_data.decode("ascii")

    # strip the last envelope <!-- -->
    open_envel_pos = read_data.rfind("<!--")
    close_envel_pos = read_data.rfind("-->")
    inner_data = read_data[(open_envel_pos + 4):close_envel_pos]

    chars_to_strip = ['\r', '\n']

    while inner_data[0] in chars_to_strip:
        inner_data = inner_data[1:]

    while inner_data[-1:] in chars_to_strip:
        inner_data = inner_data[:-1]

    return inner_data

def char_hist(inner_data):
    """ histogram of characters"""
    cnt = Counter(inner_data)
    print(cnt)

def main():
    """ main entry"""
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    char_hist(get_inner_content(url))

if __name__ == "__main__":
    main()
