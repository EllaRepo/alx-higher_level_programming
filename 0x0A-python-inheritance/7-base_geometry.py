#!/usr/bin/python3
""" This module defines a class BaseGeometry.
"""


class BaseGeometry():
    """A class BaseGeometry.
    """

    def area(self):
        """Instance method"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Instance method that validates value
        Args:
            name (str) : string
            value: can be anything
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
