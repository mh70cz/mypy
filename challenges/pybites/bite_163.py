"""
Bite 163. Which packages were upgraded?

"""

def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    upgr_dep = []
    old_reqs_lst = _parse(old_reqs)
    new_reqs_lst = _parse(new_reqs)
    
    for old_r in old_reqs_lst:
        new_r = [x for x in new_reqs_lst if x[0] == old_r[0]][0]
        old_v = old_r[1].split(".")
        new_v = new_r[1].split(".")
        for idx, old_sub_v in enumerate(old_v):
            old_sub_v = int(old_sub_v)
            new_sub_v = int(new_v[idx])
            if new_sub_v > old_sub_v:
                upgr_dep.append(old_r[0])
                break
            if new_sub_v < old_sub_v:
                break
    return upgr_dep

    
def _parse(reqs):
    reqs_lst = []
    lines = reqs.splitlines()
    for line in lines:
        if "==" in line:
            reqs_lst.append(line.split("=="))
    return reqs_lst