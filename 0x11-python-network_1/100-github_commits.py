#!/usr/bin/python3
"""Module that takes user and password and returns the github id"""
from sys import argv
import requests


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}'.format(owner, repo)
    url += '/commits?per_page=10'
    req = requests.get(url)
    commits = req.json()
    for commit in commits:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
