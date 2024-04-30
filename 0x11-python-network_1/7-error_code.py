#!/usr/bin/python3

"""Managing error code in python HTTP library REQUESTS"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.text)
    except requests.exceptions.HTTPError as e:
        print(e.status_code)
