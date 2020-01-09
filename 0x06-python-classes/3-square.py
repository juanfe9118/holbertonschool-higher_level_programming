#!/usr/bin/python3
"""Python script that creates a class and functions for the class"""


class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Returns the area of the square"""
        return int(self.__size) * int(self.__size)
