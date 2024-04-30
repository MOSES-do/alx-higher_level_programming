#!/usr/bin/python3
"""display body of a client to server response"""


import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    try:
        response = urllib.request.urlopen(sys.argv[1])
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(response.read().decode('utf-8'))
