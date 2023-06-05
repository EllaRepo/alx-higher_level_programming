#!/usr/bin/python3
""" This module defines a Rectangle class.
"""


class Rectangle:
    """Empty class Rectangle that defines a rectangle.

    """
    def __init__(self, width=0, height=0):
        """Initialize method that stores value for private attribute width
            and height.

        Args:
            width (int): width of the square.
            height (int): height of the square.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set private instance attribute width
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set private instance attribute height
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
