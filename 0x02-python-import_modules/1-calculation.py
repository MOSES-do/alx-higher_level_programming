#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
resultOfADD = add(a, b)
resultofSUB = sub(a, b)
resultofMUL = mul(a, b)
resultofDIV = div(a, b)
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, resultOfADD))
    print("{} - {} = {}".format(a, b, resultofSUB))
    print("{} * {} = {}".format(a, b, resultofMUL))
    print("{} / {} = {}".format(a, b, resultofDIV))
