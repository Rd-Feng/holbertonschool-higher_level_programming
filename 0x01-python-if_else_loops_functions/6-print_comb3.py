#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i < j:
            if i is 8:
                print(i, j, sep='')
            else:
                print(i, j, sep='', end = ", ")
