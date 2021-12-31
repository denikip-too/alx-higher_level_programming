#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """definition of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = "#"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """returns area rectangle"""
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        strs = ""
        if self.__width == 0 or self.__height == 0:
            return (strs)
        for i in range(self.__height):
            strs += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                strs += "\n"
        return strs

    def __del__(self):
        del self
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if notisinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be >= 0")
        return (Rectangle(size, size))
        square.__del__()
