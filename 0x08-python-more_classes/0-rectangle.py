#!/usr/bin/python3

"""
Definition of a Rectangle class
"""


class Rectangle:
    """Class definition of Rectangle instances"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """function to return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """function to assign/change value of private variable"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """function to return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """function to assign/change value of private variable"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
