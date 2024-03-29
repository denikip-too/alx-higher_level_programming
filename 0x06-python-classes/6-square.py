#!/usr/bin/python3

"""Square"""


class Square:
    """Printing a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value != int(value):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        mes = "position must be a tuple of 2 positive integers"
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(mes)
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.__size
        position = self.__position
        if size == 0:
            print()
        for i in range(position[1]):
            print()
        for i in range(size):
            print((" " * self.__position[0]) + ("#" * self.__size))
