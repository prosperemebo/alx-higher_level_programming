#!/usr/bin/python3
# Checks if input character is lowercase

def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
