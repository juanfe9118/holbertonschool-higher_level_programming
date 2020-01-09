#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class Square with size validation"""


class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        self.__size = size
