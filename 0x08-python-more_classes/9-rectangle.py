#!/usr/bin/python3

"""
Definition of a rectangle class
"""


class Rectangle:
    """Class definition of rectangle instances"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        if (self.__width == 0 or self.__height == 0):
            perimeter = 0
        perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        hashtag = ""
        """Print the sqaure with the # character"""
        for i in range(self.__height):
            for j in range(self.__width):
                hashtag += str(Rectangle.print_symbol)
            hashtag += '\n'
        return hashtag

    def __repr__(self):
        """returns official string represenatio of rectangle"""
        mod = type(self).__module__
        kclas = type(self).__name__
        memadd = hex(id(self))
        return f"{kclas}({self.__width}, {self.__height})"

    def __del__(self):
        """prints message on deletion of rectangle instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() == rect_2.area()):
            return rect_1
        elif (rect_1.area() > rect_2.area()):
            return rect_1
        elif (rect_2.area() > rect_1.area()):
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
