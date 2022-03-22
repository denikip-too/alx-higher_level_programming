#!/usr/bin/python3
"""displays value of X-Request-Id variable found in the header of response"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        f = response.info()
        print(f["X-Request-Id"])
