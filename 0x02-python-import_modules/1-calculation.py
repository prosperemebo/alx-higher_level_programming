#!/usr/bin/python3
# This is script prints the length and the 
# list of its arguments.

from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5

    print("a = 10")
    print("b = 5")
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
