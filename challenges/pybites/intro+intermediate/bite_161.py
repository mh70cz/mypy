#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bite 161. Count the number of files and directories 

https://codechalleng.es/bites/161
"""
import os


def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    
    nfiles = 0
    ndirs =  0
        
    for root, dirs, files in os.walk(directory):
        nfiles += len(files)
        ndirs += len(dirs)
        
    return (ndirs, nfiles)        
        
    
