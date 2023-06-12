#!/usr/bin/python3
""" This module defines a function that checks an  instance of a class is
    inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
       (directly or indirectly) from the specified class ; otherwise False
    Args:
        obj: an object
        a_class: a class the object is checked against
    Returns:
        True if obj is an instance of a class inherited
        False otherwise
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
