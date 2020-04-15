#!/usr/bin/python3
"""Module that takes a url and displays the value of one of the headers"""
from sys import argv
from urllib import request


if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        header = response.getheader('X-Request-Id')
    print(header)
