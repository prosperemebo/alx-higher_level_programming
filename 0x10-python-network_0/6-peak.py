#!/usr/bin/python3
"""This script finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers."""
    prev = 0
    for idx, num in enumerate(list_of_integers):
        if idx:
            prev = list_of_integers[idx - 1]
        if idx < len(list_of_integers) - 1:
            next = list_of_integers[idx + 1]
        else:
            next = 0
        if num >= prev and num >= next:
            return num
