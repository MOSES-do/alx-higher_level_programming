#!/usr/bin/python

"""Function returns available attributes and methods of a given object"""


def lookup(obj):
    """return class object"""
    all_attr = dir(obj)
    return all_attr
