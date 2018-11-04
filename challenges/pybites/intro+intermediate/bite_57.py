"""
Bite 57. Create a simple calculator that receives command line arguments
https://codechalleng.es/bites/57/
Created on Sun Jul 22 12:21:13 2018

@author: mh70
"""

import argparse
from functools import reduce

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""
    num = map(float, numbers)
    opr = {
        "add": (lambda x, y: x + y),
        "sub": (lambda x, y: x - y),
        "mul": (lambda x, y: x * y),
        "div": (lambda x, y: x / y),
    }
    return round(reduce(opr[operation], num), 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description="a simple calculator")
    parser.add_argument("--add", "-a", type=str, nargs="+", help="Sums numbers")
    parser.add_argument("--sub", "-s", type=str, nargs="+", help="Subtracts numbers")
    parser.add_argument("--mul", "-m", type=str, nargs="+", help="Multiplies numbers")
    parser.add_argument("--div", "-d", type=str, nargs="+", help="Divides numbers")

    # args = parser.parse_args()
    # print(parser)
    # print(args)
    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue
        # print (operation)
        # print (numbers)
        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == "__main__":
    call_calculator(stdout=True)

