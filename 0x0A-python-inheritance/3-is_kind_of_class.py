#!/usr/bin/python3

"""check if object is instance of a class"""


def is_kind_of_class(obj, a_class):

    """check if object is an instance of the class"""

    if (isinstance(obj, a_class)):
        return True
    else:
        return False
