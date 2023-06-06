#!/usr/bin/python3
""" This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix

    Args:
        matrix: A matrix (list of lists) of integers/floats.
        A number (integer or float).

    Returns:
        A new matrix with all elements divided by div and rounded
        to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of an integer or float lists.
                   If each row of the matrix is not of the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    msg = 'matrix must be a matrix (list of lists) of integers/floats'
    msg_sz = 'Each row of the matrix must have the same size'
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix or not isinstance(matrix, list):
        raise TypeError("{}".format(msg))
    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError("{}".format(msg))
        if len(matrix[0]) != len(row):
            raise TypeError("{}".format(msg_sz))
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("{}".format(msg))
    nm = list(map(lambda i: list(map(lambda j: round(j / div, 2), i)), matrix))
    return nm
