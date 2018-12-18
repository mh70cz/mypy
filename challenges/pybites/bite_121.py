"""
Bite 121. Determine the strength of a password 

https://codechalleng.es/bites/121


    Password has both lower- and uppercase letters,
    Password contains one or more numbers in addition to one or more characters,
    Password has one or more special characters,
    Password has a minimum length of 8 characters,
    Password starting 8 chars ("long enough") that doesn't have repeating characters ('1234abcd' = good, '1234abbd' = bad)


"""
 
import re


def password_complexity(password):
    """Input: password string, calculate score according to 5 criteria in bite,
       return: score int"""
    strength_counter = 0
    
    
    reg_lower = re.compile(r"[a-z]")
    reg_upper = re.compile(r"[A-Z]")
    reg_number = re.compile(r"[0-9]")
    reg_special = re.compile(r"[@$]")
    reg_consrep = re.compile(r"(.)\1{1,}") #consecutive repeated character ({1,} - repeated char 1 or more times)
    
    if bool(reg_lower.search(password)) and bool(reg_upper.search(password)):
        strength_counter+= 1
    if (bool(reg_lower.search(password)) or
        bool(reg_upper.search(password))) and bool(reg_number.search(password)) :
        strength_counter+= 1
    if bool(reg_special.search(password)):
        strength_counter+= 1        
    
    
    if len(password) >= 8:
        strength_counter += 1
        if not bool(reg_consrep.search(password)):
            strength_counter+= 1 
    return strength_counter