"""
Bite 79. Parse a csv file and create a bar chart 
oficiální řešení je výrazně lepší
https://codechalleng.es/bites/79
"""

import csv

import requests

from collections import  Counter

CSV_URL = 'https://bit.ly/2HiD2i8'


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    r = requests.get(CSV_URL, )
    return r.text.split("\r\n") #lépe splitlines -- nenechá poslední prázdný řádek

"""Unlike split() when a delimiter string sep is given, 
   this(splitlines() )  method returns an empty list for the empty string, 
   and a terminal line break does not result in an extra line:
"""       


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    c = Counter()

    cnt = content[1:-1] #strip first (header) and last line - lépe splitlines
    reader = csv.reader(cnt, delimiter=",") #lépe použít csv.DictReader
    for row in reader:
        #print(reader.line_num)
        #print(row)
        tz = row[2]
        c[tz] += 1
    txt_arr = []
    for k,v in c.items():
        txt_arr.append(f"{k:<20} | {v*'+'}")
    txt_arr.sort()
    print (txt_arr)
    

import re

import pytest



# making sure to call requests just once!
content = get_csv()

expected_output = """Africa/Algiers       | ++
Africa/Cairo         | +
Africa/Monrovia      | +
Africa/Nairobi       | ++++
America/Buenos_Aires | +
America/Chicago      | ++++++++++++++
America/Denver       | ++++
America/Fortaleza    | +
America/Los_Angeles  | +++++++++++++++++++++++++++++++++++
America/Manaus       | +
America/Mexico_City  | +++
America/New_York     | +++++++++++++++++++++++++++
America/Regina       | +
America/Santiago     | +
America/Sao_Paulo    | ++++
Asia/Amman           | +
Asia/Bangkok         | +
Asia/Chongqing       | ++++
Asia/Dhaka           | +
Asia/Istanbul        | ++
Asia/Jerusalem       | +
Asia/Kolkata         | +++++++++++++
Asia/Kuala_Lumpur    | +
Asia/Muscat          | +
Asia/Taipei          | +
Australia/Brisbane   | +
Australia/Canberra   | ++++++
Australia/Perth      | +
Europe/Amsterdam     | ++++++++++++++
Europe/Athens        | ++
Europe/Belgrade      | +
Europe/Helsinki      | +
Europe/London        | ++++++++++++
Europe/Moscow        | ++
Europe/Warsaw        | ++
Pacific/Honolulu     | +
""".splitlines()


@pytest.mark.parametrize("expected_line", expected_output)
def test_output(expected_line, capfd):
    create_user_bar_chart(content)
    output = capfd.readouterr()[0]

    timezone, pluses = expected_line.split('|')
    timezone = timezone.strip()
    pluses = pluses.strip().replace('+', '\+')  # escape for upcoming regex

    # allow variable number of spaces before/after the pipe
    pattern = r'{}\s+\|\s+{}'.format(timezone, pluses)
    assert re.search(pattern, output)


import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          