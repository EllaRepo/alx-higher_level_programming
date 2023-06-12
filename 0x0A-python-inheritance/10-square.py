#!/usr/bin/python3
""" This module defines a class Square.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class that defines Square inherited from Rectangle.
    """

    def __init__(self, size):
        """"Instance constructor
        Args:
            size: size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Reaturns area of a square
        """
        return super().area()
