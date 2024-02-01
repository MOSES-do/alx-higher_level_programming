#!/usr/bin/python3
"""

This module provides a function that adds to integers

"""


def add_integer(a, b=98):

    """
    function add two integers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    if a == float('NaN'):
        raise TypeError("a must be an integer")
    if b == float('NaN'):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
