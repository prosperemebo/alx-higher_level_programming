#!/usr/bin/python3
"""MyList that inherits from list."""


class MyList(list):
    """MyList that inherits from list."""

    def print_sorted(self):
        """
        Print input list in acending order.

        Args:
            self
        """
        print(sorted(self))
