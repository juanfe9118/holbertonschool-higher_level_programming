#!/usr/bin/python3
"""Read n lines module"""


def read_lines(filename="", nb_lines=0):
    """Reads n lines of a text file (UTF8) and prints it to stdout"""
    linum = 0
    with open(filename, 'r') as o:
        for line in o:
            linum += 1
    with open(filename, 'r') as o:
        if nb_lines <= 0 or nb_lines > linum:
            for line in o:
                print(line, end='')
        else:
            for i in range(nb_lines):
                print(o.readline(), end='')
