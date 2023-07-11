#!/usr/bin/python3
"""This module checks if object is of instance."""


def is_same_class(obj, a_class):
    """
    Check if both inputs are of the same instance.

    Args:
        obj: Input one
        a_class: Input Class

    Returns:
        bool: True if yes and False if not
    """
    return a_class == type(obj)
