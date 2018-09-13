#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    fname, nums = argv[0], argv[1:]
    sum = 0
    for num in nums:
        sum += int(num)
    print(sum)
