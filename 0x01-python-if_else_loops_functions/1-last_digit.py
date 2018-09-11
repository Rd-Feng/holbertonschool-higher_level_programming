#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    d = (-number) % 10
    d *= -1
else:
    d = number % 10
print("Last digit of {:d} is ".format(number), d, "and is", end = ' ')
if d > 5:
    print("greater than 5")
elif d == 0:
    print("is 0")
else:
    print("less than 6 and not 0")
