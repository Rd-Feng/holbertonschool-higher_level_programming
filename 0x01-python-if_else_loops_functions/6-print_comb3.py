#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j:
            if i is 8:
                print("{0}{1}".format(i, j))
            else:
                print("{0}{1}".format(i, j), end=", ")
