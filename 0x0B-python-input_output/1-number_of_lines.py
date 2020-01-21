#!/usr/bin/python3
"""Number of lines module"""


def number_of_lines(filename=""):
    """Returns the number of lines in a text file"""
    with open(filename, 'r') as o:
        linum = 0
        for line in o:
            linum += 1
        return linum
