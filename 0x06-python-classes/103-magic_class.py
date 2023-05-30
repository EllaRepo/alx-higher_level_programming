#!/usr/bin/python3
""" This module defines a Square class.
"""
import math


class MagicClass:
    """A class that represents a circle with a given radius.
    """

    def __init__(self, radius=0):
        """Initializes a MagicClass object with the given radius.

        Args:
            radius (float): The radius of the circle (default 0).
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Computes and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
