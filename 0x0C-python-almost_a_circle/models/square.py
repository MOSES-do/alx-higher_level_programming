#!/usr/bin/python3
"""Square classi inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor using super()"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
