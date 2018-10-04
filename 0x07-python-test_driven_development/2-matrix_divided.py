#!/usr/bin/python3
"""module matrix_divided

This module define matrix_divided function.
"""


def matrix_divided(matrix, div):
    """divide elements in matrix
    divide all elements by input div
    """
    # Check if matrix is a list of lists of integers or floats
    if ((not isinstance(matrix, list)) or
        (not all(isinstance(r, list) for r in matrix)) or
            (not all(isinstance(e, (int, float)) for r in matrix for e in r))):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    # Check if rows have same size
    if len(set([len(row) for row in matrix])) != 1:
        raise TypeError(
            'Each row of the matrix must have the same size'
        )
    # div must be a number
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    # div cannot be 0
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [list(map(lambda e: round(e / div, 2), row)) for row in matrix]
