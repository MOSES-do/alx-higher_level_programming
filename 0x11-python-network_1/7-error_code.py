#!/usr/bin/python3

"""Managing error code in python HTTP library REQUESTS"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code == 200:
        print(r.text)
    elif (r.status_code > 400):
        print(f"Error code: {r.status_code}")
