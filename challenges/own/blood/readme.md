# Bloodtypes
Check red blood cell compatibility between donor and recipient.  


For simplicity, the appearance of 8 basic types of blood is considered.
The input of blood type can be in the form of:  
- pre defined Bloodtype enum e.g.: Bloodtype.ZERO_NEG
- value of the pre-defined Bloodtype 1..7
- pre defined text  e.g. "0-", "B+", "AB+", ...
---
There are 8 basic blood types based on presence/absence of these 3 antigens: A, B, and Rh-D. 
Presence of the A antigen is marked as A in a blood type.  
Presence of the B antigen is marked as B in a blood type.  
Presence/absence od the Rh-D antigen is marked as +/-  
0- no antigen  
0+ Rh-D antigen  
A- antigen A  
A+ antigen A and Rh-D  
B- antigen B  
B+ antigen B and Rh-D  
AB- antigen A and B  
AB+ all 3 antigens (A, B, Rh-D)  

---
General rule:
### An individual who does not have a certain antigen cannot receive a blood from someone who has this antigen.

*Blood group 0*  individuals do not have either A or B antigens.  Therefore, a group 0 individual can receive blood only from a group 0 individual, but can donate blood to individuals  A, B, 0. or AB.

*Blood group A* individuals have the A antigen. Therefore, a group A individual can receive blood only from individuals of groups A or 0, and can donate blood to individuals with type A or AB.   

*Blood group B* individuals have the B antigen. Therefore, a group B individual can receive blood only from individuals of groups B or 0 , and can donate blood to individuals with type B or AB.  

*Blood group AB* individuals have both A and B antigens. Therefore, an individual with type AB blood can receive blood from AB0, but cannot donate blood to any group other than AB. 

*Rh-D negative* individuals do not have Rh-D antigen. Therefore, Rh-D negative can receive blood only from other Rh-D negative individuals.

*Rh-D positive* individuals have Rh-D antigen. Therefore, Rh-D positive individual can receive blood from both Rh-D negative or positive individuals.

Individuals with 0- are universal donors. Individuals with AB+ are universal recipients.
 
The rules described are general. In real over 340 different blood-group antigens have been found. For additional info you can see:  
https://en.wikipedia.org/wiki/Blood_type#Red_blood_cell_compatibility  
             
---
### Tasks
Complete the method *check_bt* .
The method should check red blood cell compatibility between a donor and a recipient.

Returns True for compatibility between the donor and the recipient, False otherwise.

If the input value is not a required type raise TypeError .
If the input value is not in the defined interval raise ValueError .

---
Keywords: enum, exception handling, multi type input