#!/usr/bin/python3
"""import Module"""
import json


"""From JSON string to Object"""


def from_json_string(my_str):
    """returns an object represented by a JSON string"""
    return json.loads(my_str)
