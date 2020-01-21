#!/usr/bin/python3
"""MyList class module"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list in a sorted fashion in a copied list"""
        print(sorted(self))
