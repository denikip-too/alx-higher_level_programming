#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(sys.argv[1], sys.argv[2])))
    print(result.json().get("id"))
