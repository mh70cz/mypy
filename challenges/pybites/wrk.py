# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Jul 31 19:21:27 2019 
"""

import pandas as pd
from pandas.util.testing import assert_frame_equal

movie_excel_file = "https://bit.ly/2BVUyrO"


df_skip = pd.read_excel(movie_excel_file, skiprows=7, usecols=[2, 3])
df_head = pd.read_excel(movie_excel_file, header=7, usecols=[2,3])

assert_frame_equal(df_skip, df_head)