#!/usr/bin/python3

"""check if object is an instance of class either directly or\
indirectly from specified class"""


def inherits_from(obj, a_class):

    """check object inheritance"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
