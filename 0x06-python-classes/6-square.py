#!/usr/bin/python3
"""Python script that creates a class and functions for the class"""


class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter and setter used to validate type and value of position"""
        return self.__position

    @position.setter
    def position(self, value):
        err = 'position must be a tuple of 2 positive integers'
        if isinstance(value, tuple) and len(value) == 2 and value[0] >= 0\
                and value[1] >= 0 and isinstance(value[0], int)\
                and isinstance(value[1], int):
                    self.__position = value
        else:
            raise TypeError(err)

    def area(self):
        """Returns the area of the square"""
        return int(self.__size) * int(self.__size)

    def my_print(self):
        """Prints a square using '#'"""
        if self.size == 0:
            print("")
            return
        for j in range(self.__position[1]):
            print("")
        for i in range(self.size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            print('#' * self.size)
