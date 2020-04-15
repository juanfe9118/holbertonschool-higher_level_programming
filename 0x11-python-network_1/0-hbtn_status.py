#!/usr/bin/python3
"""Module that fectches a webpage"""
import urllib.request


req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    body = response.read()
    print(body)
