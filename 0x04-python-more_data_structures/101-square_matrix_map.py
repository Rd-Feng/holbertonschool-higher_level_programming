#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map((lambda e: e * e), row)) for row in matrix]
