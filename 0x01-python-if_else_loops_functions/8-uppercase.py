#!/usr/bin/python3
# Turns input string to uppercase

def uppercase(str):
    for letter in str:
        print("{}".format(chr(ord(letter) - 32) if
              (ord(letter) < 123 and ord(letter) >= 97) else letter), end='')
    print('')
