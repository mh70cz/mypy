"""

"""
import xml.etree.ElementTree as ET
import os
from collections import namedtuple

"""
"28510101.xml" CI CEE

"""

fname= "28510101_2.xml"
path = r'C:\Users\m.houska\Documents\_CIS\Toyota\GlobalReport'
xmlpath = os.path.join(path, fname)

tree = ET.parse(xmlpath)

ns = {'ur': 'https://ws.urplus.sk"',
      'grpt': "urn:crif-cribiscz-GetGlobalReport:2013-05-03"}

def clean_street_zip(subject):
    street_number = subject.get("HomeAddressStreet_Number")    
    street =  subject.get("HomeAddressStreet_Raw")
    zip_ = subject.get("HomeAddressZip")
    
    if (street is not None) and (street_number is not None):
        if (street_number in street):
            subject["HomeAddressStreet"] = street
        else:
            subject["HomeAddressStreet"] = street + " " + street_number 
        
    elif (street is None) and (street_number is not None):
        subject["HomeAddressStreet"] = street_number 
        
    elif street is not None:
        subject["HomeAddressStreet"] = street
        
    if zip_ is not None:
        subject["HomeAddressZip"] = zip_.replace(" ", "")


root = tree.getroot()

outer_Data = root.find(".//Responses/Response/Data")
# CompanyGlobalReport = outer_Data.find(".//{urn:crif-cribiscz-GetGlobalReport:2013-05-03}CompanyGlobalReport")


cgr = outer_Data.find(".//grpt:CompanyGlobalReport", ns)  #CompanyGlobalReport
 
e = cgr.find(".//grpt:CompanyIdentification/grpt:Name", ns)
if e is not None:
    applicant_trade_name = e.text
else:
    applicant_trade_name = None
 
    
applicant_parse =    {
    "TradeName": "grpt:Name",
    "RegistrationOfficeType": "grpt:DistrictCourt",
    "RegistrationSectionFileNo": "grpt:InsertNumber",
    "RegistrationOfficeName_District": "grpt:District",
    "RegistrationOfficeName_Region": "grpt:Region",
    "AresORDateEntry": "grpt:DateOfCreation" , #BusinessCreation??
    "TaxRegistrationNumber": "grpt:VATID",
    "PhoneNumber": "grpt:PhoneNumbers/grpt:PhoneNumber[1]/grpt:Number",
    "Email": "grpt:Email",
    "Bank_Acc_Raw": "grpt:BankInfoList/grpt:BankInfo[1]/grpt:Value",
    "Bank_Acc_Type": "grpt:BankInfoList/grpt:BankInfo[1]/grpt:Type",
    "Bank_Acc_InacInd": "grpt:BankInfoList/grpt:BankInfo[1]/grpt:InacInd",
    "HomeAddressStreet_Raw": "grpt:Seat/grpt:Street",
    "HomeAddressStreet_Number": "grpt:Seat/grpt:StreetNumber",
    "HomeAddressCity": "grpt:Seat/grpt:City",
    "HomeAddressZip": "grpt:Seat/grpt:Zip",
    "HomeAddressState": "grpt:Seat/grpt:Country",
}



app = cgr.find("./grpt:CompanyIdentification", ns)
applicant = {}

for item in applicant_parse:
    e = app.find("./" + applicant_parse[item], ns)
    if e is not None:
        applicant[item] = e.text
        
# RegistrationOfficeName
ro_district =  applicant.get("RegistrationOfficeName_District")
ro_region =  applicant.get("RegistrationOfficeName_Region")

if (ro_district is not None) and (ro_region is not None):
    if (ro_district.lower() in ro_region.lower() ) or (ro_region.lower() in ro_district.lower()):
        if len(ro_district) > len(ro_region):
            applicant["RegistrationOfficeName"] = ro_district
        else:
           applicant["RegistrationOfficeName"] = ro_region 
    else:
        applicant["RegistrationOfficeName"] = ro_region + ", " + ro_district
        
elif ro_region is not None:
    applicant["RegistrationOfficeName"] = ro_region

elif ro_district is not None:
    applicant["RegistrationOfficeName"] = ro_district     
    


#předčíslí, čílo účtu, kod banky
acc_type = applicant.get("Bank_Acc_Type")
acc_inac_ind = applicant.get("Bank_Acc_InacInd")          
if acc_type == "05" and acc_inac_ind == "00":
    bank_acc_raw = applicant.get("Bank_Acc_Raw")
    bank_acc_raw_split =  bank_acc_raw.split("/")
    applicant["BankCode"] = bank_acc_raw_split[1]
    account_split = bank_acc_raw_split[0].split("-")
    if len(account_split) == 2:
        applicant["BankAccountNumber1"] = account_split[0] #předčíslí
        applicant["BankAccountNumber"] = account_split[1] #číslo účtu 
    else:        
        applicant["BankAccountNumber"] = account_split[0]
        

clean_street_zip(applicant)    
#print (applicant)    
    

statutory_parse =    {
    "Name": "grpt:Name",
    "Surname": "grpt:Surname",
    "HomeAddressStreet_Raw": "grpt:Address/grpt:Street",
    "HomeAddressStreet_Number": "grpt:Address/grpt:StreetNumber",
    "HomeAddressState": "grpt:Address/grpt:Country",
    "HomeAddressZip": "grpt:Address/grpt:Zip",
    "DateOfBirth": "grpt:DateOfBirth"
} 


# stat = cgr.find("./grpt:OtherCompanyInformation/grpt:StatutoryList/grpt:Statutory[1]", ns)
stats = cgr.find("./grpt:OtherCompanyInformation/grpt:StatutoryList", ns)
statutories = {}
for idx, stat in enumerate(stats):
    statutory = {}
    for item in statutory_parse:
        e = stat.find("./" + statutory_parse[item], ns)
        if e is not None:
            statutory[item] = e.text
    clean_street_zip(statutory)
    statutories[str(idx)] = statutory
    
    



#CompanyGlobalReport = root.find("")

# /CN_Res_Direct/Responses/Response/Data

# [namespace-uri()='https://ws.urplus.sk' and local-name()='CribisGetGlobalReportResponse'][1]/*[namespace-uri()='https://ws.urplus.sk' and local-name()='CribisGetGlobalReportResult'][1]/*[namespace-uri()='https://ws.urplus.sk' and local-name()='Data'][1]/*[namespace-uri()='urn:crif-cribiscz-GetGlobalReport:2013-05-03' and local-name()='CompanyGlobalReport'][1]
