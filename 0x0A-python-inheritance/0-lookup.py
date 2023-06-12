#!/usr/bin/python3
""" This module defines a function that returns the list of
    available attributes and methods of an object.
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.

    Args:
        obj: an object
    Returns:
        a list object
    """
    return dir(obj)
