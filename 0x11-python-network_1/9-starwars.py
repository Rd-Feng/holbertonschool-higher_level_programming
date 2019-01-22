#!/usr/bin/python3
"""sends a get request to search people using swapi
"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://swapi.co/api/people/?search=' + argv[1])
    results = r.json().get('results')
    print('Number of results: {}'.format(len(results)))
    for result in results:
        print(result.get('name'))
