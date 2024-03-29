#!/usr/bin/python3

"""Square"""


class Square:
    """defines a square and Instantiate"""

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
