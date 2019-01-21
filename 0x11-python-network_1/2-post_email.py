#!/usr/bin/python3
"""POST email to url
"""
from urllib import request, parse
from sys import argv


url = argv[1]
args = parse.urlencode({'email': argv[2]}).encode('utf-8')
with request.urlopen(argv[1], args) as response:
    print(response.read().decode('utf-8'))
