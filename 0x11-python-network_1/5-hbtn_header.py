#!/usr/bin/python3
"""sends request to URL and displays value of variable X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
