#!/usr/bin/python3
"""Module that takes a URL and email and displays the email"""
from sys import argv
import requests


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    email = r.text
    print(email)
