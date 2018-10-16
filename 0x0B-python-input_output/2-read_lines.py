#!/usr/bin/python3
""" define read_lines function """


def read_lines(filename="", nb_lines=0):
    """ reads nb_lines lines of the text file filename """
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()
    if nb_lines <= 0 or nb_lines >= len(lines):
        for line in lines:
            print(line, end="")
    else:
        for i in range(nb_lines):
            print(lines[i], end="")
