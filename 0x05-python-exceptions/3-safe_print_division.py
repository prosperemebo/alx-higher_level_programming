#!/usr/bin/python3
# divides 2 integers and
# prints the result.

def safe_print_division(a, b):
    ans = 0
    try:
        ans = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result {}".format(ans))
        return ans
