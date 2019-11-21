"""

"""
import xml.etree.ElementTree as ET
import os
import sys


pname = r'C:\Users\m.houska\Documents\_CIS\Toyota'

#fname_in= "strategy02.xml"
#fname_out = "res02.csv"

#fname_in= "strategy36.xml"
#fname_out = "res36.csv"

fname_in= "strategy79.xml"
fname_out = "res79.csv"



xmlpath = os.path.join(pname, fname_in)
tree = ET.parse(xmlpath)
root = tree.getroot()

#https://stackoverflow.com/questions/14853243/parsing-xml-with-namespace-in-python-via-elementtree
namespaces = {'xsi': "http://www.w3.org/2001/XMLSchema-instance"} # add more as needed
results = root.findall(".//BaseProcess[@xsi:type='Result']", namespaces)


def parse():
    for r in results:
        uid = r.attrib["uid"]
        processName =r.find("./processName").text
        print(f"action:,{processName},{uid},Result")  
        bes = r.findall("./exprMapping/BaseExpression")    
        if not(bes is None):
            for idx, be in enumerate(bes):
                name = be.find("./name").text
                param = be.find("./param").text
                type_ = be.find("./Type").text
                print(f"ExpConst {idx}: ,{name},{param},{type_}")
                args = be.findall("./arguments/BaseExpression")
                if not(args is None):
                    for idx, a in enumerate(args):
                        a_name = a.find("./name").text
                        a_param = a.find("./param").text
                        a_type = a.find("./Type").text
                        print(f"arg ${idx}: ,{a_name},{a_param},{a_type}")                        
                            
        print()

parse()


#pth_out = os.path.join(pname, fname_out)
#with open(pth_out, 'w') as f:
#    sys.stdout = f
#    parse()
#    sys.stdout = sys.__stdout__

#sys.stdout = sys.__stdout__
