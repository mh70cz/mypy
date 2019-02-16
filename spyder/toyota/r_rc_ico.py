# -*- coding: utf-8 -*-
"""
random sex, PIN, dat nar, IČO
"""

import random


def rc_dat():
    r_sex = random.choice(["M","Z"])
    r_day = str(random.randint(1,28))
    r_month = random.randint(1,12)
    r_year = random.randint(1920, 2000)
    
    dat_nar = f"{r_day}. {str(r_month)}. {r_year}" 
  
    r_seq = str(random.randint(0, 999)).zfill(3)
    r_day = r_day.zfill(2)
    if r_sex == "Z":
        r_month = r_month + 50
    r_month = str(r_month).zfill(2)    
            
    pin = str(r_year)[2:] + r_month + r_day + r_seq
    
    if r_year >= 1954:
        check = (int(pin) % 11) % 10
        pin = pin + str(check)
    return (r_sex, pin, dat_nar)

def r_ico():
    ico_raw = str(random.randint(1_000, 9_999_999)).zfill(7)
    suma = 0
    for i in range(0,7):
        w = 8-i
        suma += w*int(ico_raw[i])
    check = (suma % 11) % 10    
    ico = ico_raw + str(check)
    return ico

"""
for i in range (0,111111):
    

    sex, rc, dat_nar = rc_dat()
    is_rc_valid = validate_RC.validate(rc)
    
    
    ico = r_ico()
    is_ico_valid = validate_ICO.validate(ico)


    if not is_rc_valid:
        print(rc)

    if not is_ico_valid:
        print(ico)

"""
