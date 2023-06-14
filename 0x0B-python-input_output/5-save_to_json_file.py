#!/usr/bin/python3
""" This module defines a function that writes an Object to a
    text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object
        filename: file name
    Returns:
        None
    """
    with open(filename, 'w',) as f:
        json.dump(my_obj, f)
