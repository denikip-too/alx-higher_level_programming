#!/usr/bin/python3
"""import Module"""
import json


"""Save Object to a file"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text fil"""
    with open(filename, "w") as Myfile:
        return json.dump(my_obj, Myfile)
