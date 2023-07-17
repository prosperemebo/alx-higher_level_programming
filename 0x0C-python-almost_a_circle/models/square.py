#!/usr/bin/python3
"""This module Inherit the Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (both width and height).
            x (int): The x-coordinate of the square (default is 0).
            y (int): The y-coordinate of the square (default is 0).
            id (int): The unique identifier of the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
            str: A string representation of the square.
        """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__,
            self.id,
            self.x,
            self.y,
            self.width
        )

    @property
    def size(self):
        """Get or set the size of the square (both width and height)."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square (both width and height)."""
        self.width = value
        self.height = value
