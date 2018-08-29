"""
Bite 79. Parse a csv file and create a bar chart 

https://codechalleng.es/bites/79
"""

import csv
from collections import Counter

import requests

CSV_URL = 'https://bit.ly/2HiD2i8'

timezones = Counter()


def get_csv():
    """Use requests to download the csv and return the
       decoded content"""
    with requests.Session() as s:
        download = s.get(CSV_URL)
        return download.content.decode('utf-8')


def create_user_bar_chart(content):
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    reader = csv.DictReader(content.splitlines(), delimiter=',')
    for row in reader:
        tz = row['tz']
        timezones[tz] += 1

    for location, count in sorted(timezones.items()):
        print(f'{location:<20} | {"+"*count}')
    

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