"""
Bite 172. Having fun with Python Partials
"""

from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places



rounder_int = partial(lambda num, prec: round(num, prec), prec=0)
rounder_detailed = partial(lambda num, prec: round(num, prec), prec=4)

#def rounder(num, prec):
#    return round(num, prec)
#rounder_int =  partial(rounder, prec=0)
#rounder_detailed =  partial(rounder, prec=4)