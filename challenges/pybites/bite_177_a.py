"""
use of "header" instead of "skiprows" in the pd.read_excel method
"""


import pandas as pd
from pandas.util.testing import assert_frame_equal

movie_excel_file = "https://bit.ly/2BVUyrO"


df_skip = pd.read_excel(movie_excel_file, skiprows=7, usecols=[2,3])
df_head = pd.read_excel(movie_excel_file, header=7, usecols=[2,3])

assert_frame_equal(df_skip, df_head)
    

"""
# locally (Python 3.7.2, Win 10, pandas: 0.24.2 , pytest: 4.0.2) works OK
# does not work on pybite's server
df = pd.read_excel(data, header=7, usecols=[2,3]) 

# works OK on both
df = pd.read_excel(data, skiprows=7, usecols=[2,3])

"""