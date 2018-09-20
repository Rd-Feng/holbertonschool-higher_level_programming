#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        return [list(map((lambda e: e * e), row)) for row in matrix]
