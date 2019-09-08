"""
Bite 198. Calculate my Mac's longest uptime
"""
import datetime

MAC1 = """
reboot    ~                         Wed Apr 10 22:39
reboot    ~                         Wed Mar 27 16:24
reboot    ~                         Wed Mar 27 15:01
reboot    ~                         Sun Mar  3 14:51
reboot    ~                         Sun Feb 17 11:36
reboot    ~                         Thu Jan 17 21:54
reboot    ~                         Mon Jan 14 09:25
"""


def calc_max_uptime(reboots_raw):
    """Parse the passed in reboots output,
       extracting the datetimes.

       Calculate the highest uptime between reboots =
       highest diff between extracted reboot datetimes.

       Return a tuple of this max uptime in days (int) and the
       date (str) this record was hit.

       For the output above it would be (30, '2019-02-17'),
       but we use different outputs in the tests as well ...
    """
    reboots = []
    for line in reboots_raw.splitlines():
        if len(line) == 0:
            continue
        date_raw = reduce_inner_spaces(line).split(" ")[-3:]
        date_raw = "2019+" + "+".join(date_raw)
                
        # %b locale dependent
        date = datetime.datetime.strptime(date_raw, "%Y+%b+%d+%H:%M") 
        #print (date_raw)
        #print (date)
        reboots.append(date)
    diffs = []
    
    for reboot, reboot_prev in zip(reboots, reboots[1:]):
        diff = reboot - reboot_prev
        diff_days = diff.days
        reboot = datetime.datetime.strftime(reboot, "%Y-%m-%d")
        #print(diff_days, reboot)
        diffs.append((diff_days, reboot))        
    
    """
    for idx, reboot in enumerate(reboots[:-1]):
        diff =  reboot - reboots[idx+1]
        diff_days = diff.days
        reboot = datetime.datetime.strftime(reboot, "%Y-%m-%d")
        #print(diff_days, reboot)
        diffs.append((diff_days, reboot))
        
    """    
    return sorted(diffs, reverse=True)[0]
        
def reduce_inner_spaces(string):
    out_str = ""
    extra_space = False
    for c in string:
        if c == " ":
            if extra_space:
                continue
            out_str += c
            extra_space = True
        else:
            out_str += c
            extra_space = False
    return out_str
