# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:51:55 2017

@author: mh70
"""

import csv

filename = r"C:\Users\m.houska\Downloads\SubscriberList2017_10_23_02_41_21.csv"

with open(filename, newline='') as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
     header = next(csvreader)
     for row in csvreader:
         #print(', '.join(row))
         sub_name = row[0]
         sub_id = row[2]
         #print(sub_name +"; " + sub_id)
         print("<Subscriber>\n  <SubscriberId>" + sub_id + "</SubscriberId>\n" +
               "  <SubscriberName>" + sub_name + "</SubscriberName>\n</Subscriber>")