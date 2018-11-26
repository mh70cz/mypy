"""

"""
import xml.etree.ElementTree as ET
import os
from collections import namedtuple

"""
154760.xml
154801.xml
155099.xml 
155583.xml
155849.xml
155854.xml
155865.xml
155889.xml
155905.xml
155921.xml

"""

fname= "155921.xml"
path = r'C:\Users\m.houska\Documents\_CIS\Toyota\NRKI_CZE_Live'
xmlpath = os.path.join(path, fname)

Inst = namedtuple("Inst", "ra_as mia_as ra_r mia_r")
Noinst = namedtuple("Noinst", "cl_as ut_as cl_r ut_r")
Cards = namedtuple("Cards", "ra_as mia_as cl_as ra_r mia_r cl_r")

Inst24 = namedtuple("Inst24", "max_due_amount max_days_past_due" )
Noinst24 = namedtuple("Noinst24", "max_days_past_due" )
Cards24 = namedtuple("Cards24", "max_due_amount max_days_past_due")

tree = ET.parse(xmlpath)
root = tree.getroot()

fi_pc_rqu = root.find(".//CustomerData/ReqCustomer/Customer/FIPersonalCode")
#ccb_pc_rqu = root.find(".//CustomerData/ReqCustomer/Customer/CCBPersonalCode") 
fi_pc_rsp = root.find(".//CustomerData/FoundCustomer/Customer/FIPersonalCode")
ccb_pc_rsp = root.find(".//CustomerData/FoundCustomer/Customer/CCBPersonalCode") 




def get_type_of_query():
    function_code_elem = root.find(".//Header/FunctionCode")
    if function_code_elem is not None:
        function_code = function_code_elem.text
    else:
        function_code = "not_found"
    query_types = {"01001":"RI_REQ",
                   "02001":"EC_REQ",
                   "03001":"CI_REQ" ,                   
                   "not_found":"not found in repsonse"
            }
    
    return query_types.get(function_code, "unknown query type " + str(function_code))        

def get_score_values():

    score_detail = root.find(".//ContractData/CBScore/ScoreDetails")
    if score_detail:
        score_raw = score_detail.find("./ScoreRaw").text
        cbs_core_range =  score_detail.find("./CBSCoreRange").text
        score_factor =  score_detail.findall(".//ScoreFactor")
        #sf_code = score_detail.findall(".//SFCode")
        #sf_description = score_detail.findall(".//SFDescription")
    else:
        score_raw = None
        cbs_core_range = None
        score_factor = None    
    score_error = root.find(".//ContractData/CBScore/ScoreError")
    
    
    #print(score_raw, cbs_core_range, sf_code, sf_description)
    return (score_raw, cbs_core_range, score_factor, score_error)        


def get_installments():
    """ bez stavebního spoření"""
    inst_detail = root.findall(".//ContractData/Installments/InstDetail")        
    ra_as = 0   #residaul amount dlužník (A,S)
    mia_as = 0  #monthly installment amount dlužník (A,S)
    ra_r = 0    #residaul amount ručitel (R)
    mia_r = 0   #monthly installment amount ručitel (R) 
    for e in inst_detail:
        if e.findall("./CommonData/[OpPhase='EX']"):
            if e.findall("./CommonData/[Role='A']") or e.findall("./CommonData/[Role='S']"):
                ra = e.find("./ResidualAmount").text
                mia= e.find("./MonthlyInstalmentAmount").text
                ra_as += int(ra)
                mia_as += int(mia)
            if e.findall("./CommonData/[Role='R']"):
                ra = e.find("./ResidualAmount").text
                mia= e.find("./MonthlyInstalmentAmount").text
                ra_r += int(ra)
                mia_r += int(mia)
#    print(f"residual amount dlužník:            {ra_as}")
#    print(f"residual amount ručitel:            {ra_r}")
#    print(f"monthly installment amount dlužník: {mia_as}")
#    print(f"monthly installment amount ručitel: {mia_r}")   
    return Inst(ra_as, mia_as, ra_r, mia_r)
    
            
        
