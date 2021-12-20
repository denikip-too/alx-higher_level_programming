#!/usr/bin/python3
"""base class BaseGeometry inherited by class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass Rectangle"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
