#!/usr/bin/python3
# Finds all multiples of 2 in a list.

def divisible_by_2(my_list=[]):
    divisables = []
    for i in my_list:
        divisables.append(True if i % 2 == 0 else False)

    return divisables
