#!/usr/bin/python3

"""fetch url using requests"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url)
    if r.status_code == 200:
        print("Body response:")
        print(f"\t- type: {type(r.text)}")
        print(f"\t- content: {r.text}")
