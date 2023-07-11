#!/usr/bin/python3
"""Module for the class Square."""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle."""

    def __init__(self, size):
        """
        Initialise instance with values.

        Args:
            size (int): _description_
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
