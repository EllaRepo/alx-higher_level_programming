#!/usr/bin/python3
""" This module defines a function that appends a string at the end of
    a text file (UTF8)
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)

    Args:
        filename: the name of the file to read
        text: text to write
    Returns:
        the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)