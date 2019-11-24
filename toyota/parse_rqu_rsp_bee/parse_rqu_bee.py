# -*- coding: utf-8 -*-
"""
@author: mh70 , Created on Wed Nov 20 19:38:07 2019
"""

import xml.etree.ElementTree as ET
from pathlib import Path


path = Path("C:/BEE_rqu/rqu_BEE_Live_spo")
path = path / "179756_IN__636991254658007845.xml"

# 178068_IN__636968843102397373
# 178248_IN__636975927369383673 -nrki delikvence

ns = {"cls":"uri:creditinfosolutions/cls",
      "nrki":None,
      'urp': 'https://ws.urplus.sk',
      'gr': 'urn:crif-cribiscz-GetGlobalReport:2013-05-03'}

def get_root(path):
    with open(path, encoding="utf-16le") as fp:  #utf-16le  utf-8
        tree = ET.parse(fp)
    root = tree.getroot()
    return root

def get_applicant(root):
    applicant_elem = root.find(".//cls:Applicant", ns)
    if applicant_elem is None:
        print("chybi applicant")
        return None
    return applicant_elem

def get_applicant_info(subj_elem):
    sub_type = ""
    sub_type_elem = subj_elem.find(".//cls:SubjType", ns)
    if sub_type_elem is not None:
        sub_type = sub_type_elem.text
        #print (subj_type_elem)
    ico = "" # zatim 2019-11-23 neni ve vstupu do BEE
    ico_elem = subj_elem.find(".//cls:Ico", ns)
    if ico_elem is not None:
        ico = ico_elem.text    
    
    out = {"sub_type": sub_type,
           "ico": ico,}
    
    return out


"""
root =  get_root(path)
applicant_elem = get_applicant(root)


contract_data =  get_nrki(applicant_elem)["contract_data"]
cbs = get_nrki_cbscore(contract_data)

lsd = get_lsd(applicant_elem, order="first")


gr = get_global_report(applicant_elem)["gr"]
gr_info = get_global_report_info(gr)

"""


def get_nrki(subj_elem):
    """ vrati CustomerData a ContractData
        problen s nrki: ns , etree nepodporuje(?) prazdny ns  nrki:""
        az bude provedena oprava ns v response z nrki konektoru nutno 
        - zadefinovat "nrki":"opraveny_ns"
        - zmenit volani find a findall find(".//nrki:CustomerData", ns)
    """
    nrki = subj_elem.find(".//cls:ConnectorNrki", ns)
    if nrki is None:
        return None
    
    if (nrki.attrib["status"] != "ok") and (nrki.attrib["cnavStatus"] != "100"):
        return None
    
    #cr_rep = find(".//CR_REP", ns)
    input_request = nrki.attrib["cnavStatus"]
    customer_data = subj_elem.find(".//CustomerData", ns)
    contract_data = subj_elem.find(".//ContractData", ns)
    
    return {"input_request": input_request,
            "customer_data": customer_data,
            "contract_data": contract_data}

def get_nrki_cbscore(contract_data):
    """ vrati CBScore z NRKI 
        na zaklade get_nrki(subj_elem)["contract_data"]
        ns viz docstring v get_nrki  """
    cbscore_out = {}
    cbscore = contract_data.find("CBScore", ns)
    cbscore_error_code, cbscore_error_desc = "", ""
    cbscore_error = cbscore.find("ScoreError", ns)
    if cbscore_error is not None:
        cbscore_error_code = cbscore_error.find("Code", ns).text
        cbscore_error_desc = cbscore_error.find("Description", ns).text
        cbscore_out["error_code"] = cbscore_error_code
        cbscore_out["error_desc"] = cbscore_error_desc
         
    cbscore_range = ""
    cbscore_detail = cbscore.find("ScoreDetails", ns)
    if cbscore_detail is not None:
        cbscore_range = cbscore_detail.find("CBSCoreRange", ns).text
        cbscore_raw = cbscore_detail.find("ScoreRaw", ns).text
        cbscore_out["cbscore_range"] = cbscore_range
        cbscore_out["cbscore_raw"] = cbscore_raw 
        
        cbscore_factor_elems = cbscore_detail.findall("ScoreFactor", ns)    
        for idx, e in enumerate(cbscore_factor_elems):
            sf_code = e.find("SFCode").text
            sf_desc = e.find("SFDescription").text
            cbscore_out["cbscore_factor_code_" + str(idx)] = sf_code
            cbscore_out["cbscore_factor_desc_" + str(idx)] = sf_desc
    
    return cbscore_out
        
        

