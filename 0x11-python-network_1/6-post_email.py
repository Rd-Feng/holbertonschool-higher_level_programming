#!/usr/bin/python3
"""POST email to url
"""
import requests
from sys import argv


url = argv[1]
args = {'email': argv[2]}
r = requests.post(url, data=args)
print(r.content.decode(r.encoding))
