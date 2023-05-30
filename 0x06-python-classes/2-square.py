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
