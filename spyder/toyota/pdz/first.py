
import os
from bs4 import BeautifulSoup as Soup
import bs4

pathp = r'C:\Users\m.houska\OneDrive\scripts\py\spyder\toyota\pdz'
fname = "L1807183WI73KKP.html"

p = os.path.join(pathp, fname)
print(p)

with open(p, encoding='utf-8') as f:
    #s = f.read().decode('utf-8', 'ignore')
    soup = Soup(f, "html.parser")
    rqu = soup.find("div", attrs={"class" : "c"})
    
    l = list(rqu.children)
    
    def iteruj():
        att_names = []
        att_values = []
        
        for idx, e in enumerate(l):
            if isinstance(e, bs4.element.Tag):
                #print(e.name)
                if e.name == "span":
                    #print(e.name)
                    a = e.attrs
                    #print(a)
                    x = a.get("class", None)
                    if x == ["", "t", ""]:
                        e_name_open = e.contents[0].strip()
                    if x == ["", "t"]:
                        #print(e.contents[0].strip())
                        att_names.append(e.contents[0].strip())
                        #print (l[idx+1])
                        pass
                if e.name == "b":
                    att_values.append(e.contents[0].strip())
        #print(e_name_open)
        #print(att_names)
        #print(att_values)
        assert len(att_names) == len(att_values)
        z = zip(att_names, att_values)
        att_pairs = ""
        for nv in z:
            att_pairs += f" {nv[0]}=\"{nv[1]}\" "
        
        
        print(f"<{e_name_open} {att_pairs} >")