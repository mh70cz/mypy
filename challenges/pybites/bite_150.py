"""
Bite 150. Turn messy CSV into JSON 

https://codechalleng.es/bites/150

"""
 
import json
import re 

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""

def convert_to_json(members=members):
    
    reg = re.compile(r"[^,;|]+")

    lines = members.split("\n")
    keys = lines[1].split(",")
    
    members_lst = []
    for line in lines[2:-1]:
        member = reg.findall(line)        
        member_dct = dict(zip(keys, member))
        members_lst.append(member_dct )
    return json.dumps(members_lst)    

# without regex
def convert_to_json_(members=members):
    
    lines = members.split("\n")
    keys = lines[1].split(",")
    
    members_lst = []
    for line in lines[2:-1]:
        member = []
        wrk = ""
        for c in line:
            if c not in ";,|":
                wrk += c
            else:
                member.append(wrk)
                wrk = ""
        member.append(wrk)
            
        member_dct = dict(zip(keys, member))
        members_lst.append(member_dct )
    return json.dumps(members_lst)    
        
    
            
                
        