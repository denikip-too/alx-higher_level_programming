#!/usr/bin/python3
"""Import modules"""
import json


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        text = []
        if list_objs is None:
            return []
        else:
            for lst in list_objs:
                text.append(lst.to_dictionary())
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(Base.to_json_string(text))

    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        elif cls.__name__ == "Square":
            new = cls(10, 10)
        new.update(**dictionary)
        return new

    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))
        return object_created
