#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 21:20:33 2017

@author: mh70
"""

import pandas as pd
import numpy as np
from urllib.parse import urlparse
import matplotlib.pyplot as plt

import get_raw_data

df_visits, df_urls = get_raw_data.main()

def data_sites(pd_df):
    data = pd_df.copy()
    #remove all information from the URL, leaving only the domain/subdomain:
    parser = lambda u: urlparse(u).netloc
    data.url = data.url.apply(parser)   
    
        
    site_frequencies = data.groupby(['url'])['visitcount'].sum().to_frame()
    
    site_frequencies.reset_index(inplace=True) # Make the domain a column
    
    site_frequencies.columns = ['domain', 'count']
    return site_frequencies

def visualize_sf(site_frequencies):
    topN = 20
    plt.title('Top $n sites Visited'.replace('$n', str(topN)))
    pie_data = site_frequencies['count'].head(topN).tolist()
    
    pie_labels = None
    
    plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
    plt.show()
    
site_frequencies = data_sites(df_urls)
visualize_sf(site_frequencies)



"""
sites_per_week = data['datetime'].groupby(data['datetime'].dt.week).count()
"""

