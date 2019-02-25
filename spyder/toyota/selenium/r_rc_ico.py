# -*- coding: utf-8 -*-
"""
random sex, PIN, dat nar, IČO
"""

import random


def rc_dat(sex=None):
    if sex not in ["M", "F", "Z"]:        
        sex = random.choice(["M","Z"])
    elif sex == "F":
        sex = "Z"        
    r_day = str(random.randint(1,28))
    r_month = random.randint(1,12)
    r_year = random.randint(1945, 2000)
    
    dat_nar = f"{r_day}.{str(r_month)}.{r_year}" 
  
    day = r_day.zfill(2)
    month = r_month
    if sex == "Z":
        month = r_month + 50
    month = str(month).zfill(2)    
            
        
    while True:
        r_seq = str(random.randint(0, 999)).zfill(3)
        pin = str(r_year)[2:] + month + day + r_seq
        if r_year >= 1954:
            check = (int(pin) % 11) % 10
            pin = pin + str(check)
            
            suma = 0
            for n in pin:
                suma += int(n)
            if int(suma) % 11 != 0:
                #print(pin)
                continue # nevracej čísla s výjimkou 
            else:
                break
        else:
            break
    return (sex, pin, dat_nar)

def r_ico():
    ico_raw = str(random.randint(1_000, 9_999_999)).zfill(7)
    suma = 0
    for i in range(0,7):
        w = 8-i
        suma += w*int(ico_raw[i])
    check = (11 -(suma % 11)) % 10    
    ico = ico_raw + str(check)
    return ico

"""
for i in range (10):
    print (str(i) + rc_dat())
    
    
for i in range (10):
    

    sex, rc, dat_nar = rc_dat()
    is_rc_valid = validate_RC.validate(rc)
    
    
    ico = r_ico()
    is_ico_valid = validate_ICO.validate(ico)


    if not is_rc_valid:
        print(rc)

    if not is_ico_valid:
        print(ico)
        
     
    27600297    69663963
        
    8025436

"""
for i in range(1000):
    ico = r_ico()

        