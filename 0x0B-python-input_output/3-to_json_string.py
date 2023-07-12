#!/usr/bin/python3
"""This module encodes input in JSON."""
import json


def to_json_string(my_obj):
    """Transform input to JSON.

    Args:
        my_obj (_type_): _description_
    """
    json.dumps(my_obj)
