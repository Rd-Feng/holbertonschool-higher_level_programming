#!/usr/bin/python3
"""get response header X-Request-Id
"""
import urllib.request
from sys import argv


with urllib.request.urlopen(argv[1]) as response:
    print(response.info().get('X-Request-Id'))
