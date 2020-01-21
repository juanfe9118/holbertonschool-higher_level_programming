#!/usr/bin/python3
"""Save object to file module"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w') as fo:
        json.dump(my_obj, fo)
