#!/usr/bin/python3
"""get response header X-Request-Id
"""
from urllib import request
from sys import argv


with request.urlopen(argv[1]) as response:
    print(response.info().get('X-Request-Id'))
