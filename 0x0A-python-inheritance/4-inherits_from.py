#!/usr/bin/python3
"""
Returns True if the object is an instance of a class that inherited.

(directly or indirectly) from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """Verify that Input obj inherites from Input a_class.

    Args:
        obj: _description_
        a_class: _description_

    Returns:
        bool: _description_
    """
    return type(obj) != a_class and isinstance(obj, a_class)
