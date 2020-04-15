#!/usr/bin/python3
"""Module that takes a URL and an email as parameter and prints the email"""
from sys import argv
from urllib import request, parse


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        email = response.read()
    print(email.decode('utf8'))
