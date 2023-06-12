#!/usr/bin/python3
""" This module defines a class MyInt that inherits from int.
"""


class MyInt(int):
    """A class MyInt that inherits from int.
    """

    def __eq__(self, other):
        """Checks inequality
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Checks equality
        """
        return int.__eq__(self, other)
