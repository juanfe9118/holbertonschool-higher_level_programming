#!/usr/bin/python3
"""Locked class module"""


class LockedClass:
    """Class that only allows the 'firs name' attribute to be created"""
    __slots__ = ["first_name"]
