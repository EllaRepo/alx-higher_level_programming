#!/usr/bin/python3
""" This module defines a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the name of the file to read
        search_string: string to be search
        new_string: string to insert
    Returns: None
    """
    nw_f = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            nw_f += [line]
            if search_string in line:
                nw_f += [new_string]
    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(nw_f))
