#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def calc():

    if len(sys.argv) < 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    arg1 = sys.argv[1]
    ope = sys.argv[2]
    arg2 = sys.argv[3]

    if ope == "+":
        result = add(int(arg1), int(arg2))
        print(f"{arg1} + {arg2} = {result}")
    elif ope == "*":
        result = mul(int(arg1), int(arg2))
        print(f"{arg1} * {arg2} = {result}")
    elif ope == "-":
        result = sub(int(arg1), int(arg2))
        print(f"{arg1} - {arg2} = {result}")
    elif ope == "/":
        result = div(int(arg1), int(arg2))
        print(f"{arg1} / {arg2} = {result}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    calc()
