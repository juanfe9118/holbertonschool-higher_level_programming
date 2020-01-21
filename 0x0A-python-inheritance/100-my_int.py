#!/usr/bin/python3
"""MyInt class Module"""


class MyInt(int):
    """Class MyInt that inherits from int"""
    def __eq__(self, other):
        """Inverts == and !="""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Inverts == and !="""
        return not self.__eq__(other)
