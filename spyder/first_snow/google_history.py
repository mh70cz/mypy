# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:34:16 2017
based on:
https://applecrazy.github.io/blog/posts/analyzing-browser-hist-using-python/

@author: mh70
"""

import sqlite3
from sqlite3 import Error
import pandas as pd

import numpy as np
from urllib.parse import urlparse
import matplotlib.pyplot as plt

def create_connection(db_file):
    """ create a database connection to the SQLite db specified by the db_file
    :param db_file: database file
    :return: Connection object or None    
    """
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    
    return None


def get_raw_data():
    
    db_path = r"C:\Users\m.houska\AppData\Local\Google\Chrome\User Data\Default"
    db_file_name = "History"
    database = db_path + '\\' + db_file_name
        
    # create a database connection        
    conn = create_connection(database)
    with conn:
    #    print("select raw data")
        cur = conn.cursor()
        cur.execute("select datetime(last_visit_time/1000000-11644473600,'unixepoch'), url from  urls order by last_visit_time desc;")
        
        rows = cur.fetchall() #raw data
    #    for row in rows:
    #        print(row)
        
    return rows

raw_data = get_raw_data()

data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

#convert the datetime string column into a column of Pandas datetime elements
# Since pandas represents timestamps in nanosecond resolution, 
# the timespan that can be represented using a 64-bit integer is limited 
# to approximately 584 years 
# '1677-09-22 00:12:43.145225' to '2262-04-11 23:47:16.854775807'
# see pd.Timestamp.min ; pd.Timestamp.max
# errors='coerce' create NaT for invalid values

data.datetime = pd.to_datetime(data.datetime, errors='coerce')

#remove all information from the URL, leaving only the domain/subdomain:
parser = lambda u: urlparse(u).netloc
data.url = data.url.apply(parser)   

site_frequencies = data.url.value_counts().to_frame()
site_frequencies.reset_index(inplace=True) # Make the domain a column

site_frequencies.columns = ['domain', 'count']

topN = 20
plt.title('Top $n sites Visited'.replace('$n', str(topN)))
pie_data = site_frequencies['count'].head(topN).tolist()

pie_labels = None

plt.pie(pie_data, autopct='1.1f%%', labels=pie_labels)
plt.show()

