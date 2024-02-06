#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle

"""A square class"""

class Square(Rectangle):
    """Rectangle"""
    def __init__(self, size):
        """size instantiation"""
        self.__size = size

    def area(self):
        """returns area of square"""
        return self.__size * self.__size
    
    def __str__(self):
        """prints description of square in string format"""
        size = self.__size
        return ("{} {}/{}").format(type(self).__name__, size, size)
