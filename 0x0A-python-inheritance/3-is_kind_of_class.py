#!/usr/bin/python3
""" This module defines a function that checks object is an instance of,
    or if the object is an instance of a class that inherited from
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or if the object
       is an instance of a class that inherited from, the specified class;
       otherwise False
    Args:
        obj: an object
        a_class: a class the object is checked against
    Returns:
        True if obj is an instance of
        False otherwise
    """
    return isinstance(obj, a_class)
