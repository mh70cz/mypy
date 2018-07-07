#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://codechalleng.es/bites/7/
datetime, parse datetime
Created on Sat Jul  7 21:15:37 2018

@author: mh70
"""

'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    idx = line.find(" ") + 1
    dt_str = line[idx: idx+19]
    year = int(dt_str[:4])
    month = int(dt_str[5:7])
    day = int(dt_str[8:10])
    hours = int(dt_str[11:13])
    minutes = int(dt_str[14:16])
    seconds = int(dt_str[17:19])
    d = datetime(year, month, day, hours, minutes, seconds)    
    return d



def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    shutd = []
    for line in loglines:
        if "Shutdown initiated" in line:
            shutd.append(line)
    d1 = convert_to_datetime(shutd[0])
    d2 = convert_to_datetime(shutd[1])
    td = d2 - d1
    return td