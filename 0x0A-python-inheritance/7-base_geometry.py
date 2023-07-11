#!/usr/bin/python3
"""BaseGeometry Class."""


class BaseGeometry:
    """BaseGeometry class."""

    def area(self):
        """Raise exception.

        Raises:
            Exception: _description_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if input value is an int.

        Args:
            name: _description_
            value: _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
