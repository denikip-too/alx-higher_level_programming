#!/usr/bin/python3
"""Same class or inherit from"""


def is_kind_of_class(obj, a_class):
    """checks instance of,or if the object is an instance of a class inherited from a specified class"""
    if isinstance(obj, a_class):
        return True
    return False
