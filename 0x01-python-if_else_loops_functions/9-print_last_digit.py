#!/usr/bin/python3
# Prins last digit of input number

def print_last_digit(number):
    n = abs(number) % 10
    print(n, end='')
    return n
