#!/usr/bin/python3
""" This module defines a function returns the dictionary description
    with simple data structure
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
       (list, dictionary, string, integer and boolean) for JSON serialization
       of an object

    Args:
        obj: an instance of a Class
    Returns:
        returns the dictionary description
    """
    dict_desc = {}
    if hasattr(obj, "__dict__"):
        dict_desc = obj.__dict__.copy()
    return dict_desc
