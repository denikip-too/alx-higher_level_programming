#!/usr/bin/python3
"""defines class Rectangle and inheriting class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """subclass of Rectangle"""

    def __init__(self, size):
        """define size"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """defines area"""
        return (self.__size * self.__size)

    def __str__(self):
        """description of square"""
        str1 = "[" + str(self.__class__.__name__) + "]" + " " + str(self.__size) + "/" + str(self.__size)
        return str1
