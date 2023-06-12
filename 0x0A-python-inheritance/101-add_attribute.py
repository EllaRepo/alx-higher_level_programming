#!/usr/bin/python3
""" This module defines a function that adds attribute to an object
"""


def add_attribute(obj, name, value):
    """Adds attribute to an object
    Args:
        obj: an object
        name: attribute name to be added
        value: attribute value
    Returns:
        True if instance is exact
        False otherwise
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
