#!/usr/bin/python3

"""
Definition of a rectangle class
"""


class Rectangle:
    """Class definition of rectangle instances"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def height(self):
        """return height of rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """return width of rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
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

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ("")
        hashtag = ""

        """Print the sqaure with the # character"""
        for i in range(self.__height):
            for j in range(self.__width):
                hashtag += str(Rectangle.print_symbol)
            if (i != self.__height - 1):
                hashtag += '\n'
        return (hashtag)

    def __repr__(self):
        """returns official string represenation of rectangle"""
        kclas = type(self).__name__
        return (f"{kclas}({self.__width}, {self.__height})")

    def __del__(self):
        """prints message on deletion of rectangle instance"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
