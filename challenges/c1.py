
"""http://www.pythonchallenge.com/pc/def/map.html"""

def haf():
    """rot"""
    shift = 2
    enc_txt = """g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

    count_letters_in_alphabet = ord('z') - ord('a') + 1
    opn_txt = ""
    for c in enc_txt:
        c_code = ord(c)
        if (c_code >= ord('a')) and (c_code <= ord('z')):
            if c_code <= (ord('z') - shift):
                opn_txt += chr(c_code + shift)
            else:
                opn_txt += chr(c_code + shift - count_letters_in_alphabet)
        else:
            opn_txt += c

    print(opn_txt)

haf()
