# -*- coding: utf-8 -*-
"""
process df 
"""

import re
import pandas as pd

SRO = "112"


def neg_match(string, legal_form_sro=True):
    neg_re_sro = ["společně",
              "(dvou|obou|všech).+jednatelů",
              "(výjimkou|pouze)",
              "(půjčka|půjčce|úvěr|úvěru|závazek|závazku)",
              "předseda[ ].{0,35}jednatelů",
              ]
    
    neg_re_nonsro = ["společně",
                     "(výjimkou|pouze)",
                     "(půjčka|půjčce|úvěr|úvěru|závazek|závazku)",
              ]
    
    if legal_form_sro:
        neg_re = neg_re_sro
    else:
        neg_re = neg_re_nonsro
        
    for regex in neg_re:
        match_obj = re.search(regex, string)
        if match_obj is not None:
            return "NEG", regex
    return "NF", ""                                                                                     


def pos_match(string):
    pos_re = ["jednatel[ů]?[ ].*(jedná|zastupuje|jednat|zastupovat|rozhoduje)[ ].*samostatně",
              "(jedná|jednat|zastupuje)[ ].*jednatel[ů]?[ ].*samostatně",
              "jednatelé[ ].*(jednají|zastupují|jednat|zastupovat)[ ].*samostatně",
              "jednají[ ].*jednatelé[ ].*samostatně",
            ]
    for regex in pos_re:
        match_obj = re.search(regex, string)
        if match_obj is not None:
            return "POS", regex
    return "NF", ""             

out = []        
for idx, row in df2.head(n=600).iterrows():
    if row["num_stat"] != 1:
        #print(idx, row["other_stat_facts"])
           
        other_stat_facts = row["other_stat_facts"].lower()
        status, regex = neg_match(other_stat_facts, (row["legal_form_cd"] == SRO))
        if (status != "NEG") and (row["legal_form_cd"] == SRO):
            status, regex = pos_match(other_stat_facts)
        #print (status + ": " + regex + "\n" + other_stat_facts)
        
        out_row = {
                   "status": status,
                   "regex": regex,
                   "other_stat_facts":row["other_stat_facts"],
                   "num_repr": row["num_repr"],
                   "num_stat": row["num_stat"],
                   "ico_gr": row["ico_gr"],
                   "legal_form_cd": row["legal_form_cd"],
                   "rqu_id_f": row["rqu_id_f"],
                }
        out.append(out_row)
         
df3 = pd.DataFrame(out)
     
""""
neg_re_bee = " | \n".join(['MATCH($_otherStatutoryFacts, "' + x + '")' for x in neg_re])
pos_re_bee = " | \n".join(['MATCH($_otherStatutoryFacts, "' + x + '")' for x in pos_re])

print(neg_re_bee)
print("\n\n")
print(pos_re_bee)


pos_re = ["jednatel[ů]?[ .].*(jedná|zastupuje|jednat|zastupovat|rozhoduje)[ .].*samostatně",
          "(jedná|zastupuje)[ .].*jednatel[ů]?[ .].*samostatně",
          "jednatelé[ .].*(jednají|zastupují|jednat|zastupovat)[ .].*samostatně",        
        ]


neg_re = ["společně",
          "(dvou|obou|všech).+jednatelů",
          "(výjimkou|pouze)",
          "(půjčka|půjčce|úvěr|úvěru)",
          ]

"""
