#!/usr/bin/python3
"""This module Handles the Base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by the JSON string.

        Args:
            json_string (str): The JSON string.
            representing a list of dictionaries.

        Returns:
            list: The list of dictionaries represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
