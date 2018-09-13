#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    fname, numbers = argv[0], argv[1:]
    argc = len(argv) - 1
    if argc == 0:
        print(argc, "arguments.")
    else:
        if argc < 2:
            print(argc, "argument:")
        else:
            print(argc, "arguments:")
        for i in range(argc):
            print("{}:".format(i + 1), argv[i + 1])
