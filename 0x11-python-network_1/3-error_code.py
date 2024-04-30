#!/usr/bin/python3
"""display body of a client to server response"""

import urllib.request
import urllib.error
import sys


if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    try:
        response = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(response.read().decode('utf-8'))
