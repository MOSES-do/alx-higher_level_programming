#!/usr/bin/python3

"""Function returns available attributes and methods of a given object"""


def lookup(obj):
    """return class object"""
    my_attr = dir(obj)
    return (my_attr)
