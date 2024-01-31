#!/usr/bin/python3

"""
Definition of a Rectangle class
"""


class Rectangle:
    """Class definition of Rectangle instances"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        """function to return height value"""
        return self.__height

    @height.setter
    def height(self, value):
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of a rectangle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return ((self.__width + self.__height) * 2)
