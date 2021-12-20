#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """base class BaseGeometry"""

    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
