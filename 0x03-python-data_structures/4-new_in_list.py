#!/usr/bin/python3
# Replaces element in input list securely

def new_in_list(my_list, idx, element):
    new_list = []

    for i in range(len(my_list)):
        new_list.append(element if i == idx else my_list[i])

    return new_list
