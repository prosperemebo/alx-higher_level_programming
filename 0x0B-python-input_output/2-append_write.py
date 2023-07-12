#!/usr/bin/python3
"""This script appends file."""


def append_write(filename="", text=""):
    """Append specified filename.

    Args:
        filename (str, optional): _description_. Defaults to "".
        text (str, optional): _description_. Defaults to "".
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
