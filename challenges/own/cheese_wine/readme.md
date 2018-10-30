# Gourmets' nightmare

A lot of gourmets struggle to find the perfect match of wine and cheese. 
A number of considerations are relevant, where each of them creates 
the unique combination, so finding the perfect match is a long-time assignment.  
Your assignment is not supposed to be long-time but it will use original but
scarry matching criteria.

You will match by similarity of a letter frequency in a name of wine and cheese.

                 sum of occurence of chars shared by both words
    similarity = ――――――――――――――――――――――――――――――――――――――――――――――
                 1 + square of length difference of both words

Examples:  
//ToDo

Upper and lower case variants are ignored in the mathing process.  
Space " ", dash "-", and aposthrope "'" are considered as valid chars.

3 lists of wine are provided (red, white, sparkling).  
You will match them with 43 cheeses mentioned in the in the "Cheese Shop" sketch  
(from Monty Python's Flying Circus  
http://montypython.wikia.com/wiki/Cheese_Shop_sketch )

Hint for sum of occurence of chars shared by both words:  
https://stackoverflow.com/questions/44012479/intersection-of-two-counters

Keywords: Counter , Operator, Multi key sort

ToDo:
- [ ] Examples of similarity
- [ ] Requirment: list of wines and 5 top matching cheeses
- [ ] Requirment: 3 best performing matches based on wine type (or absolute)
- [ ] Assignment file
- [ ] Solution file
- [ ] Test case file


