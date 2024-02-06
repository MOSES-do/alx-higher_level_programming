#!/usr/bin/python3


"""A geometry class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


""" A Rectangle class"""


class Rectangle(BaseGeometry):
    """Rectangle"""
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        super().integer_validator()

    def area(self):
        """area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        dstring = "[" + str(self.__class__.__name__) + "] "
        dstring += str(self.__width) + "/" + str(self.__height)
        return (dstring)
