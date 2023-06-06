#!/usr/bin/python3
# This script generates a random integer,
# and checks if it's positive, negative or zero.

import random
number = random.randint(-10, 10)
if number < 0:
	print(f"{number:d} is negative")
elif number == 0:
	print(f"{number:d} is zero")
else:
	print(f"{number:d} is positive")
