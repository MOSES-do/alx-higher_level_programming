#!/usr/bin/python3

"""script that takes my Github credentials (uname and pword)..."""


import requests
import sys


if __name__ == "__main__":
    """and uses the github API to display my id"""
    url = f"https://api.github.com/users/{sys.argv[1]}"
    basic = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get(url, auth=basic)
    if req.status_code == 200:
        user_id = req.json()
        print(user_id.get('id'))
