"""
Bite 179. Strip comments from Python code
"""
from string import whitespace

def strip_comments(code):
    code_ = strip_tq(code)
    code_2 = strip_h(code_)
    return code_2


def strip_tq(txt):
    tq_idx = []
    idx = 0    
    while idx < len(txt):
        try:
            idx = txt.index('"""', idx)
        except ValueError:
            break
        tq_idx.append(idx)
        idx += 3
        
    tq_idx_len = len(tq_idx)
    assert tq_idx_len % 2 == 0
    
    idx_offset = 0
    for i in range(0, tq_idx_len, 2):
        lo_idx = tq_idx[i] - idx_offset
        hi_idx = tq_idx[i+1] + 3 - idx_offset
        txt_len_org = len(txt)
        txt_lo = txt[0:lo_idx]
        txt_hi = txt[hi_idx:]
              
        if (txt_hi[0] == "\n") and (_no_non_white_before(txt_lo)):
            txt_lo = txt_lo[:txt_lo.rindex("\n")+1]
            txt_hi = txt_hi[1:]
        txt = txt_lo + txt_hi
        txt_len_new = len(txt)
        idx_offset  += (txt_len_org - txt_len_new)
    return txt


def strip_h(txt):
    out_lines = []
    lines = txt.splitlines()
    for line in lines:
        if len(line) == 0:
            out_lines.append("")
            continue
        string_idxs = _detect_strings(line)
        idx = 0
        while idx < len(line):
            try:
                idx = line.index("#", idx)
            except ValueError:
                out_lines.append(line)
                break
    
            if ((string_idxs == []) or 
                not(all([i[0] < idx < i[1] for i in string_idxs]))
                ):
                if idx == 0: # # is at the start of the line 
                    break
                elif _no_non_white_before(line[:idx]):
                    break
                else:
                    out_lines.append(line[:idx])
                    break
            idx += 1
    return "\n".join(out_lines)

        
def _no_non_white_before(txt):
    try:
        last_nl_idx = txt.rindex("\n")
    except ValueError:
        last_nl_idx = -1 
    if len(txt) == last_nl_idx + 1:
        return True
    chunk = txt[last_nl_idx + 1:]
    return all([c in whitespace for c in chunk])
    
  

def _detect_strings(txt):
    q_idx  = []
    idx = 0
    while idx < len(txt):
        try:
            idx = txt.index("'", idx)
        except ValueError:
            break
        if (idx > 0) and (txt[idx-1] == "\\"):
            idx += 1 
            continue
        q_idx.append(idx)
        idx += 1        
    
    q_idx_len = len(q_idx)
    #assert q_idx_len % 2 == 0 # does not work with " ' "
    
    return list(zip(q_idx[::2],q_idx[1::2]))

    

"""
assert strip_tq(class_three_indents) == class_three_indents_after_strip
assert strip_tq(class_with_method) == class_with_method_after_strip
assert strip_tq(multiline_docstring) == multiline_docstring_after_strip
""" 

"""
assert strip_h(single_comment).strip() == single_comment_after_strip.strip()

"""    
 