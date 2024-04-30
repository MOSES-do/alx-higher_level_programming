#!/usr/bin/python3
"""Python script to request response  and display X-Request-Id value"""


import urllib.request
import sys


if __name__ == '__main__':
    """from header response object key:value pairs using ".get('key')"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        html_id = response.headers.get('X-Request-Id')
        print(html_id)
