#!/usr/bin/python3
""" This module defines a function that  reads a text
    file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout

    Args:
        filename: the name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        text = f.readline()
        while text != '':
            print(text, end='')
            text = f.readline()
    print()
