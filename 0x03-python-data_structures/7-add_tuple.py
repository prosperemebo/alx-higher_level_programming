#!/usr/bin/python3
# Add input tuple

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = (
            (0 if len(tuple_a) == 0 else tuple_a[0]) +
            (0 if len(tuple_b) == 0 else tuple_b[0]),
            (0 if len(tuple_a) <= 1 else tuple_a[1]) +
            (0 if len(tuple_b) <= 1 else tuple_b[1])
    )

    return tuple_c
