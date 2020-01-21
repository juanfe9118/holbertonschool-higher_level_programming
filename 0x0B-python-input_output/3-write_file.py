#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns
    the number of characters written"""
    with open(filename, 'w') as w:
        return w.write(text)
