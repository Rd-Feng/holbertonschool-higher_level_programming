#!/usr/bin/python3
"""sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter to query for a user
"""
import requests
from sys import argv


if __name__ == '__main__':
    args = {'q': ""}
    try:
        args['q'] = argv[1]
    except:
        pass
    r = requests.post('http://0.0.0.0:5000/search_user', data=args)
    u = {}
    try:
        u = r.json()
    except:
        print('Not a valid JSON')
    if len(u):
        print('[{}] {}'.format(u['id'], u['name']))
    else:
        print('No result')
