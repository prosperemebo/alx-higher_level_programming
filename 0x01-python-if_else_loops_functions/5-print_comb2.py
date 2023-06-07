#!/usr/bin/python3
# Outputs all numbers in range 0 - 100

for i in range(0, 100):
    if i < 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:02d}".format(i))
