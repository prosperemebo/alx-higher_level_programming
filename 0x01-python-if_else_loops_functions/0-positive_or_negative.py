#!/usr/bin/python3
# This script generates a random number,
# and prints positive, negative or zero.

import random
number = random.randint(-10, 10)
if number > 0:
    print(f'{number:d} is positive')
elif number < 0:
    print(f'{number:d} is negative')
else:
    print(f'{number:d} is zero')
