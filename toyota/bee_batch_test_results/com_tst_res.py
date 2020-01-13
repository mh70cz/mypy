# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Tue Dec 31 12:24:33 2019 
porovnani vysledku testu v BEE
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import os
from collections import namedtuple

Results = namedtuple("Result", "decision, not_evaluated, passed, rejected, manual, warning, no_data")

srcpath_new = Path("C:/BEE_batch/out__spo")
srcpath_old = Path("C:/BEE_batch/out__spo_56")

# srcpath_new = Path("C:/BEE_batch/out_wrk")
# srcpath_old = Path("C:/BEE_batch/out_old_wrk")

ns = {"cls":"uri:creditinfosolutions/cls",}


def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def get_results(path):
    
    root = get_root(path)
    common_elem = root.find(".//cls:Outputs/cls:Common", ns)
    if common_elem is None:
        raise ValueError("missing Common")
    
    rules_elem = root.find(".//cls:Outputs/cls:Rules", ns)
    if rules_elem is None:
        raise ValueError("missing Rules")
    
    rules_results_elem = root.find(".//cls:Outputs/cls:RulesResults", ns)
    if rules_results_elem is None:
        raise ValueError("missing RulesResults")
    
    not_evaluated_elem = rules_results_elem .find(".//cls:NotEvaluated", ns)
    if not_evaluated_elem is not None:
        not_evaluated = not_evaluated_elem.text
    else:
        raise ValueError("missing NotEvaluated")        
    
    passed_elem = rules_results_elem .find(".//cls:Passed", ns)
    if passed_elem is not None:
        passed = passed_elem.text
    else:
        raise ValueError("missing Passed")         
        
    rejected_elem = rules_results_elem .find(".//cls:Rejected", ns)
    if rejected_elem is not None:
        rejected = rejected_elem.text
    else:
        raise ValueError("missing Rejected")         
    
    manual_elem = rules_results_elem .find(".//cls:Manual", ns)
    if manual_elem is not None:
        manual = manual_elem.text
    else:
        raise ValueError("missing Manual")         
        
    warning_elem = rules_results_elem .find(".//cls:Warning", ns)
    if warning_elem is not None:
        warning = warning_elem.text
    else:
        raise ValueError("missing Warning")         
       
    no_data_elem = rules_results_elem .find(".//cls:NoData", ns)
    if no_data_elem is not None:
        no_data = no_data_elem.text
    else:
        raise ValueError("missing NoData")         
        
    decision_elem = common_elem.find(".//cls:Decision", ns)
    if decision_elem is not None:
        decision = decision_elem.text
    else:
        raise ValueError("missing Decision")         
    
    results = Results(decision, not_evaluated, passed, rejected, manual, warning, no_data)
    return results


files_new = []
for file in os.listdir(srcpath_new):
    if file.endswith(".xml"):
        files_new.append(file)

results_diffs_cnt = 0
files_cnt = 0
for file in files_new[:550]:
    print(file)
    path_new = srcpath_new / file
    path_old = srcpath_old / file
    files_cnt += 1
    try:
        results_new = get_results(path_new)    
        results_old = get_results(path_old)
    except ValueError as e:
        print("*****   " + str(e) + "\n")
        results_diffs_cnt += 1
        continue
    
    if results_new != results_old:
        results_diffs_cnt += 1
        print (results_new)
        print (results_old)
        print ("")
        
print (f"\n__________\nfiles processed: {files_cnt}\nresults diffs: {results_diffs_cnt}")        
        