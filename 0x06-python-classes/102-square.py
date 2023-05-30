#!/usr/bin/python3
""" This module defines a Square class.
"""


class Square:
    """Class Square that defines a square.

    """
    def __init__(self, size=0):
        """Initialize method that stores value for private attribute size.

        Args:
            size (int): Size of the square.

        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)

    def __eq__(self, other):
        return self.size == other.size

    def __ne__(self, other):
        return self.size != other.size

    def __gt__(self, other):
        return self.size > other.size

    def __ge__(self, other):
        return self.size >= other.size

    def __lt__(self, other):
        return self.size < other.size

    def __le__(self, other):
        return self.size <= other.size

    @property
    def size(self):
        """Retrieve private instance attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set private instance attribute size
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(value)

    def area(self):
        """Returns the current square area.
        """
        return self.__size**2
