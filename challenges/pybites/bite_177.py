"""
Bite 177. Use Pandas to find most common genres in a movie excel sheet
"""

import pandas as pd
import numpy as np

movie_excel_file = "https://bit.ly/2BVUyrO"


def explode(df, lst_cols, fill_value='', preserve_index=False):
    """Helper found on SO to split pipe (|) separted genres into
       multiple rows so it becomes easier to group the data -
       https://stackoverflow.com/a/40449726
    """
    if(lst_cols is not None and len(lst_cols) > 0 and not
       isinstance(lst_cols, (list, tuple, np.ndarray, pd.Series))):
        lst_cols = [lst_cols]
    idx_cols = df.columns.difference(lst_cols)
    lens = df[lst_cols[0]].str.len()
    idx = np.repeat(df.index.values, lens)
    res = (pd.DataFrame({
                col:np.repeat(df[col].values, lens)
                for col in idx_cols},
                index=idx)
             .assign(**{col:np.concatenate(df.loc[lens>0, col].values)
                            for col in lst_cols}))
    if (lens == 0).any():
        res = (res.append(df.loc[lens==0, idx_cols], sort=False)
                  .fillna(fill_value))
    res = res.sort_index()
    if not preserve_index:
        res = res.reset_index(drop=True)
    return res

def group_by_genre(data=movie_excel_file):
    """Takes movies data excel file (https://bit.ly/2BXra4w) and loads it
       into a DataFrame (df).

       "Explode" genre1|genre2|genre3 into separte rows using the "explode"
       function mentioned here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1) sorted by movie count
       descending (example output: https://bit.ly/2ILODva)
    """
    df = pd.read_excel(data, skiprows=7, usecols=[2, 3])
    
    # create a list (the explode method requires a list)
    df["genres"] = df["genres"].str.split('|') 
    
    df = explode(df, ['genres'])
    df = df[df['genres'] != '(no genres listed)']
    grp = df.groupby(['genres']).count()
    srt = grp.sort_values(by="movie", ascending=False)
    return srt

def group_by_genre2(data=movie_excel_file):
    """Takes movies data excel file (https://bit.ly/2BXra4w) and loads it
       into a DataFrame (df).

       Explode genre1|genre2|genre3 into separte rows using the provided
       "explode" function we found here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1) sorted by movie count
       descending (example output: https://bit.ly/2ILODva)
    """
  
    #df = pd.read_excel(data, header=7, usecols=[2,3])
    df = pd.read_excel(data, skiprows=7, usecols=[2,3])
    genres_exp = df["genres"].str.split("|").apply(pd.Series, 1)
    s = genres_exp.stack()
    s.index = s.index.droplevel(-1) # only indices from df
    s.name = "genres2" #  df.join() requires a name for s     
    df = df.join(s)
    
    df = df[df["genres2"] != "(no genres listed)"]
    
    grp = df[["genres2", "movie"]].groupby(by="genres2").count()
    srt = grp.sort_values(by="movie", ascending=False)
    srt.index.name = "genres"
    return srt

def group_by_genre3(data=movie_excel_file):
    """Takes movies data excel file (https://bit.ly/2BXra4w) and loads it
       into a DataFrame (df).

       Explode genre1|genre2|genre3 into separte rows using the provided
       "explode" function we found here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1) sorted by movie count
       descending (example output: https://bit.ly/2ILODva)
    """

    df = pd.read_excel(data)
    
    df = df.iloc[:,[2,3]]
    df = df[~df.iloc[:,0].isna()]
    col_names = [df.iloc[0,0],df.iloc[0,1]]      # read the top row
    df.columns = col_names
    df.drop([df.index[0]], axis=0, inplace=True) # delete the top row
    
    genres_exp = df['genres'].str.split('|').apply(pd.Series, 1)
    s = genres_exp.stack()
    s.index = s.index.droplevel(-1) # only indices from df
    s.name = 'genres2' #  df.join() requires a name for s     
    df = df.join(s)
    
    df = df[df["genres2"] != "(no genres listed)"]
    
    grp = df[["genres2", "movie"]].groupby(by="genres2").count()
    srt = grp.sort_values(by="movie", ascending=False)
    srt.index.name = "genres"
    return srt
    
