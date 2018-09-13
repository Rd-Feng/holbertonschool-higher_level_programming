#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

ops = {'+': add, '-': sub, '*': mul, '/': div}

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    op = ops.get(argv[2])
    if op is None:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
    a, b = int(argv[1]), int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, op(a, b)))
