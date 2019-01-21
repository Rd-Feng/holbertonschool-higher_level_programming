#!/usr/bin/python3
"""get response header X-Request-Id
"""
import requests
from sys import argv


r = requests.get(argv[1])
print(r.headers.get('X-Request-Id'))
