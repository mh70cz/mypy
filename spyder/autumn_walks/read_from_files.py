#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 21:39:53 2017

@author: mh70
"""

import csv

data_path = "./data/"
files_from_days_Sep = [
    "2017-09-23", "2017-09-24", "2017-09-25", "2017-09-26", '2017-09-27', 
    '2017-09-28', '2017-09-29', '2017-09-30'
    ]

files_from_days_Oct = [
        '2017-10-01', '2017-10-02', '2017-10-03', '2017-10-04', '2017-10-05', 
        '2017-10-06', '2017-10-07'
        #'2017-10-08', '2017-10-09'
        ]

files_from_days = files_from_days_Sep + files_from_days_Oct


def read_from_file(fname):
    read_list = list()
    with open(fname, newline='', encoding='utf-8') as csvfile:
        csv_in = csv.reader(csvfile)
        next(csv_in)  # gets the first line
        for row in csv_in:
            t = tuple(row)
            read_list.append(t)
    return read_list

fnames = list()
big_list = list()

for day in files_from_days:
    fnames.append("idnes+lidovky" + day + ".csv")

for fname in fnames:
    big_list.extend(read_from_file(data_path + fname))
      
