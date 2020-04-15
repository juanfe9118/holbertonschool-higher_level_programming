#!/usr/bin/python3
"""Module that """
from sys import argv
import requests


if __name__ == "__main__":
    try:
        letter = argv[1]
    except IndexError:
        letter = ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        _dict = req.json()
        _id = _dict['id']
        name = _dict['name']
        print('[{}] {}'.format(_id, name))
    except ValueError:
        print("Not a valid JSON")
    except KeyError:
        print("No result")
