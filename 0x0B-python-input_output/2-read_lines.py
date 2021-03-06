#!/usr/bin/python3
""" define read_lines function """


def read_lines(filename="", nb_lines=0):
    """ reads nb_lines lines of the text file filename """
    with open(filename, encoding='utf-8') as f:
        ls = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(ls):
            print(*ls, end="", sep="")
        else:
            print(*ls[:nb_lines], end="", sep="")
