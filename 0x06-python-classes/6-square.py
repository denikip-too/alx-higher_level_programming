#!/usr/bin/python3

"""Square"""


class Square:
    """Printing a square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        size = self.__size
        position = self.__position
        if size == 0:
            print()
        for i in range(position[1] > 0):
            print()
        for i in range(size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for y in range(0, self.__size)]
            print("")
