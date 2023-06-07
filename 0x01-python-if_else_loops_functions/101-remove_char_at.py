#!/usr/bin/python3
# Removes a character at input index

def remove_char_at(str, n):
    copy = ""
    for i in range(0, len(str)):
        if i != n:
            copy += str[i]
    return copy
