#!/usr/bin/python3
""" This module defines a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """A function that adds two integers/floats

    Args:
        a: first integer/float
        b: second integer/float

    Returns:
        The return value. a + b

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
