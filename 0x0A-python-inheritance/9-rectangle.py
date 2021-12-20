#!/usr/bin/python3
"""base class BaseGeometry that class Rectangle inherites"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """subclass Rectangle"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """defines area"""
        return (self.__width * self.__height)
    
    def __str__(self):
        """rectangle description"""
        str1 = "[" + str(self.__class__.__name__) + "]" + " " + str(self.__width) + "/" + str(self.__height)
        return str1
