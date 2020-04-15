#!/usr/bin/python3
"""Module that takes user and password and returns the github id"""
from sys import argv
import requests


if __name__ == "__main__":
    user = argv[1]
    pswd = argv[2]
    req = requests.get('https://api.github.com/user', auth=(user, pswd))
    user = req.json().get('id')
    print(user)
