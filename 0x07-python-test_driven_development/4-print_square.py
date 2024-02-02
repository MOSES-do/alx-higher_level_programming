#!/usr/bin/python3

"""

A function that prints # n number of times

"""


def print_square(size):
    """
    A 2d print of any given symbol
    """

    if type(size) not in [int]:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, str):
        raise TypeError("size must be an integer")
    if size == float('NaN'):
        raise TypeError("size must be an integer")
    if size is None:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
