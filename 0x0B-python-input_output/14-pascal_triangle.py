#!/usr/bin/python3
""" define pascal_triangle function """


def pascal_triangle(n):
    """ return a pascal triangle of n rows """
    l = []
    for i in range(n):
        l.append([0 for e in range(i + 1)])
        l[i][0], l[i][i], h, t = 1, 1, 1, i - 1
        while h <= t:
            l[i][h] = l[i - 1][h] + l[i - 1][h - 1]
            l[i][t], h, t = l[i][h], h + 1, t - 1
    return l
