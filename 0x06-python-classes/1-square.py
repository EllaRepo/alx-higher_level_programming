#!/usr/bin/python3
""" This module defines a Square class.
"""


class Square:
    """Class Square that defines a square.

    """
    def __init__(self, size):
        """Initialize method that stores value for private attribute size.

        Args:
            size (int): Size of the square.

        """
        self.__size = size
