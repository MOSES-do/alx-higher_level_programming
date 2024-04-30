#!/usr/bin/python3
"""display body of a client to server response"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print(f"Error code: {e.code}")
    else:
        print(response.read().decode('utf-8'))
