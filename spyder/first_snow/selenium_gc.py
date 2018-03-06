#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:31:25 2018

@author: mh70
"""

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import csv
import datetime

pwd_val = '' #'l...e'

if pwd_val == "":
    pwd_val = input("Password: ")

def save_to_file(fname, dict_to_save):
    with open(fname, 'w', newline='', encoding='utf-8') as csvfile:
        csv_out = csv.writer(csvfile)
        csv_out.writerow(["cache", "loggers"])

        ''' one value per row
        for key, values in dict_to_save.items():
            for value in values:
                csv_out.writerow([key, value])  
        '''
        for key, values in dict_to_save.items():
            csv_out.writerow([key, values])


opts = Options()
opts.set_headless()
assert opts.headless # operation in headles mode
browser = Firefox(options=opts)



browser.get('https://www.geocaching.com/account/login')
usr = browser.find_element_by_id('Username')
pwd = browser.find_element_by_id('Password')
log_in = browser.find_element_by_id('Login')
usr.send_keys('mh70+ic76')
pwd.send_keys(pwd_val)
log_in.click()


'''
https://coord.info/GC290AN Trapistický klášter
https://coord.info/GC40WZM Pod mohutnym modrinem
https://coord.info/GC6QWNR Polokacer
https://coord.info/GC6V72Y Superkacer
https://coord.info/GC6ZNTB Treti kacer
https://coord.info/GC7030Q Kostel na Barrandove
https://coord.info/GC7JMAV Kostel naZlichove
'''

caches = {'GC290AN': 'Trapistický klášter',
          'GC40WZM': 'Pod mohutnym modrinem',
          'GC6QWNR': 'Polokacer',
          'GC6V72Y': 'Superkacer',
          'GC6ZNTB': 'Treti kacer',
          'GC7030Q': 'Kostel na Barrandove',
          'GC7JMAV': 'Kostel na Zlichove',          
          }


'''
#https://coord.info/GC7JMAV
browser.get('https://coord.info/GC7JMAV')
logs_table = browser.find_element_by_id("cache_logs_table")

finders = logs_table.find_elements_by_class_name('logOwnerProfileName')

for f in finders:
    print (f.text)
'''

cache_loggers = dict()

for cache in caches.keys():
    cache_url = 'https://coord.info/' + cache
    browser.get(cache_url)
    logs_table = browser.find_element_by_id('cache_logs_table')
    loggers = logs_table.find_elements_by_class_name('logOwnerProfileName')
    loggers_lst = list()
    for l in loggers:
        print (l.text)
        loggers_lst.append(l.text)
    
    cache_loggers[cache] = loggers_lst
    
    
now = datetime.datetime.today().strftime('%Y-%m-%dT%H%M%S')
fname = './data/loggers' + now + '.txt'
save_to_file(fname, cache_loggers)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
