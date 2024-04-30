#!/usr/bin/python3
"""send an email as parameter to a url"""


import urllib.request
import urllib.parse
import sys


url = sys.argv[1]
email = sys.argv[2]


if __name__ == "__main__":
    """send an email as parameter to a url"""
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
