#!/usr/bin/python3
"""Python netwoking using urllib"""
import urllib.request

req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
  html = response.read()
  print("Body response:")
  print(f" - type: {type(html)}")
  print(f" - content: {html}")
  print(f" - utf8 content: {html.decode('utf-8')}")
