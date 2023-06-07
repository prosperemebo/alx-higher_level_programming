#!/usr/bin/python3
# Prints ASCII alphabet, 
# in reverse order, alternating lowercase and uppercase.

for i in range(90, 64, -1):
    print("{}".format(chr(i + 32) if (i % 2 == 0) else chr(i)), end='')
