#!/usr/bin/python3
"""print error code on error
"""
from urllib import request
from urllib.error import HTTPError
from sys import argv

try:
    with request.urlopen(argv[1]) as response:
        print(response.read().decode('utf-8'))
except HTTPError as e:
    print('Error code: {}'.format(e.code))
