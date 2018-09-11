#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        d = (-number) % 10
        print(d, end='')
        return (d)
    else:
        d = number % 10
        print(d, end='')
        return (d)
