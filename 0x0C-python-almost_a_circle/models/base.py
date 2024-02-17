#!/usr/bin/python3

"""
Base class creation
"""


class Base:
    """Base class"""
    __nb__objects = 0

    def __init__(self, id=None):
        if (id is not None):
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
