#!/usr/bin/python3
"""Module for the class Rectangle."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle inherits BaseGeometry."""

    def __init__(self, width, height):
        """Init function for rectangle method.

        Args:
            width: _description_
            height: _description_
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