def get_cards(st="exclude"):
    card_detail = root.findall(".//ContractData/Cards/CardDetail")        
    ra_as = 0   #residaul amount dlužník (A,S)
    mia_as = 0  #monthly installment amount dlužník (A,S)
    cl_as = 0   #credit Limit dlužník (A,S)
    ra_r = 0    #residaul amount ručitel (R)
    mia_r = 0   #monthly installment amount ručitel (R) 
    cl_r = 0    #credit Limit ručitel (R)
    for e in card_detail:
        if e.findall("./CommonData/[OpPhase='EX']"):
            op_type = e.find("./CommonData/OpType").text
            if st == "exclude":  #bez staveb sporeni
                if op_type == "ST":
                    continue
            if st == "only":     #pouze staveb sporeni
                if not op_type == "ST":
                    continue                
            if e.findall("./CommonData/[Role='A']") or e.findall("./CommonData/[Role='S']"):
                ra = e.find("./ResidualAmount").text
                mia = e.find("./MonthlyInstalmentAmount").text
                cl = e.find("./CreditLimit").text
                ra_as += int(ra)
                mia_as += int(mia)
                cl_as += int(cl)
            if e.findall("./CommonData/[Role='R']"):
                ra = e.find("./ResidualAmount").text
                mia= e.find("./MonthlyInstalmentAmount").text
                cl = e.find("./CreditLimit").text
                ra_r += int(ra)
                mia_r += int(mia)
                cl_r += int(cl)
#    print(f"residual amount dlužník:            {ra_as}")
#    print(f"residual amount ručitel:            {ra_r}")
#    print(f"credit limit dlužník:               {cl_as}")
#    print(f"credit limit ručitel:               {cl_r}")    
#    print(f"monthly installment amount dlužník: {mia_as}")
#    print(f"monthly installment amount ručitel: {mia_r}")   
    return Cards(ra_as, mia_as, cl_as, ra_r, mia_r, cl_r)



def get_no_installments():
    noinst = root.find(".//ContractData/NoInstallments")
    
    #credit Limit dlužník (A,S)
    cl_as = int(noinst.find("./ACNoInstAmounts/NoInstAmounts/CreditLimit").text)    
    #utilization dlužník (A,S)
    ut_as = int(noinst.find("./ACNoInstAmounts/NoInstAmounts/Utilization").text)
    #credit Limit ručitel (R)
    cl_r = int(noinst.find("./GNoInstAmounts/NoInstAmounts/CreditLimit").text)
    #utilization ručitel (R)
    ut_r = int(noinst.find("./GNoInstAmounts/NoInstAmounts/Utilization").text)
    
    
#    print(f"credit Limit dlužník:               {cl_as}")
#    print(f"credit Limit ručitel:               {cl_r}")
#    print(f"utilization dlužník:                {ut_as}")
#    print(f"utilization ručitel:                {ut_r}")   
    
    return Noinst(cl_as, ut_as, cl_r, ut_r)

def get_installments_24():
    inst_detail = root.findall(".//ContractData/Installments/InstDetail") 
    
    due_amount = []
    days_past_due = []
    for e in inst_detail:
        role = e.find("./CommonData/Role").text
        if not (role  == "A" or role == "S"):
            continue
        profile = e.findall("./InstProfile")
        if profile is None:
            continue
        for p in profile:
            da = p.find("./DueAmount").text
            due_amount.append(da)
            dpd = p.find("./DaysPastDue")
            if dpd is not None: #nepovinné pole
                days_past_due.append(dpd.text)
    if due_amount:            
        max_due_amount = max([(int(x)) for x in due_amount if x is not None])
    else:
        max_due_amount = 0
    if days_past_due:
        max_days_past_due = max([(int(x)) for x in days_past_due if x is not None])
    else:
        max_days_past_due = 0
    return Inst24(max_due_amount, max_days_past_due)
        
            

def get_no_installments_24():
    inst_detail = root.findall(".//ContractData/NoInstallments/NoInstDetail") 
    
    days_past_due = []
    for e in inst_detail:
        role = e.find("./CommonData/Role").text
        if not (role  == "A" or role == "S"):
            continue
        profile = e.findall("./NoInstProfile")
        if profile is None:
            continue
        for p in profile:
            dpd = p.find("./DaysPastDue")
            if dpd is not None: #nepovinné pole
                days_past_due.append(dpd.text)
    if days_past_due:
        max_days_past_due = max([(int(x)) for x in days_past_due if x is not None])
    else:
        max_days_past_due = 0
    return Noinst24( max_days_past_due)

    
