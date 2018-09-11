#!/usr/bin/python3
lower = True
for i in range(122, 96, -1):
    if not lower:
        i -= 32
    print("{}".format(chr(i)), end='')
    lower = not lower
