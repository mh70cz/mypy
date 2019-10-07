# -*- coding: utf-8 -*-
"""
Bite 213. Code a translation fixer
"""
import re


org_text = '''<p>Iterate over the given <code>names</code> and <code>countries list</code>s, <strong>printing</strong> them prepending the number of the loop (starting at 1). Here is the output you need to deliver:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Notice that the 2nd column should have a fixed width of 11 chars, so between <i>Julian</i> and <i>Australia</i> there are 5 spaces, between <i>Bob</i> and <i>Spain</i>, there are 8. This column should also be aligned to the left.</p><p>Ideally you use only one for loop, but that is not a requirement.</p><p>Good luck and keep calm and code in Python!</p>'''
trans_text = '''<p>Iterare i <code>nomi</code> e le <code>liste dei paesi</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre> 1. Julian Australia 2. Bob Spagna 3. PyBites Global 4. Dante Argentina 5. Martin Stati Uniti d'America 6. Rodolfo Messico </pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''
fixed = '''<p>Iterare i <code>names</code> e le <code>countries list</code>s indicati, <strong>stampandoli</strong> anteponendo il numero del ciclo (a partire da 1). Ecco l'output che devi consegnare:<pre>
1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
</pre></p><p>Si noti che la seconda colonna dovrebbe avere una larghezza fissa di 11 caratteri, quindi tra <i>Julian</i> e <i>Australia</i> ci sono 5 spazi, tra <i>Bob</i> e <i>Spagna</i> , ci sono 8. Questa colonna dovrebbe anche essere allineata a sinistra. </p><p>Idealmente si utilizza solo uno for loop, ma questo non è un requisito. </p><p>Buona fortuna e mantenere la calma e codice in Python! </p>'''


def fix_translation(org_text, trans_text):
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    r = re.compile(r"<code>.*?<\/code>|<pre>.*?<\/pre>", re.DOTALL)
    find_lst=r.findall(org_text)
    split_lst=r.split(trans_text)    

    return "".join([x[0] + x[1] for x in zip(split_lst,find_lst)]) + split_lst[-1]

def gen():
    for i in range(100,0,-1):
        yield i
        
g = gen()
for j in range(101):
    print(next(g))


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    r = re.compile(r"PB(-[A-Z0-9]{8}){4}")
    
    bool(r.match('PB-HJD5FTUY-OM0KYDXI-WXTPGI3E-B7FV8E63A'))
