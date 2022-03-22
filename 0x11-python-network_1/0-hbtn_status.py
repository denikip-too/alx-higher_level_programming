#!/usr/bin/python3
"""display my status"""
import urllib.request


def status():
    """display my status"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        f = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(f)))
        print("\t- content: {}".format(f))
        print("\t- utf8 content: {}".format(f.decode("utf8")))


if __name__ == "__main__":
    status()
