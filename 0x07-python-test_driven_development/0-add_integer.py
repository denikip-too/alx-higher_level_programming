#!/usr/bin/python3
"""Integers addition"""


def add_integer(a, b=98):
    """adds 2 integers"""
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    else:
        return a + b
