#!/usr/bin/python3
""" This module defines a function that prints a square with the character #
"""


def print_square(size):
    """Prints in stdout the square with the character #

    Args:
        size: size of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print("#" * size)
