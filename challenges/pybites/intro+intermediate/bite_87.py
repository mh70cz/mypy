"""
Bite 87. Convert Decimal to Roman Numerals 

https://codechalleng.es/bites/87
"""

def romanize(decimal_number):
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError
    
    
    if 0 <= decimal_number >= 4000:
        raise ValueError
    
    rn = "IVXLCDM"
    roman = ""
    
    for i in range(4):
        n = decimal_number % 10**(i+1) // 10**i 
        
        if n < 4:
            s = n*rn[0+i*2]
        elif n == 4:
            s = rn[0+i*2] + rn[1+i*2]    
        elif n == 5:
            s = rn[1+i*2]
        elif n < 9:
            s = rn[1+i*2] + (n-5)*rn[0+i*2]
        elif n == 9:
            s = rn[0+i*2] + rn[2+i*2]        
        roman = s + roman
    return roman        
    
    
import pytest




@pytest.mark.parametrize("number, numeral", [
    (1000, 'M'),
    (500, 'D'),
    (100, 'C'),
    (50, 'L'),
    (10, 'X'),
    (5, 'V'),
    (1, 'I'),
    (177, 'CLXXVII'),
    (244, 'CCXLIV'),
    (87, 'LXXXVII'),  # Bite LXXXVII
    (1033, 'MXXXIII'),
    (997, 'CMXCVII'),
    (3999, 'MMMCMXCIX'),
    (13, 'XIII'),
    (777, 'DCCLXXVII'),
    (1652, 'MDCLII'),
    (1981, 'MCMLXXXI'),
    (2018, 'MMXVIII'),
    (3500, 'MMMD'),
])
def test_romanize(number, numeral):
    assert romanize(number) == numeral


def test_boundaries():
    with pytest.raises(ValueError):
        romanize('string')
        romanize(-1)
        romanize(0)
        romanize(4000)
        romanize(10000)
    
import sys
if __name__ == '__main__':
    pytest.main(sys.argv)          