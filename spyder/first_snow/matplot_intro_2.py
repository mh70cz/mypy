#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://realpython.com/blog/python/python-matplotlib-guide/
"""
from io import BytesIO
import tarfile
from urllib.request import urlopen
import matplotlib.pyplot as plt
import numpy as np

url = 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
b = BytesIO(urlopen(url).read())
fpath = 'CaliforniaHousing/cal_housing.data'

with tarfile.open(mode='r', fileobj=b) as archive:
    housing = np.loadtxt(archive.extractfile(fpath), delimiter=',' )
    
y = housing[:, -1] # area's average home value
pop, age = housing[:, [4, 7]].T # area's population , average house age

def add_titlebox(ax, text):
    ax.text(.55, .8, text, 
            horizontalaligment='center',
            transform = ax.transAxes,
            bbox=dict(facecolor='white', alpha=0.6),
            fontsize=12.5)
    return ax

gridsize = (3, 2)
fig = plt.figure(figsize=(12, 8))
ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
ax2 = plt.subplot2grid(gridsize, (2, 0))
ax3 = plt.subplot2grid(gridsize, (2, 1))