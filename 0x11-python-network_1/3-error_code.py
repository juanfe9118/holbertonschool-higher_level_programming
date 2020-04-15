#!/usr/bin/python3
"""Module that takes a URL and sends a request printing the body or error"""
from sys import argv
from urllib import request, error


if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
