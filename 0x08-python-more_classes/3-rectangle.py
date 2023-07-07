#!/usr/bin/python3
"""An empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """
        Class Initiliser.

        Args:
            width Argument.
            height Argument.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter.

        Returns:
            int: width od Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter.

        Args:
            value (int): input value

        Raises:
            TypeError: Value must be defined and must be an int.
            ValueError: Value must be greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter.

        Returns:
            int: height od Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter.

        Args:
            value (int): input value

        Raises:
            TypeError: value must be defined and must be an int.
            ValueError: Value must be greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate Area of self.

        Returns:
            int: Area of self.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Calculate perimetr of self.

        Returns:
            int: perimeter of self.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Generate a square.

        Returns:
            _type_: _description_
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        square = ""

        for h in range(self.__height):
            for w in range(self.__width):
                square += "#"
            if h != self.__height - 1:
                square += "\n"

        return square
