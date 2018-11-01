# Bloodtypes
Check red blood cell compatibility between donor and recipient.  
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility

For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:  
- pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
- value of the pre-defined Bloodtype 1..7
- pre defined text  e.g. "0-", "B+", "AB+", ...
    

---
### Tasks
Complete the method *check_bt* .
The method should check red blood cell compatibility between a donor and a recipient.

Returns True for compatibility between the donor and the recipient, False otherwise.

If the input value is not a required type raise TypeError .
If the input value is not in the defined interval raise ValueError .

---
Keywords: enum, exception handling, multi type input