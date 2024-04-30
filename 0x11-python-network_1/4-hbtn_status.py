#!/usr/bin/python3

"""fetch url using requests"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    r = requests.get(url).text
    print("Body response:")
    print(f"    - type: {type(r)}")
    print(f"    - content: {r}")
