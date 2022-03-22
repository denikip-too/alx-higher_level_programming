#!/usr/bin/python3
"""POST an email"""
import urllib.request
import urllib.parse
import sys


def post_email():
    """sends a POST request to the passed URL with the email as a parameter"""
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        f = response.read()
        print(f.decode("utf-8"))


if __name__ == "__main__":
    post_email()
