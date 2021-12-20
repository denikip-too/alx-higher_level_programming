#!/usr/bin/python3
"""class Rectangle"""


class BaseGeometry:
    """base class BaseGeometry"""

    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""class Rectangle"""


class Rectangle(BaseGeometry):
    """subclass Rectangle"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
