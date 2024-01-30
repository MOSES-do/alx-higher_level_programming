#!/usr/bin/python3

"""
Definition of a Rectangle class
"""


class Rectangle:
    """Class definition of rectangle instances"""
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
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
        if (self.__width or self.__height == 0):
            perimeter = 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        hashtag = ""
        """Print the sqaure with the # character"""
        if self.__width or self.__height == 0:
            hashtag = ""
        for i in range(0, self.__height):
            for j in range(self.__width):
                hashtag += "#"
            hashtag += "\n"
        return hashtag

    def __repr__(self):
        """returns official string represenatio of rectangle"""
        mod = type(self).__module__
        kclas = type(self).__name__
        memadd = hex(id(self))
        return f"<{mod}.{kclas} object at {memadd}>"
