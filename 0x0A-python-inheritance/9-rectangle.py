#!/usr/bin/python3
""" This module defines a class Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that defines Rectangle inherited from BaseGeometry.
    """

    def __init__(self, width, height):
        """"Instance constructor
        Args:
            width: width
            height: height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns instance information
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Instance method that returns the area of a rectangle"""
        return self.__height * self.__width
