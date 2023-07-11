#!/usr/bin/python3
"""Return the list of available attributes and methods of an object."""


def lookup(obj):
    """
    Return all attributes and object of input object

    Args:
        obj: _description_

    Returns: Attributes and objects
    """
    return dir(obj)
