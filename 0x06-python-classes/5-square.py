#!/usr/bin/python3
"""Python script that creates a class and functions for the class"""


class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """Getter and setter used to validate type and value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """Returns the area of the square"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Prints a square using '#'"""
        if self.size == 0:
            print("")
        for i in range(self.size):
            print('#' * self.size)
