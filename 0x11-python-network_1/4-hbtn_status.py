#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    content = r.content.decode(r.encoding)
    print('Body response:')
    print('\t- type: {}'.format(type(content)))
    print('\t- content: {}'.format(content))