def get_global_report(subj_elem):    
    gr = subj_elem.find(".//cls:ConnectorGlobalReport", ns)
    if gr is None:
        return None
    
    if (gr.attrib["status"] != "ok") and (gr.attrib["cnavStatus"] != "100"):
        return None  

    status_code = ""
    result_elem =  gr.find(".//urp:Status/urp:Code", ns)
    if result_elem is not None:
        status_code  = result_elem.text    
    
    out = {"status_code": status_code,
           "gr": gr}
    return out
    
def get_global_report_info(gr):
    """
    
    """    
    ico = ""
    ico_elems = gr.findall(".//gr:Ico", ns)
    if ico_elems:
        ico = ico_elems[0].text

    vatid = ""
    vatid_elems = gr.findall(".//gr:VATID", ns)
    if vatid_elems:
        vatid = vatid_elems[0].text

    num_statutories = 0
    statutory_list_elem = gr.find(".//gr:StatutoryList", ns)
    if statutory_list_elem is not None:
        statutories = statutory_list_elem.findall(".//gr:Statutory", ns)
        num_statutories = len(statutories)

    other_stat_facts = ""
    other_stat_facts_elems = gr.findall(".//gr:OtherStatutoryFacts", ns)
    if other_stat_facts_elems:
        other_stat_facts = other_stat_facts_elems[0].text

    out = {"ico": ico,
           "vatid": vatid,
           "num_statutories": num_statutories,
           "other_stat_facts": other_stat_facts,
           }
    return (out)    
    
def get_lsd(subj_elem, order="first"):
    
    conn_elem = ".//cls:ConnectorLsd_" + order
    
    lsd = subj_elem.find(conn_elem, ns)
    if lsd is None:
        return None
    
    if (lsd.attrib["status"] != "ok") and (lsd.attrib["cnavStatus"] != "100"):
        return None  

    status_code = ""
    result_elem =  lsd.find(".//urp:Status/urp:Code", ns)
    if result_elem is not None:
        status_code  = result_elem.text
        
    response_value = ""
    if status_code == "101":
        response_value_elem = lsd.find(".//urp:ResponseValue", ns)
        if response_value_elem is not None:
            response_value =response_value_elem.text
        
    
    out = {"status_code": status_code,
           "response_value": response_value,
           "lsd": lsd}
    return out



def get_vat_other_stat_facts(subj):
    """ deprecated """

    ico = ""
    ico_elems = subj.findall(".//gr:Ico", ns)
    if ico_elems:
        ico = ico_elems[0].text

    vatid = ""
    vatid_elems = subj.findall(".//gr:VATID", ns)
    if vatid_elems:
        vatid = vatid_elems[0].text


    #statutory_list = []
    num_statutories = 0
    statutory_list_elem = subj.find(".//gr:StatutoryList", ns)
    if statutory_list_elem is not None:
        statutories = statutory_list_elem.findall(".//gr:Statutory", ns)
        num_statutories = len(statutories)

    other_stat_facts = ""
    other_stat_facts_elems = subj.findall(".//gr:OtherStatutoryFacts", ns)
    if other_stat_facts_elems:
        other_stat_facts = other_stat_facts_elems[0].text

    out = {"ico": ico,
           "vatid": vatid,
           "num_statutories": num_statutories,
           "other_stat_facts": other_stat_facts,
           }
    return (out)

"""
StatutoryList
OtherStatutoryFacts

"""