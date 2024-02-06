#!/usr/bin/python3

"""A single class inheritance by MyList from list"""


class MyList(list):
    """Prints list asorted list in ascending order"""
    def print_sorted(self):
        print(sorted(self))
