#!/usr/bin/python3
""" This module defines a function that checks object exactness
"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class
       otherwise returns False

    Args:
        obj: an object
        a_class: a class the object is checked against
    Returns:
        True if instance is exact
        False otherwise
    """
    return type(obj) is a_class
