#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l = []
    for i in range(2):
        a, b = 0, 0
        if len(tuple_a) > i:
            a = tuple_a[i]
        if len(tuple_b) > i:
            b = tuple_b[i]
        l.append(a + b)
    return (l[0], l[1])
