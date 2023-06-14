#!/usr/bin/python3
# Prints the result of the addition of all arguments

from sys import argv
if __name__ == "__main__":
    add = 0
    for i in range(1, len(argv)):
        add += int(argv[i])
    print("{}".format(add))
