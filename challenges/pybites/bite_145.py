"""
Bite 145. Record Breakers - not passing test 

https://codechalleng.es/bites/145

"""
 
from collections import namedtuple
from datetime import date

import pandas as pd

DATA_FILE = "http://projects.bobbelderbos.com/pcc/weather-ann-arbor.csv"
STATION = namedtuple("Station", "ID Date Value")


def high_low_record_breakers_for_2015():
    """Extract the high and low record breaking temperatures for 2015

    The expected value will be a tuple with the highest and lowest record
    breaking temperatures for 2015 as compared to the temperature data
    provided.

    NOTE:
    The date values should not have any timestamps, should be a datetime.date() object.
    The temperatures in the dataset are in tenths of degrees Celsius, so you must divide them by 10

    Possible way to tackle this challenge:

    1. Create a DataFrame from the DATA_FILE dataset.
    2. Manipulate the data to extract the following:
       * Extract highest temperatures for each day between 2005-2015
       * Extract lowest temperatures for each day between 2005-2015
       * Remove February 29th from the dataset to work with only 365 days
    3. Separate data into two separate DataFrames:
       * high/low temperatures between 2005-2014
       * high/low temperatures for 2015
    4. Iterate over the 2005-2014 data and compare to the 2015 data:
       * For any temperature that is higher/lower in 2015 extract ID, Date, Value
    5. From the record breakers in 2015, extract the high/low of all the temperatures
       * Return those as STATION namedtuples, (high_2015, low_2015)
    """
    df = pd.read_csv(DATA_FILE)
    record_breakers = []
    record_breakers_total = []

    idx_list = []
    dates = df["Date"].unique()

    for d in dates:
        idx_max_date = df[(df["Date"] == d) & (df["Element"] == "TMAX")]["Data_Value"].idxmax()
        idx_min_date = df[(df["Date"] == d) & (df["Element"] == "TMIN")]["Data_Value"].idxmin()
        idx_list.append(idx_max_date)
        idx_list.append(idx_min_date)
    df_mm = df.loc[idx_list]
    idx_leap = df_mm[df_mm["Date"].str.contains("02-29")].index
    df_mm = df_mm.drop(idx_leap)
    
    df_05_14 = df_mm[df_mm["Date"] < "2015-01-01"]
    df_15 = df_mm[df_mm["Date"] >= "2015-01-01"]
    
    month_days = df_15["Date"].str[5:].unique()
    for md in month_days:
        #print(md)
        row_05_14 = df_05_14[df_05_14["Date"].str[5:] == md]
        row_15 = df_15[df_15["Date"].str[5:] == md]
        
        row_05_14_max = row_05_14[row_05_14["Element"] == "TMAX"]
        row_05_14_min = row_05_14[row_05_14["Element"] == "TMIN"]
        row_15_max = row_15[row_15["Element"] == "TMAX"]
        row_15_min = row_15[row_15["Element"] == "TMIN"]
        
        max_05_14 = row_05_14_max["Data_Value"].max()
        min_05_14 = row_05_14_min["Data_Value"].min()
        max_15 = row_15_max["Data_Value"].iloc[0]
        min_15 = row_15_min["Data_Value"].iloc[0]
        
        if max_15 > max_05_14 :
            record_breakers.append(row_15_max.index[0])
#            id_ = row_15_max["ID"].iloc[0]
#            d = row_15_max["Date"].iloc[0]
#            d = date(int(d[:4]), int(d[5:7]), int(d[8:]))
#            value = row_15_max["Data_Value"].iloc[0]
#            value = int(value) / 10            
#            station = STATION(id_, d, value)
#            record_breakers.append(station)
            
            
        
        if min_15 < min_05_14:
            record_breakers.append(row_15_min.index[0])
#            id_ = row_15_min["ID"].iloc[0]
#            d = row_15_min["Date"].iloc[0]
#            d = date(int(d[:4]), int(d[5:7]), int(d[8:]))
#            value = row_15_min["Data_Value"].iloc[0]
#            value = int(value) / 10                       
#            station = STATION(id_, d, value)
#            record_breakers.append(station)
            
    total_max_idx = df_mm.loc[record_breakers]["Data_Value"].idxmax()
    total_min_idx = df_mm.loc[record_breakers]["Data_Value"].idxmin()
    
    total_max = df_mm.loc[total_max_idx]
    total_min = df_mm.loc[total_min_idx]
    for s in [total_max, total_min]:
        id_ = s["ID"]
        d = s["Date"]
        d = date(int(d[:4]), int(d[5:7]), int(d[8:]))
        value = s["Data_Value"]
        value = int(value) / 10            
        station = STATION(id_, d, value)
        record_breakers_total.append(station)
        
    return record_breakers_total       
        
"""
[Station(ID='USW00014853', Date=datetime.date(2015, 7, 29), Value=36.1),
 Station(ID='USW00094889', Date=datetime.date(2015, 2, 20), Value=-34.3)]
"""    
    
    
            
            
            
             
    
    
        
    
    
    


        
   
    
    
    """
    
    
        for row in df_mm.itertuples():
        date = row.date
        
        
        element = row.element
        x = pd.to_datetime(df_mm["Date"])
        x.dt.dayofyear
        
        dfminmax = pd.DataFrame(columns=list(df.columns.values))
    
        dfmax = df[df["Element"] == "TMAX"]
        dfmin = df[df["Element"] == "TMIN"]
    
        dtmax = df[(df["Date"] == d) & (df["Element"] == "TMAX")]
        d_max = dtmax[dtmax["Data_Value"] == max(dtmax["Data_Value"])]
        dlist.append(d_max.values[0].tolist())
        #dfminmax.append(d_max)
        dtmin = df[(df["Date"] == d) & (df["Element"] == "TMIN")]
        d_min= dtmin[dtmin["Data_Value"] == min(dtmin["Data_Value"])]    
        #dfminmax.append(d_min)
        dlist.append(d_min.values[0].tolist())
    
    
    
        dates = df["Date"].unique()
        dfminmax = pd.DataFrame(columns=list(df.columns.values))
        
       df = df.set_index("Date")
    
    
    
    dtmax = df[(df["Date"] < "2005-01-02") & (df["Element"] == "TMAX")]
    df.loc[-1] = row
    
    df[df["Date"]=="2006-09-04"]
    df[(df["Date"]>="2005") & (df["Date"]<="2015")]
    df[(df["Date"]>="2005") & (df["Date"]<="2015") & (df["Element"] == "TMAX")]
    maxtmp = df[(df["Date"]>="2005") & (df["Date"]<="2015") & (df["Element"] == "TMAX")]
    mintmp = df[(df["Date"]>="2005") & (df["Date"]<="2015") & (df["Element"] == "TMIN")]
    
    """