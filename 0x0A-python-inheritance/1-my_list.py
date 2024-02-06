#!/usr/bin/python3

"""A single class inheritance by MyList from list"""


class MyList(list):
    """Prints list a sorted list in ascending order"""
    def print_sorted(self):
    """Prints list a sorted list in ascending order"""
        print(sorted(self))
