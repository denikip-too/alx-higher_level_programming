#!/usr/bin/python3
"""import class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle"""

    width = 0
    height = 0
    def __init__(self, size, x=0, y=0, id=None):
        super(Square, self).__init__(width = size, height = size, x = x, y = y, id = id)
        self.size = size

    def __str__(self):
        id = self.id
        w = self.size
        h = self.size
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, w, h))

    @property
    def size(self):
        return self.width
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def to_dictionary(self):
        return self.__dict__

    def update(self, *args, **kwargs):
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
