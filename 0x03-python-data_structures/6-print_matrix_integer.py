#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            if i == len(line) - 1:
                print ("{:d}".format(line[i]), end="")
            else:
                print("{:d}".format(line[i]), end=" ")
        print()
