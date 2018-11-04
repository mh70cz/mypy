"""
Bite 48. Make a bar chart of new Safari books 
https://codechalleng.es/bites/48/ 
Created on Thu Jul 19 20:47:51 2018
 
"""


import os
import urllib.request

# import pytest
# pytest.main(["bite_48.py"])

LOG = os.path.join("/tmp", "safari.logs")
PY_BOOK, OTHER_BOOK = "🐍", "."
urllib.request.urlretrieve("http://bit.ly/2BLsCYc", LOG)


def create_chart():
    dates = []
    with open(LOG) as f:
        line_prev = f.readline()
        for line in f.readlines():
            if "sending to slack channel" in line:
                d = line[:5]
                if not dates:
                    dates.append(d + " ")
                if not d in dates[-1]:
                    dates.append(d + " ")
                book = line_prev[50:]
                if "python" in book.lower():
                    token = PY_BOOK
                else:
                    token = OTHER_BOOK
                dates[-1] += token
            line_prev = line
    print(dates)


expected_lines = """02-13 ...........
02-14 ..............
02-15 .................
02-16 ............
02-19 🐍.......🐍
02-20 ...
02-21 ..............🐍
02-22 🐍...................""".split(
    "\n"
)


def test_valid_output(capfd):
    create_chart()
    out, _ = capfd.readouterr()
    for line in expected_lines:
        assert line in out, f'"{line}" should be in output of create_chart'
