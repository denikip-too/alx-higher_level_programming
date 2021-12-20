#!/usr/bin/python3
"""class BaseGeometry"""


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
        """instatiation of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """defines area"""
        return (self.__width * self.__height)

    def __str__(self):
        """description of rectangle"""
        str1 = "[" + str(self.__class__.__name__) + "]" + " " + str(self.__width) + "/" + str(self.__height)
        return str1

"""class Square"""


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
