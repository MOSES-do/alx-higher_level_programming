#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        """Instantiation with size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

        def __str__(self):
            return (f"[Square] {self.__size}")
