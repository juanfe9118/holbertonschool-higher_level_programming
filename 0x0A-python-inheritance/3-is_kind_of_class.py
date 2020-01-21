#!/usr/bin/python3
"""Same class or inherit from module"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a class
    it inherited from, False otherwise"""
    return isinstance(obj, a_class)
