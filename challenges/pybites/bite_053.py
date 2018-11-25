"""
 Bite 53. Convert text into multiple columns 

https://codechalleng.es/bites/53
"""
from itertools import zip_longest
 
COL_WIDTH = 20
COL_SPACE = 5

def splitter(text):
    words = text.split(" ")
    lines = []
    line = words[0]
    for w in words[1:]:
        if (len(line) + len(w)) < COL_WIDTH:
            line = line + " " + w
        else:
            lines.append(line)
            line = w
    lines.append(line)
    return lines

def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    parags = text.split("\n\n")
    blocks = []
    for p in parags:
        block = splitter(p)
        blocks.append(block)
    output = ""
    for linechunks in zip_longest(*blocks, fillvalue=""):
        line = ""
        for lc in linechunks[:-1]:
            line += lc + (COL_WIDTH + COL_SPACE - len(lc)) * " "
        line += linechunks[-1]
        output += line + "\n"
    return output
        
    
                
            
    