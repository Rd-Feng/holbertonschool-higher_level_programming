#!/usr/bin/python3
"""print error code on error
"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get(argv[1])
    try:
        r.raise_for_status()
        print(r.content.decode(r.encoding))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
