#!/usr/bin/python3

"""Square"""


class Square:
    """Square"""

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        size = self.__size
        return size * size
