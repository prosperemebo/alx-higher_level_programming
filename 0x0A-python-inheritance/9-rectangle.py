#!/usr/bin/python3
"""Module for the class Rectangle."""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialise instance and set values.

        Args:
            width (int)
            height (int)
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """
        Return the following rectangle description.

        [Rectangle] <width>/<height>
        """
        return ("[" + type(self).__name__ + "] " + str(self.__width)
                + "/" + str(self.__height))
