"""

"""
import xml.etree.ElementTree as ET
import os
import sys


pname = r'C:\Users\m.houska\Documents\_CIS\Toyota'

#fname_in= "strategy02.xml"
#fname_out = "strategy02.csv"

#fname_in= "strategy36.xml"
#fname_out = "strategy36.csv"

fname_in= "strategy79.xml"
fname_out = "strategy79.csv"



xmlpath = os.path.join(pname, fname_in)
tree = ET.parse(xmlpath)
root = tree.getroot()

#https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
namespaces = {'xsi': "http://www.w3.org/2001/XMLSchema-instance"} # add more as needed
conditions = root.findall(".//BaseProcess[@xsi:type='Condition']", namespaces)


def trfa (bp, tf):      
    uid = bp.attrib["uid"]
    processName =bp.find("./processName").text
    process_type = list(bp.attrib.values())[0] #xsi:type
    print(f"{tf}:")
    print(f"action:,{processName},{uid},{process_type}")        
    if process_type == "Result":
        r_name = bp.find("./exprMapping/BaseExpression/name").text
        r_param = bp.find("./exprMapping/BaseExpression/param").text
        r_type = bp.find("./exprMapping/BaseExpression/Type").text
        print(f"expressionFunc:,{r_name},{r_param},{r_type}")
        bes = bp.findall("./exprMapping/BaseExpression/arguments/BaseExpression")
        if not(bes is None):
            for idx, be in enumerate(bes):
                a_name = be.find("./name").text
                a_param = be.find("./param").text
                a_type = be.find("./Type").text
                print(f"arg ${idx},{a_name},{a_param},{a_type}")


def parse():
    for c in conditions:
        uid = c.attrib["uid"]
        processName =c.find("./processName").text
        
        test = c.find("./test")
        test_name = test.find("./name").text
        test_param = test.find("./param").text
        test_type = test.find("./Type").text
    
    
            
        print(f"action:,{processName},{uid},Condition ")
        print(f"test :,{test_name},{test_param},{test_type}")
        
        bes = test.findall("./arguments/BaseExpression")
        if not(bes is None):
            for idx, be in enumerate(bes):
                a_name = be.find("./name").text
                a_param = be.find("./param").text
                a_type = be.find("./Type").text
                print(f"arg ${idx} ,{a_name},{a_param},{a_type}")
        
        iftrue_bp = c.find("./iftrue/BaseProcess")
        iffalse_bp = c.find("./iffalse/BaseProcess")
        
    
        if not(iftrue_bp is None):
            trfa (iftrue_bp, "True")
        if not(iffalse_bp is None):  
            trfa (iffalse_bp, "False")
        print()

#parse()


pth_out = os.path.join(pname, fname_out)
with open(pth_out, 'w') as f:
    sys.stdout = f
    parse()
    sys.stdout = sys.__stdout__

#sys.stdout = sys.__stdout__
