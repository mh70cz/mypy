# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 12:56:17 2018

@author: mh70
"""

#from m import mtd as mmtd
import m as m_alias
from enum import Enum

class C_alt:
    x = "new"
    
    

class DateFormat_alt(Enum):
    MMDDYY = 0  # mm/dd/yy
    DDMMYY = 1  # dd/mm/yy
    YYMMDD = 2  # yy/mm/dd
    NONPARSABLE = -999

    @classmethod
    def get_d_parse_formats(cls, val=None):
        """ Arg:
        val(int | None) enum member value
        Returns:
        1. for val=None a list of explicit format strings 
            for all supported date formats in this enum
        2. for val=n an explicit format string for a given enum member value
        """
        d_parse_formats = ["%m/%d/%y", "%d/%m/%y", "%y/%m/%d"]
        if val is None:
            return d_parse_formats
        if 0 <= val <= len(d_parse_formats):
            return d_parse_formats[val]
        raise ValueError    
    
m_alias.C = C_alt
m_alias.DateFormat = DateFormat_alt


m_alias.mtd()