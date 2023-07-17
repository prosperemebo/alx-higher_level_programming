#!/usr/bin/python3
"""This module Handles the Base class."""


class Base:
    """Base Class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init method.

        Args:
            id (number, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
