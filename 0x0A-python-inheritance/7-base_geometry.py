#!/usr/bin/python3
"""Geometry class module"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """Raises an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks integer and correct value"""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
