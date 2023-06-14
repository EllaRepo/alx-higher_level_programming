#!/usr/bin/python3
""" This module defines a function thatcreates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”

    Args:
        filename: file name
    Returns:
        None
    """
    with open(filename, 'r',) as f:
        return json.load(f)
