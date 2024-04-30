#!/usr/bin/python3
"""Python networking using urllib to
fetch https://alx-intranet.hbtn.io/status"""
import urllib.request


"""
Urllib Response objects
response.read
response.readinto
response.getheaders
fileno
msg
version
url
headers
status
reason
debuglevel
closed
info
getcode
"""
if __name__ == "__main__":
    URI = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(URI) as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf8 content: {html.decode('utf-8')}")
