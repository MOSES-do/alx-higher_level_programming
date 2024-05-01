#!/usr/bin/python3

"""script that takes my Github credentials (uname and pword)..."""


import requests
import sys


if __name__ == "__main__":
    """and uses the github API to display my id"""
    if len(sys.argv) > 2:
        url = f"https://api.github.com/repos/{sys.argv[1]}\
        /{sys.argv[2]}/commits"
        req = requests.get(url)
        if req.status_code == 200:
            last_10_commits = req.json()
            for commit in last_10_commits[:10]:
                print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    else:
        params = sys.argv[1].split("/")
        u_name = params[0]
        repo = params[1]
        url = f"https://api.github.com/repos/{u_name}/{repo}/commits"
        req = requests.get(url)
        if req.status_code == 200:
            last_10_commits = req.json()
            for commit in last_10_commits[:10]:
                print(f"{commit['sha']}: {commit['commit']['author']['name']}")
