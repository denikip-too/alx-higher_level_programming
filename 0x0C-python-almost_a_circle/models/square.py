#!/usr/bin/python3
"""import class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    width = 0
    height = 0

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super(Square, self).__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """returns attributes of Square"""
        id = self.id
        w = self.size
        h = self.size
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, w, h))

    @property
    def size(self):
        """get width and height"""
        return self.width
        return self.height

    @size.setter
    def size(self, value):
        """set width and height"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        id = self.id
        w = self.size
        h = self.size
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': w, 'y': y}

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