def get_cards_24(st="exclude"):
    inst_detail = root.findall(".//ContractData/Cards/CardDetail") 
    
    due_amount = []
    days_past_due = []
    for e in inst_detail:
        role = e.find("./CommonData/Role").text
        if not (role  == "A" or role == "S"):
            continue
        op_type = e.find("./CommonData/OpType").text
        if st == "exclude": #bez staveb sporeni
            if op_type == "ST":
                continue
        if st == "only": #pouze staveb sporeni
            if not op_type == "ST":
                continue          
        profile = e.findall("./CardProfile")
        if profile is None:
            continue
        for p in profile:
            da = p.find("./DueAmount").text
            due_amount.append(da)
            dpd = p.find("./DaysPastDue")
            if dpd is not None: #nepovinné pole
                days_past_due.append(dpd.text)
    if due_amount:            
        max_due_amount = max([(int(x)) for x in due_amount if x is not None])
    else:
        max_due_amount = 0
    if days_past_due:
        max_days_past_due = max([(int(x)) for x in days_past_due if x is not None])
    else:
        max_days_past_due = 0
    return Cards24(max_due_amount, max_days_past_due)
        
print("*****************************************\n")
print(f"File name:               {fname}")

score_raw, cbs_core_range, score_factor, score_error = get_score_values()

print(f"FIPersonalCode CIS     : {fi_pc_rqu.text if fi_pc_rqu is not None else ''}")
print(f"CCBPersonalCode CRIF   : {ccb_pc_rsp.text if ccb_pc_rsp is not None else ''}")
print(f"FIPersonalCode CRIF    : {fi_pc_rsp.text if fi_pc_rsp is not None else ''}")
print(f"Type of query          : {get_type_of_query()}")

if score_error:    
    print(f"Score error Code       : {score_error[0].text}")
    print(f"Score error Description: {score_error[1].text}")   
else:    
    print(f"ScoreRaw               : {score_raw}")
    print(f"CBSCoreRange           : {cbs_core_range}")
    
    for sf in score_factor:
        print(f"SFCode                 : {sf[0].text}")
        print(f"SFDescription          : {sf[1].text}")  


inst_without_st = get_installments()
cards_only_st = get_cards(st="only") # pouze stavební spoření
ra_as = inst_without_st.ra_as + cards_only_st.ra_as
mia_as = inst_without_st.mia_as + cards_only_st.mia_as
ra_r = inst_without_st.ra_r + cards_only_st.ra_r
mia_r = inst_without_st.mia_r + cards_only_st.mia_r

inst = Inst(ra_as, mia_as, ra_r, mia_r)
cards = get_cards(st="exclude") # vyjma stavebního spoření
noinst = get_no_installments()

inst24_without_st = get_installments_24()
cards24_only_st = get_cards_24(st="only") # pouze stavební spoření
max_due_amount = inst24_without_st.max_due_amount + cards24_only_st.max_due_amount
max_days_past_due = inst24_without_st.max_days_past_due + cards24_only_st.max_days_past_due

inst24 = Inst24(max_due_amount, max_days_past_due)
cards24 = get_cards_24(st="exclude") # vyjma stavebního spoření
noinst24 = get_no_installments_24()

print("\n*********\nInstallment operations:")
print(f"residual amount dlužník:            {inst.ra_as}")
print(f"residual amount ručitel:            {inst.ra_r}")
print(f"monthly installment amount dlužník: {inst.mia_as}")
print(f"monthly installment amount ručitel: {inst.mia_r}")
print("Installment history 24 months:")
print(f"max due amount dlužník:             {inst24.max_due_amount}")
print(f"max days past due dlužník:          {inst24.max_days_past_due}")
print("\n*********\nCards:")
print(f"residual amount dlužník:            {cards.ra_as}")
print(f"residual amount ručitel:            {cards.ra_r}")
print(f"credit limit dlužník:               {cards.cl_as}")
print(f"credit limit ručitel:               {cards.cl_r}")    
print(f"monthly installment amount dlužník: {cards.mia_as}")
print(f"monthly installment amount ručitel: {cards.mia_r}") 
print("Cards history 24 months:")
print(f"max due amount dlužník:             {cards24.max_due_amount}")
print(f"max days past due dlužník:          {cards24.max_days_past_due}")
print("\n*********\nNoinstallment operations:")    
print(f"credit limit dlužník:               {noinst.cl_as}")
print(f"credit limit ručitel:               {noinst.cl_r}")
print(f"utilization dlužník:                {noinst.ut_as}")
print(f"utilization ručitel:                {noinst.ut_r}")   
print("Noinstallment history 24 months:")
print(f"max days past due dlužník:          {noinst24.max_days_past_due}")   
    