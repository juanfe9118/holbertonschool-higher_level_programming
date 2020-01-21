#!/usr/bin/python3
"""Append file module"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, 'a') as w:
        return w.write(text)
