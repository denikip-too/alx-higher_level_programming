#!/usr/bin/python3
""" displays Error code"""
import requests
import sys


def error_code():
    """displays Error code"""
    r = requests.get(sys.argv[1])
    try:
        if r.status_code >= 400:
            print("Error code: {}".format(r.status_code))
        else:
            print(r.content)
    except:
        pass


if __name__ == "__main__":
    error_code()
