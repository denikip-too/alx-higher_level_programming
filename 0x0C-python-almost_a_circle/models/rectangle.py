#!/usr/bin/python3
"""import base class Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = value

    def area(self):
        width = self.__width
        height = self.__height
        return (width * height)

    def display(self):
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        for w in range(y):
            print()
        for i in range(height):
                print((x * " ") + (width * "#"))

    def __str__(self):
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return ("[Rectancle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args, **kwargs):
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__
