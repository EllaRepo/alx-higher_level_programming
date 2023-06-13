#!/usr/bin/python3
""" This module defines a function that writes a string to a text file
"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename: the name of the file to read
        text: text to write
    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
