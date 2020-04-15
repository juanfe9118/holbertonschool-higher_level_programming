#!/usr/bin/python3
"""Module that takes a url and displays a header"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    header = r.headers.get('X-Request-Id')
    print(header)
