# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Tue Dec 31 12:24:33 2019 
analyza vysledku testu v BEE
"""

import xml.etree.ElementTree as ET
from pathlib import Path
import os
from collections import namedtuple
from collections import Counter

FinalResult = namedtuple("FinalResult", "decision, not_evaluated, passed, rejected, manual, warning, no_data")

srcpath = Path("C:/BEE_batch/out__po")


# srcpath_new = Path("C:/BEE_batch/out_wrk")
# srcpath_old = Path("C:/BEE_batch/out_old_wrk")

ns = {"cls":"uri:creditinfosolutions/cls",}


def get_root(path):
    with open(path, encoding="utf-8") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def get_final_result(root):
    
    common_elem = root.find(".//cls:Outputs/cls:Common", ns)
    if common_elem is None:
        raise ValueError("missing Common")
    
    rules_elem = root.find(".//cls:Outputs/cls:Rules", ns)
    if rules_elem is None:
        raise ValueError("missing Rules")
    
    rules_result_elem = root.find(".//cls:Outputs/cls:RulesResults", ns)
    if rules_result_elem is None:
        raise ValueError("missing RulesResults")
    
    not_evaluated_elem = rules_result_elem .find(".//cls:NotEvaluated", ns)
    if not_evaluated_elem is not None:
        not_evaluated = not_evaluated_elem.text
    else:
        raise ValueError("missing NotEvaluated")        
    
    passed_elem = rules_result_elem .find(".//cls:Passed", ns)
    if passed_elem is not None:
        passed = passed_elem.text
    else:
        raise ValueError("missing Passed")         
        
    rejected_elem = rules_result_elem .find(".//cls:Rejected", ns)
    if rejected_elem is not None:
        rejected = rejected_elem.text
    else:
        raise ValueError("missing Rejected")         
    
    manual_elem = rules_result_elem .find(".//cls:Manual", ns)
    if manual_elem is not None:
        manual = manual_elem.text
    else:
        raise ValueError("missing Manual")         
        
    warning_elem = rules_result_elem .find(".//cls:Warning", ns)
    if warning_elem is not None:
        warning = warning_elem.text
    else:
        raise ValueError("missing Warning")         
       
    no_data_elem = rules_result_elem .find(".//cls:NoData", ns)
    if no_data_elem is not None:
        no_data = no_data_elem.text
    else:
        raise ValueError("missing NoData")         
        
    decision_elem = common_elem.find(".//cls:Decision", ns)
    if decision_elem is not None:
        decision = decision_elem.text
    else:
        raise ValueError("missing Decision")         
    
    final_result = FinalResult(decision, not_evaluated, passed, rejected, manual, warning, no_data)
    return final_result


def cnt_rules(rules, r_cnt):
    for rule in rules:
        r_name = rule.attrib["name"]
        r_res = rule.attrib["result"]
        r_cnt[(r_name, r_res)] += 1



        

files_new = []
for file in os.listdir(srcpath):
    if file.endswith(".xml"):
        files_new.append(file)


files_cnt = 0
final_results = []
manual_details_lst = []
r_cnt = Counter()
for file in files_new[:550]:
    print(file)
    path = srcpath/ file

    files_cnt += 1
    try:
        root = get_root(path)
        final_result = get_final_result(root)
        
        rules = root.find(".//cls:Rules", ns)
        cnt_rules(rules, r_cnt)

    except ValueError as e:
        print("*****   " + str(e) + "\n")
        continue
    final_results.append(final_result)
    
    if final_result.decision == "MANUAL":
        rules_result_elem = root.find(".//cls:Outputs/cls:RulesResults", ns)
        decision_manual_rules = []
        for elem in rules_result_elem:
            if "Decision_MANUAL" in elem.tag:
                decision_manual_rules.append(elem.text)
        manual_details = {
            "file": file,
            "rules_manual_cnt": final_result.manual,
            "rules_manual_txt": decision_manual_rules,
            }
        manual_details_lst.append(manual_details)


decision_continue_cnt = 0
decision_manual_cnt = 0    
for final_result in final_results:
    if final_result.decision == "CONTINUE":
        decision_continue_cnt += 1
    elif final_result.decision == "MANUAL":
        decision_manual_cnt += 1
        
        
    
        
print (f"\n__________\nfiles processed: {files_cnt}")    

print (f"CONTINUE: {decision_continue_cnt}  ({decision_continue_cnt/files_cnt*100:.2f} %)")       
print (f"MANUAL: {decision_manual_cnt}    ({decision_manual_cnt/files_cnt*100:.2f} %)") 


"""
[(x, r_cnt[x]) for x in r_cnt if x[1]=="Manual"]
sorted([(x, r_cnt[x]) for x in r_cnt if x[1]=="Manual"], key=lambda x: x[1], reverse=True)

[(x, r_cnt[x]) for x in r_cnt if x[1]=="Warning"]
sorted([(x, r_cnt[x]) for x in r_cnt if x[1]=="Warning"], key=lambda x: x[1], reverse=True)

zadatel cizinec:
[x for x in manual_details_lst if "BR_01_004" in "".join(x['rules_manual_txt'])]

Pocet statutaru:
[x for x in manual_details_lst if "BR_01_123" in "".join(x['rules_manual_txt'])]

Pocet pripadu, kdy posle na MANUAL  BR_01_123 jako jedine pravidlo:
len([x for x in manual_details_lst if ("BR_01_123" in "".join(x['rules_manual_txt'])) and (x["rules_manual_cnt"] == "1")])



"""