#!/usr/bin/python3
"""
Returns True if the object is an instance of.

or if the object is an instance of a class that inherited from.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if the object is an instance of.

    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.

    Args:
        obj: _description_
        a_class: _description_

    Returns:
        bool: _description_
    """

    if isinstance(obj, a_class):
        return True

    return False
