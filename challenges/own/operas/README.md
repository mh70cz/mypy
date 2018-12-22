#Contemporary Composers

You are given a list of `operas` and a list of `composers`.  
For two given composers find operas (where one of the composers is the author) at which premiere both could have been together (i.e. they both had to be alive).  Consider just a theoretical possibility of presence, so omit health condition, traveling problems, resources, and any other problems (excluding death) which could restrict their presence.  

The list of `operas` has the following structure:   
composer id, Title, date of premiere.  
The list of `composers` contains dictionaries, where each dictionary has the following structure:  
key: composer id  
value: composer's name, date of birth, date of death  

---
### Task
Complete the function `operas_both_at_premiere(guest, composers, operas)`.   
Parameters:   
guest - one of the composers but not the author of an opera  
composer - the author of an opera  
operas - list of operas  
If the required composer or guest is not in the list of composers, raise a ValueError exception.

Returns a list of titles of operas.

---
Note that the list of operas in the pyBite is shortened.  
Sources:  
https://en.wikipedia.org/wiki/List_of_operas_by_Wolfgang_Amadeus_Mozart
https://en.wikipedia.org/wiki/List_of_compositions_by_Ludwig_van_Beethoven
https://en.wikipedia.org/wiki/List_of_works_for_the_stage_by_Richard_Wagner
https://en.wikipedia.org/wiki/List_of_compositions_by_Giuseppe_Verdi
