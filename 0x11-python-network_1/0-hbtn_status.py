#!/usr/bin/python3
"""Python networking using urllib to fetch https://alx-intranet.hbtn.io/status"""
import urllib.request
if __name__ == "__main__":
  URI = urllib.request.Request('https://alx-intranet.hbtn.io/status')
  with urllib.request.urlopen(URI) as response:
    html = response.read()
    print("Body response:")
    print(f"\t- type: {type(html)}")
    print(f"\t- content: {html}")
    print(f"\t- utf8 content: {html.decode('utf-8')}")
