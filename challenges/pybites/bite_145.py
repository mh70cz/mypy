"""
Bite 145. Record Breakers 

https://codechalleng.es/bites/145

"""
 
from collections import namedtuple
from datetime import date

import pandas as pd
import numpy as np

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
    g_tmax = df[df["Element"] == "TMAX"]
    g_tmin = df[df["Element"] == "TMIN"]
    

    grp_tmax = g_tmax.groupby(["Date"])
    grp_tmin = g_tmin.groupby(["Date"])  
    
    daily_max = grp_tmax.agg({ "Data_Value": np.max })
    daily_min = grp_tmin.agg({ "Data_Value": np.min })
    
    daily_max.reset_index(inplace=True)
    daily_min.reset_index(inplace=True)
    
    daily_max_15 = daily_max[daily_max["Date"] >= "2015-01-01"]
    daily_max_05_14 = daily_max[daily_max["Date"] <= "2014-12-31"]
    daily_min_15 = daily_min[daily_min["Date"] >= "2015-01-01"]
    daily_min_05_14 = daily_min[daily_min["Date"] <= "2014-12-31"]    
    md_05_14 = daily_max_05_14["Date"].str[5:]
    
    daily_max_05_14["md"] = md_05_14
    daily_min_05_14["md"] = md_05_14
    grp_md_max_05_14 = daily_max_05_14.groupby("md")
    grp_md_min_05_14 = daily_min_05_14.groupby("md")
    md_max_05_14 = grp_md_max_05_14.agg({"Date": "first", "Data_Value": np.max})
    md_min_05_14 = grp_md_min_05_14.agg({"Date": "first", "Data_Value": np.min})
    
    record_breakers = []
    record_breakers_total = []
    
    month_days = list(daily_max_15["Date"].str[5:])

    for md in month_days:
        day_15 = daily_max_15[daily_max_15["Date"].str[5:] == md]
        day_05_14 = md_max_05_14.loc[md]        
        if (day_15["Data_Value"].iloc[0]) > (day_05_14["Data_Value"]):
            record_breakers.append(day_15.iloc[0])
            
        day_15 = daily_min_15[daily_min_15["Date"].str[5:] == md]
        day_05_14 = md_min_05_14.loc[md]        
        if (day_15["Data_Value"].iloc[0]) < (day_05_14["Data_Value"]):
            record_breakers.append(day_15.iloc[0])            
                      
    rbs = sorted(record_breakers, key = lambda x: x["Data_Value"])
    for s in [rbs[-1], rbs[0]]:
        
        d = s["Date"]
        value = s["Data_Value"]
        id_ = df[(df["Date"]==d ) & (df["Data_Value"]==value)].iloc[0]["ID"]
        
        value = int(value) / 10            
        d = date(int(d[:4]), int(d[5:7]), int(d[8:]))
        station = STATION(id_, d, value)
        record_breakers_total.append(station)
                  
    return record_breakers_total
    
