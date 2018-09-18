"""

"""
import xml.etree.ElementTree as ET
import os
import sys
import csv

pname = r'C:\Users\m.houska\Documents\_CIS\Toyota\strategie'

#fname_in= "strategy02.xml"
#fname_out = "op02.csv"

fname_in= "strategy36.xml"
fname_out = "op36.csv"

#fname_in= "strategy79.xml"
#fname_out = "op79.csv"

csvname = 'rulesDesc.csv'
op_desc_csv = os.path.join(pname, csvname )

op_desc = []

with open(op_desc_csv) as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        op_desc.append(row)



xmlpath = os.path.join(pname, fname_in)
tree = ET.parse(xmlpath)
root = tree.getroot()

#https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
namespaces = {'xsi': "http://www.w3.org/2001/XMLSchema-instance"} # add more as needed
results = root.findall(".//BaseProcess[@xsi:type='Result']", namespaces)

ops = []

def parse():
    results_lst = list()
    op_set = set()
    for r in results:
        uid = r.attrib["uid"]
        processName =r.find("./processName").text        
        exp = r.findall("./exprMapping/BaseExpression") #ExpressionFunc , ExpressionConst
        exp_lst = []
        if not(exp is None):
            for idx, exp in enumerate(exp):
                exp_uid = exp.attrib["uid"]
                exp_name = exp.find("./name").text
                exp_param = exp.find("./param").text
                exp_type = exp.find("./Type").text
                args = exp.findall("./arguments/BaseExpression")
                exp_arg_lst = []
                if not(args is None):
                    for idx, a in enumerate(args):
                        a_name = a.find("./name").text
                        a_param = a.find("./param").text
                        a_type = a.find("./Type").text
                        exp_arg_lst.append((idx,a_name,a_param,a_type))
                exp_lst.append((idx, exp_uid, exp_name, exp_param, exp_type, exp_arg_lst))
                op_set.add(exp_name)

                                
        results_lst.append((uid, processName, exp_lst))
    op_set = list(op_set)
    op_set.sort()
    return results_lst, op_set
        


def wrt(results, op_set):
    for op in op_set:
        descr = ""
        for local_op in op_desc:
            if op == local_op[1].strip():
                descr = local_op[2]
                break
        
        print(f"{op} ,{descr}")
        print(f"")
        for r in results:
            exps = r[2]
            for e in exps:
                local_op_name = e[2]
                if op == local_op_name:
                    #print(op, local_op_name)
                    idx, exp_uid, exp_name, exp_param, exp_type, exp_arg_lst = e
                    result_name = r[1]
                    print(f",{result_name},{exp_param},,,{exp_uid},{exp_type}")
                    for a in exp_arg_lst:
                        a_idx, a_name, a_param, a_type = a
                        print(f" , ,${a_idx},{a_name},{a_param},,{a_type}")
        print()
 
results, op_set = parse()
#wrt(results, op_set)               


pth_out = os.path.join(pname, fname_out)
with open(pth_out, 'w') as f:
    sys.stdout = f
    wrt(results, op_set)   
    sys.stdout = sys.__stdout__

#sys.stdout = sys.__stdout__
