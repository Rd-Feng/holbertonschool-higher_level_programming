#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        block = ""
        if num % 3 == 0:
            block += 'Fizz'
        if num % 5 == 0:
            block += 'Buzz'
        if num % 3 != 0 and num % 5 != 0:
            block += "{}".format(num)
        print("{} ".format(block), end='')
