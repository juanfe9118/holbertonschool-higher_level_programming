#!/usr/bin/python3
"""Module that fetches the body of a URL"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    body = r.text
    print('Body response:')
    print('\t- type: {}'.format(type(body)))
    print('\t- content: {}'.format(body))
