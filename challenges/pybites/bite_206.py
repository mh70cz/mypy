# -*- coding: utf-8 -*-
"""
Bite 206. Calculate and evenly split the bill
"""
from decimal import Decimal
from decimal import ROUND_HALF_EVEN
def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """
    TWO_PLACES = Decimal("0.01")
    item_total = Decimal(item_total[1:])
    tax_rate = Decimal(tax_rate[:-1])
    tip = Decimal(tip[:-1])
    total_tax = Decimal(item_total * (1+tax_rate/100))
    #print(total_tax)
    total_tax = Decimal(total_tax.quantize(TWO_PLACES, rounding=ROUND_HALF_EVEN))
    #print(total_tax)
    grand_total = Decimal(total_tax  * (1+tip/100))
    #print(grand_total)
    grand_total = Decimal(grand_total.quantize(TWO_PLACES, rounding=ROUND_HALF_EVEN))
    split = Decimal(grand_total/people)
    split = split.quantize(TWO_PLACES, rounding=ROUND_HALF_EVEN)
    split_extra = grand_total - people * split
    splits = [split for _ in range(people)]
    splits[0] = split + split_extra
    
    return ((f"${grand_total}",splits ))


"""

our_value = Decimal(16.0/7)
output = Decimal(our_value.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))


        (('$8.68', '4.75%', '10%', 3), '$10.00'),
        (('$8.44', '6.75%', '11%', 3), '$10.00'),
        (('$9.99', '3.25%', '10%', 2), '$11.34'),
        (('$186.70', '6.75%', '18%', 6), '$235.17'),
        (('$191.57', '6.75%', '15%', 6), '$235.18'),
        (('$0.00', '0%', '0%', 1), '$0.00'),
        (('$100.03', '0%', '0%', 4), '$100.03'),
        (('$141.86', '2%', '18%', 9), '$170.75'),
        (('$16.99', '10%', '20%', 1), '$22.43'),
        (('$16.99', '10%', '20%', 2), '$22.43'),
        (('$16.99', '10%', '20%', 3), '$22.43'),
        (('$16.99', '10%', '20%', 4), '$22.43'),

# ROUND_05UP       ROUND_DOWN       ROUND_HALF_DOWN  ROUND_HALF_UP
# ROUND_CEILING    ROUND_FLOOR      ROUND_HALF_EVEN  ROUND_UP
"""