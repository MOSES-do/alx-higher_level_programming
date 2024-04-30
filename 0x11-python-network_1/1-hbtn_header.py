#!/usr/bin/python3
"""Python script to request response  and display X-Request-Id value
from header object and key values using ".get('key')"""


import urllib.request
import sys


if __name__ == '__main__':
    URI = sys.argv[1]
    with urllib.request.urlopen(URI) as response:
        html_id = response.headers.get('X-Request-Id')
        print(html_id)
