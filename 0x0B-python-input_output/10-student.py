#!/usr/bin/python3
"""class Student"""


class Student:
    """Instatiate public instances attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defines a student"""
        if type(attrs) == list:
            dic = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in self.__dict__.keys():
                    dic[i] = self.__dict__[i]
            return self.__dict__
        else:
            return self.__dict__
