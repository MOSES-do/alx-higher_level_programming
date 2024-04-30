#!/usr/bin/python3
"""display body of a client to server response"""


import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
