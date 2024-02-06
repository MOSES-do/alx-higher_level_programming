#!/usr/bin/python3

"""Function that checksif an object is of same class"""

def is_same_class(obj, a_class):
    """Function that checksif an object is of same class"""
    if (isinstance(obj, a_class)):
        return True
    else:
        return False
