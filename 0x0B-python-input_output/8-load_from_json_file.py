#!/usr/bin/python3
"""Create object from JSON file module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a 'JSON file' and returns it"""
    with open(filename, 'r') as fo:
        return json.load(fo)
