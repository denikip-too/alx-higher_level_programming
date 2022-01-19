#!/usr/bin/python3
"""Import modules"""
import json
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        text = []
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for lst in list_objs:
                    text.append(lst.to_dictionary())
                f.write(cls.to_json_string(text))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        object_created = []
        with open(filename, 'r') as f:
            file_string = f.read().replace('\n', '')
            data = cls.from_json_string(file_string)
            for el in data:
                object_created.append(cls.create(**el))
            return object_created

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            res = []
            res = [item.to_dictionary() for item in list_objs]
            writer = csv.DictWriter(f, res[0].keys())
            writer.writeheader()
            writer.writerows(res)

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, "r") as f:
            rows = []
            dicti = {}
            filename = csv.DictReader(f)
            for row in filename:
                for i, j in dict(row).items():
                    dicti[i] = int(j)
                rows.append(cls.create(**dicti))
        return rows
