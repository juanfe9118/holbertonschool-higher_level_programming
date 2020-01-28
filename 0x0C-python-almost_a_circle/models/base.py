#!/usr/bin/python3
"""Base Class Module"""
import json
from os import path


class Base:
    """Class Base that will be the parent all the classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        flname = cls.__name__ + '.json'
        dic = []
        if list_objs is not None:
            dic = [a.to_dictionary() for a in list_objs]
        with open(flname, 'w') as f:
            f.write(cls.to_json_string(dic))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Square':
            new_base = cls(1)
        else:
            new_base = cls(1, 1)
        cls.update(new_base, **dictionary)
        return new_base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        flname = cls.__name__ + '.json'
        if path.isfile(flname):
            with open(flname, 'r') as f:
                my_l = cls.from_json_string(f.read())
            return [cls.create(**a) for a in my_l]
        return []
