#!/usr/bin/python3
"""This script writes to file."""


def write_file(filename="", text=""):
    """Write to specified filename.

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
