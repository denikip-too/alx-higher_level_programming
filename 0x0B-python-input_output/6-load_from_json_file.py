#!/usr/bin/python3
"""import Module"""
import json


"""Create object from a JSON file"""


def load_from_json_file(filename):
    """creates an Object from a JSON file"""
    with open(filename) as Myfile:
        return json.load(Myfile)
