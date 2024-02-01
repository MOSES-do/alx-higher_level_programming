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
    if type(a) not in [int]:
        int_a = int(a)
        a = int(a)

    if type(b) not in [int]:
        int_b = int(b)
        b = int(b)

    return (a + b)
