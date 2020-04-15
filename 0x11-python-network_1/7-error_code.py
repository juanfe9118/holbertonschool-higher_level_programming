#!/usr/bin/python3
"""Module that takes a url and sends a request printing the body or error"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print('Error code: {}'.format(r.status_code))
    else:
        print(r.text)
