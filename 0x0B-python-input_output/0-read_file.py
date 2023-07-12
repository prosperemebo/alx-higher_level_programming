#!/usr/bin/python3
"""Script for read_file."""


def read_file(filename=""):
    """Read specified filename.

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
