#!/usr/bin/python3
# Prints a dictionary by ordered keys.

def print_sorted_dictionary(a_dictionary):
    for i, j in sorted(a_dictionary.items()):
        print(f"{i}: {j}")
