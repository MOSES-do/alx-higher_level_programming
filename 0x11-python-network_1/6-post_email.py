#!/usr/bin/python3

"""Using POST with python's request library"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.post(url, data={'email': sys.argv[2]})
    if r.status_code == 200:
        print(r.text)
