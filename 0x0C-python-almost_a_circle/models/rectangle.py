#!/usr/bin/python3
"""Rectangle class creation"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width of rectangle"""
        return self.__width

    @property
    def height(self):
        """Get height of rectangle"""
        return self.__height

    @property
    def x(self):
        """Get x value"""
        return self.__x

    @property
    def y(self):
        """Get y of rectangle"""
        return self.__y

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width  must be an integer")
        elif (value < 0 or value == 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height  must be an integer")
        elif (value < 0 or value == 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if (not isinstance(value, int)):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if (not isinstance(value, int)):
            raise TypeError("y must be an integer")
        elif (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Returns 2d array based on height and width values"""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            for y in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overrides __str__ witha different value"""
        kclas = type(self).__name__
        new_id = self.id
        a = self.__x
        b = self.__y
        w = self.__width
        h = self.__height
        return ("[{}] ({}) {}/{} - {}/{}".format(kclas, new_id, a, b, w, h))

    def update(self, *args, **kwargs):
        """
        function updates instance attr based on values passed and
        reinitializes object if no value is passed
        """
        index = 0
        """list_attr = [self.width, self.height, self.x, self.y]"""

        if args and len(args) != 0:
            for arg in args:
                if index == 0:
                    if (arg is None):
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg
                index += 1
        else:
            w = self.width
            h = self.height
            if kwargs and len(kwargs) != 0:
                for key, value in kwargs.items():
                    if key == "id":
                        if value is None:
                            self.__init__(w, h, self.x, self.y)
                        else:
                            self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Dictionary represenation of rectangle"""
        return ({
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                })
