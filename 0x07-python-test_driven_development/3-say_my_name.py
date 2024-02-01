#!/usr/bin/python3

"""

Create a function that prints name of a person (first, last)

"""


def say_my_name(first_name, last_name=""):
    """
    function prints full name
    """

    if type(first_name) not in [str] or first_name == "":
        raise TypeError("first_name must be a string")
    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")
    if type(last_name) not in [str]:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
