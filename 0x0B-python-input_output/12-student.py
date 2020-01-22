#!/usr/bin/python3
"""Student to JSON module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        ret_att = {}
        for key, val in self.__dict__.items():
            if key in attrs:
                ret_att[key] = val
        return ret_att
