#!/usr/bin/python3
# Adds all unique integers in input list

def uniq_add(my_list=[]):
    new_list = set(my_list)
    summ = sum(int(i) for i in new_list)
    return summ
