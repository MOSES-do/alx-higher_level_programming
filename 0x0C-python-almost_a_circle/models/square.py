#!/usr/bin/python3
"""Square classi inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor using super()"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The overloading __str__ method should return [Square]..."""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """args=index + arguments, kwargs=key pair values"""
        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    if (arg is None):
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
